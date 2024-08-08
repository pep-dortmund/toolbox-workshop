include ../../common/common.mk
include ../../common/generate_vorlage.mk

DIRS := $(sort $(wildcard *))
BUILDS := $(addsuffix _build, $(DIRS))

all: $(BUILDS)

%_build:
	@[ ! -e $*/Makefile-loesung ] || $(MAKE) -f Makefile-loesung -C $*

FORCE: $(BUILDS)

.PHONY: all clean FORCE
