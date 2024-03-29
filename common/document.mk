DOCUMENT := $(shell basename "$$(pwd)")

build/$(DOCUMENT).pdf: FORCE  | build
	TEXINPUTS="$(shell pwd)/../common/:" \
	max_print_line=1048576 \
	latexmk -r $(shell pwd)/../common/latexmkrc \
	$(DOCUMENT).tex

preview: FORCE | build
	TEXINPUTS="$(shell pwd)/../common/:" \
	max_print_line=1048576 \
	latexmk --interaction=nonstopmode -pvc -r $(shell pwd)/../common/latexmkrc \
	$(DOCUMENT).tex

build/figures/%.pdf: figures/%.crop | build/figures
	@../common/crop.py "$<" "$@"

build build/figures:
	mkdir -p build/figures

clean:
	rm -rf build

FORCE:

.PHONY: all fast clean FORCE
