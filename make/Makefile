CONTENT := $(addprefix content/, $(addsuffix .tex, make))

build/slides.pdf: slides.tex $(CONTENT) ../common/header/packages.tex ../common/header/options.tex ../common/header/commands.tex | build
	@../common/tex.sh slides.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --fast slides.tex

clean:
	rm -rf build
