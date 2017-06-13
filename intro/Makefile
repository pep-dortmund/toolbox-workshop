include ../common/common.mk
include ../common/document.mk

FIGURES := $(addprefix build/figures/, $(addsuffix .pdf, os programming interest))

build/intro.pdf: $(FIGURES) $(addprefix build/figures/, editors.jpg vim.png emacs.png real_programmers.png matplotlib.png sympy.png scipy.png numpy.png atom.jpg)

build/figures/os.pdf: script/answers.py data/2015.tsv
	TEXINPUTS=$(shell pwd): python3 $<

$(addprefix build/figures/, programming.pdf interest.pdf): build/figures/os.pdf

build/figures/editors.jpg: | build/figures
	wget http://www.manuelmagic.me/manuelsweb/resources/Geek/Text-editors/text_editors.jpg -O $@ --no-use-server-timestamps

build/figures/vim.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Vimlogo.svg/500px-Vimlogo.svg.png -O $@ --no-use-server-timestamps

build/figures/emacs.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Emacs-logo.svg/500px-Emacs-logo.svg.png -O $@ --no-use-server-timestamps

build/figures/real_programmers.png: | build/figures
	wget http://imgs.xkcd.com/comics/real_programmers.png -O $@ --no-use-server-timestamps

build/figures/matplotlib.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Matplotlib_logo.svg/500px-Matplotlib_logo.svg.png -O $@ --no-use-server-timestamps

build/figures/sympy.png: | build/figures
	wget http://docs.sympy.org/latest/_static/sympylogo.png -O $@ --no-use-server-timestamps

build/figures/scipy.png: | build/figures
	wget https://raw.githubusercontent.com/scipy/scipy-sphinx-theme/master/_static/scipyshiny_small.png -O $@ --no-use-server-timestamps

build/figures/numpy.png: | build/figures
	wget http://www.numpy.org/_static/numpy_logo.png -O $@ --no-use-server-timestamps

build/figures/atom.jpg: | build/figures
	wget https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Atom_editor_logo.svg/2000px-Atom_editor_logo.svg.png -O $@ --no-use-server-timestamps
