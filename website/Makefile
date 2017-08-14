DOCS=index about contact lectures projects exams homework

HDOCS=$(addsuffix .html, $(DOCS))
PHDOCS=$(HDOCS)
SERVER=mru8@courses.cit.cornell.edu:~/coursewww/mru8/opt-reading/

.PHONY : docs
docs : $(PHDOCS)

.PHONY : update
update : $(PHDOCS)
	@echo -n 'Syncing to server...'
	rsync -avz --no-p *.css $(SERVER)
	rsync -avz --no-p *.html $(SERVER)
	rsync -avz --no-p eqs $(SERVER)
	@echo ' done.'

%.html : %.jemdoc MENU
	python jemdoc.py -c jemdoc.conf -o $@ $<

.PHONY : clean
clean :
	-rm -f *.html
