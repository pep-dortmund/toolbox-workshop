DOCUMENTS := exercises-latex exercises-toolbox git intro latex make python unix

all:
	for document in $(DOCUMENTS) ; do \
		if [ -e "$$document/Makefile" ] ; then \
			make -C "$$document" ; \
		fi ; \
	done

clean:
	for document in $(DOCUMENTS) ; do \
		if [ -e "$$document/Makefile" ] ; then \
			make -C "$$document" clean ; \
		fi ; \
	done
