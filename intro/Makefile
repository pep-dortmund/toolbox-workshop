include ../common/common.mk
include ../common/document.mk

FIGURES := $(addprefix build/figures/, $(addsuffix .pdf, os programming interest))
EXAMPLE_PLOT := build/example_plot.pdf

build/intro.pdf: $(FIGURES) $(EXAMPLE_PLOT) $(addprefix build/figures/, \
	vim.png nano.png real_programmers.png code.png windows.png macos.png tux.jpg\
	fedora.png archlinux.png ubuntu.png debian-openlogo.png \
	)

build/figures/os.pdf: script/answers.py data/toolbox2023.json ../common/matplotlibrc ../common/header-matplotlib.tex
	MATPLOTLIBRC=../common/matplotlibrc TEXINPUTS=$$(pwd)/../common: python3 $<

$(addprefix build/figures/, programming.pdf interest.pdf): build/figures/os.pdf

build/figures/nano.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Gnu-nano.svg/480px-Gnu-nano.svg.png -O $@ --no-use-server-timestamps

build/figures/code.png: | build/figures
	wget https://code.visualstudio.com/assets/images/code-stable.png -O $@ --no-use-server-timestamps

build/figures/vim.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Vimlogo.svg/500px-Vimlogo.svg.png -O $@ --no-use-server-timestamps

build/figures/real_programmers.png: | build/figures
	wget http://imgs.xkcd.com/comics/real_programmers.png -O $@ --no-use-server-timestamps

build/figures/windows.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Windows_logo_and_wordmark_-_2021.svg/1024px-Windows_logo_and_wordmark_-_2021.svg.png -O $@ --no-use-server-timestamps

build/figures/macos.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/MacOS_logo.svg/768px-MacOS_logo.svg.png -O $@ --no-use-server-timestamps

build/figures/tux.jpg: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/d/dd/Linux_logo.jpg -O build/figures/tux-original.jpg --no-use-server-timestamps
	convert build/figures/tux-original.jpg -trim $@

build/figures/debian-openlogo.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Debian-OpenLogo.svg/581px-Debian-OpenLogo.svg.png -O build/figures/debian-openlogo.png

build/figures/ubuntu.png: build/figures
	wget -O $@ --no-use-server-timestamps https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Ubuntu_logo.svg/600px-Ubuntu_logo.svg.png

build/figures/fedora.png: build/figures
	wget -O $@ --no-use-server-timestamps https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Fedora-logo.svg/480px-Fedora-logo.svg.png

build/figures/archlinux.png: build/figures
	wget -O $@ --no-use-server-timestamps https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Archlinux-logo-standard-version.png/1024px-Archlinux-logo-standard-version.png

build/example_plot.pdf: script/example_plot.py | build/figures
	MATPLOTLIBRC=../common/matplotlibrc TEXINPUTS=$$(pwd)/../common: python3 $<
