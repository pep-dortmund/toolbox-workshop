all: toolbox-LaTeX.pdf

toolbox-LaTeX.pdf: toolbox-LaTeX.tex *.sty Inhalt/*
	lualatex -shell-escape toolbox-LaTeX.tex
	lualatex -shell-escape toolbox-LaTeX.tex
	mkdir -p logfiles
	mv *.vrb *.log *.aux *.nav *.out *.snm *.toc logfiles/

clean:
	rm -r logfiles
