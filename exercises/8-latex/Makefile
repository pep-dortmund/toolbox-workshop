EXERCISES := 1-helloworld 2-input 3-lists 4-titlepage 5-structure 6-math 7-siunitx

all:
	for exercise in $(EXERCISES) ; do \
		make -C "$$exercise" -f Makefile-loesung ; \
	done
