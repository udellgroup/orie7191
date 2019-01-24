"""Todo:
* add links to coauthors webpages
* allow sorting by publication type
* allow sorting by topic
* enforce consistent capitalization, and parse string as bibtex does (eg, special characters, escapes)
* enforce consistent author first names (my bibstylefile for Nice LVMs does this)
"""

import sys, re

def insert_links(mdfile, bib2str, outfile=sys.stdout):
	with open(mdfile, "r") as file:
		for i,line in enumerate(file):
			# remove comments
			if line[0] == "%": continue                    # remove comment lines
			line = re.sub(re.compile("%.*?\n" ), "", line) # remove all occurance singleline comments (% COMMENT\n ) from string
			line = re.sub(re.compile("<!--.*?-->",re.DOTALL ), "", line) # remove all single line html comments (/*COMMENT */) from string
			# insert links
			line_with_refs = re.sub("\[.*?\]", bib2str, line)
			outfile.write(line_with_refs.strip() + "\n")

def print_papers_only(mdfile, bib2str, outfile=sys.stdout):
	with open(mdfile, "r") as file:
		for i,line in enumerate(file):
			# remove comments
			if line[0] == "%": continue                    # remove comment lines
			line = re.sub(re.compile("%.*?\n" ), "", line) # remove all occurance singleline comments (% COMMENT\n ) from string
			line = re.sub(re.compile("<!--.*?-->",re.DOTALL ), "", line) # remove all single line html comments (/*COMMENT */) from string
			# print all papers found
			for m in re.finditer("(\[.*?\])", line):
				outfile.write(bib2str(m) + "\n")

def extract_papers(bibfile):
	papers = {}
	with open(bibfile, "r") as file:
		paper = {}
		for i,line in enumerate(file):
			m = re.search("@.+{(.+),", line)
			if m:
				# end old paper
				if paper:
					validate_paper(paper)
					paper["bib"] += "}"
					papers[paper["id"]] = paper
				# new paper
				paper = {}
				paper["bib"] = line
				paper["id"] = m.group(1)
			else:
				line = line.strip()
				splut = line.split("=")
				if len(splut) == 2:
					paper[splut[0].strip()] = format_string(splut[1])
					paper["bib"] += "\t" + line + "\n"
	if paper:
		validate_paper(paper)
		paper["bib"] += "}"
		papers[paper["id"]] = paper
	return papers

def validate_paper(paper, required_keys = ["year", "author", "title"]):
	k = paper.keys()
	for key in required_keys:
		if key not in k:
			raise ValueError("Every paper must have a " + key + ".\n" + str(paper))

def format_string(string):
	return string.strip().strip(",").replace("{","").replace("}","").strip('"')

def print_by_year(papers, outfile):
	for paper in sorted(papers, key = lambda paper: paper["year"], reverse=True):
		write_paper(paper, outfile)

"""
Write paper in long form (several lines) as html
"""
def write_paper(paper, file):
	if True:
		# title
		file.write("<p><b>"+paper["title"]+"</b><br>\n")
		# authors
		file.write(format_authors(paper["author"])+"<br>\n")
		# journal, year
		if "journal" in paper.keys():
			where = paper["journal"]
			file.write(where + ", " + paper["year"] +"<br>\n")
		elif "booktitle" in paper.keys():
			where = paper["booktitle"]
			file.write(where + ", " + paper["year"] +"<br>\n")
		elif "howpublished" in paper.keys():
			where = paper["howpublished"]
			file.write(where + ", " + paper["year"] +"<br>\n")
		else:
			file.write(paper["year"] +"<br>\n")
			print("\tpaper has no publication information:")
			print("\t"+paper["title"] + "\n")
		if "comment" in paper.keys():
			file.write(paper["comment"] + "<br>\n")

		# links
		links = format_links(paper, ["arxiv", "pdf", "url", "slides", "code", "bib", "video"])
		if links:
			file.write(links+"<br>\n")

		# spacing to next paper
		file.write("\n")
	# except:
	# 	raise TypeError("Paper incorrectly formatted:\n"+str(paper))

"""returns a string of the (short form) of authors' names + title of paper"""
def format_paper(bibref, papers):
	id = bibref.group(0)[1:-1] # exclude brackets
	if id in papers.keys():
		p = papers[id]
		description = format_authors_short(p["author"]) + " " + p["year"] + ". " + p["title"]
		return description
	else:
		return id

def format_links(paper, link_types):
	links = ""
	for link in link_types:
		if link == "arxiv":
			if "archivePrefix" in paper.keys() and paper["archivePrefix"] == "arXiv" and "eprint" in paper.keys():
				links += '<a href="http://www.arxiv.org/abs/' + paper["eprint"] + '">[arxiv]</a>'
		elif link == "bib":
				fn = 'bib/' + paper["id"] + '.bib'
				links += '<a href="' + fn + '">[bib]</a>'
				with open(fn, "w") as file:
					file.write(paper["bib"])
		elif link in paper.keys():
			links += '<a href="' + paper[link] + '">[' + link + ']</a>'
	return links

"""Return a string of all authors' names"""
def format_authors(string):
	authorlist = string.split(" and ")
	authors = [list(reversed(a.strip().strip("{").strip("}").split(", "))) for a in authorlist]
	# first initial only
	for a in authors:
		for i in range(len(a)-1):
			a[i] = a[i][0] + "."
	authors = [" ".join(a) for a in authors]
	if len(authors) > 2:
		authorstring = ", ".join(authors[:-1]) + ", and " + authors[-1]
	else:
		authorstring = " and ".join(authors)
	return authorstring

"""Return a string of the authors' names, or the first author et al. if there are >3 authors"""
def format_authors_short(string):
	authorlist = string.split(" and ")
	authors = [list(reversed(a.strip().strip("{").strip("}").split(", "))) for a in authorlist]
	# last names only
	last_names = [a[-1] for a in authors]
	if len(authors) > 3:
		authorstring = last_names[0] + " et al."
	elif len(authors) > 2:
		authorstring = ", ".join(last_names[:-1]) + ", and " + last_names[-1]
	else:
		authorstring = " and ".join(last_names)
	return authorstring

def format_citation(bibref, papers):
	id = bibref.group(0)[1:-1] # exclude brackets
	if id in papers.keys():
		p = papers[id]
		link = getlink(p)
		description = format_authors_short(p["author"]) + " " + p["year"]
		if link:
			return "[" + description + "](" + link + ")"
		else:
			return "[" + description + "](???)"
	else:
		return "[" + id + "]" # maybe it already had the link following

def getlink(paper):
	if "url" in paper.keys():
		return paper["url"]
	elif "pdf" in paper.keys():
		return paper["pdf"]
	else:
		ValueError("Can't find link for bibref " + paper["id"])

if __name__ == '__main__':

	mdfile = sys.argv[1]
	bibfile = sys.argv[2]
	papers = extract_papers(bibfile)
	# insert_links(mdfile, lambda bibref: format_citation(bibref, papers))
	print_papers_only(mdfile, lambda bibref: format_paper(bibref, papers))
