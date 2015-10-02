all:

include common/recursive.mk

all: $(BUILDS)

CLEANS := $(addsuffix _clean, $(DIRS))

clean: $(CLEANS)

%_clean:
	@[ ! -e $*/Makefile ] || $(MAKE) -C $* clean

FORCE: $(CLEANS)

.PHONY: all clean
