CONTENT := $(addprefix content/, $(addsuffix .tex, python))

build/python.pdf: python.tex $(CONTENT) ../common/header/packages.tex ../common/header/options.tex ../common/header/commands.tex | build
	@../common/tex.sh python.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --fast python.tex

clean:
	rm -rf build
