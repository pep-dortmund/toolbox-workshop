DIRS := $(sort $(wildcard *))
BUILDS := $(addsuffix _build, $(DIRS))

ifndef MAKEFILE
	MAKEFILE := Makefile
endif

%_build:
	@[ ! -e $*/$(MAKEFILE) ] || $(MAKE) -C $* -f $(MAKEFILE)

FORCE: $(BUILDS)

.PHONY: FORCE
