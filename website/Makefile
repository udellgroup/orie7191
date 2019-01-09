DOCS=index

HDOCS=$(addsuffix .html, $(DOCS))
MDOCS=$(addsuffix .md, $(DOCS))
PHDOCS=$(HDOCS)
SERVER=mru8@courses.cit.cornell.edu:~/coursewww/mru8/orie7191/

.PHONY : docs
docs : $(PHDOCS)

.PHONY : update
update : $(PHDOCS)
	@echo -n 'Syncing to server...'
	rsync -avz --no-p *.css $(SERVER)
	rsync -avz --no-p *.html $(SERVER)
	@echo ' done.'

index.html : index.md
	grip index.md > index.html

index.md : syllabus.md
	python add_links_from_bib.py syllabus.md reading.bib > index.md

.PHONY : clean
clean :
	-rm -f *.html
