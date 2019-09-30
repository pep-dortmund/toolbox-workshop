include common/common.mk

all:

include common/recursive.mk

all: $(BUILDS)

all: latex-template/build/latex-template.zip

latex-template/build/latex-template.zip: latex-template_build
	@rm -f $@
	zip -rq $@ latex-template --exclude latex-template/build/\*

CLEANS := $(addsuffix _clean, $(DIRS))

clean: $(CLEANS)

%_clean:
	@[ ! -e $*/Makefile ] || $(MAKE) -C $* clean

FORCE: $(CLEANS)

.PHONY: all clean
