include common/common.mk

all:

include common/recursive.mk

all: $(BUILDS)

all: latex-template/build/latex-template.zip

latex-template/build/latex-template.zip: latex-template_build | latex-template/build
	@rm -f $@
	# FS will recreate the zip, prevents removed files from still being in the zip
	zip -FSrq $@ latex-template --exclude latex-template/vXXX/build/\* --exclude latex-template/build/\*

latex-template/build:
	mkdir -p $@

CLEANS := $(addsuffix _clean, $(DIRS))

clean: $(CLEANS)

%_clean:
	@[ ! -e $*/Makefile ] || $(MAKE) -C $* clean

FORCE: $(CLEANS)

.PHONY: all clean
