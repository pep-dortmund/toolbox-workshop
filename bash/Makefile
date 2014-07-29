CONTENT := $(addprefix content/, $(addsuffix .tex, bash))

build/bash.pdf: bash.tex $(CONTENT) ../common/header/packages.tex ../common/header/options.tex ../common/header/commands.tex | build
	@../common/tex.sh bash.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --fast bash.tex

clean:
	rm -rf build
