CONTENT := $(addprefix content/, $(addsuffix .tex, make))

build/make.pdf: make.tex $(CONTENT) ../common/header/packages.tex ../common/header/options.tex ../common/header/commands.tex | build
	@../common/tex.sh make.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --fast make.tex

clean:
	rm -rf build
