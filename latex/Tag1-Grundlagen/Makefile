all: toolbox-LaTeX-Tag1.pdf

toolbox-LaTeX-Tag1.pdf: toolbox-LaTeX-Tag1.tex *.sty
	lualatex toolbox-LaTeX-Tag1.tex
	lualatex toolbox-LaTeX-Tag1.tex
	mkdir -p logfiles
	mv *.vrb *.log *.aux *.nav *.out *.snm *.toc logfiles/

clean:
	rm -r logfiles
