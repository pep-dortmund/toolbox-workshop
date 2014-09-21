DOCUMENTS := exercises git intro latex make python unix

all:
	for document in $(DOCUMENTS) ; do \
		make -C "$$document" ; \
	done

clean:
	for document in $(DOCUMENTS) ; do \
		make -C "$$document" clean ; \
	done
