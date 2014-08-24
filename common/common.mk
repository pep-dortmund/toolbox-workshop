HEADER := $(addprefix ../common/, header.tex beamercolorthemeTUDo.sty beamerfontthemeTUDo.sty beamerinnerthemeTUDo.sty beamerouterthemeTUDo.sty beamerthemeTUDo.sty)

DOCUMENT := $(shell basename "$$(pwd)")

build/$(DOCUMENT).pdf: $(DOCUMENT).tex $(HEADER) content/*.tex | build
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" $(DOCUMENT).tex

build/figures/%.pdf: figures/%.crop | build/figures
	@../common/crop.py "$<" "$@"

build build/figures:
	mkdir -p build/figures

fast:
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" --fast $(DOCUMENT).tex

clean:
	rm -rf build
