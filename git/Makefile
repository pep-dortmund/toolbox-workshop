CONTENT := $(addprefix content/, $(addsuffix .tex, git))

build/git.pdf: git.tex $(CONTENT) ../common/header/packages.tex ../common/header/options.tex ../common/header/commands.tex | build
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" git.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" --fast git.tex

clean:
	rm -rf build
