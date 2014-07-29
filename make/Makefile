all:
	make slides
	make open

slides:
	make tex
	make tex
	biber slides.bcf
	make tex

tex: slides.tex
	lualatex slides.tex

open:
	open slides.pdf

clean:
	rm -f *.aux
	rm -f *.bbl
	rm -f *.bcf
	rm -f *.blg
	rm -f *.log
	rm -f *.nav
	rm -f *.out
	rm -f *.run.xml
	rm -f *.snm
	rm -f *.toc
	rm -f slides.pdf
