CONTENT := $(addprefix content/, $(addsuffix .tex, bash))

build/bash.pdf: bash.tex $(CONTENT) ../common/header/packages.tex ../common/header/options.tex ../common/header/commands.tex | build
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" bash.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" --fast bash.tex

clean:
	rm -rf build
