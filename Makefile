DOCUMENTS := bash git latex make python

all:
	for document in $(DOCUMENTS) ; do \
		make -C "$$document" ; \
	done

clean:
	for document in $(DOCUMENTS) ; do \
		make -C "$$document" clean ; \
	done
