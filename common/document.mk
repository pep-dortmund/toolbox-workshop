HEADER := $(addprefix ../common/, header.tex packages.tex settings.tex commands.tex beamerthemevertex.sty)

DOCUMENT := $(shell basename "$$(pwd)")

build/$(DOCUMENT).pdf: $(DOCUMENT).tex $(HEADER) content/*.tex | build
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" $(BIBER) $(DOCUMENT).tex

build/figures/%.pdf: figures/%.crop | build/figures
	@../common/crop.py "$<" "$@"

build build/figures:
	mkdir -p build/figures

fast:
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" --fast $(BIBER) $(DOCUMENT).tex

clean:
	rm -rf build

.DELETE_ON_ERROR:

.PHONY: all fast clean
