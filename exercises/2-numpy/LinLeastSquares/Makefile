all: linleastsquares.pdf 

linleastsquares.pdf: linleastsquares.tex
	lualatex linleastsquares
	lualatex linleastsquares
	make clean

extensions = *.log *.aux *.toc *.bbl *.bcf *.run.xml *.blg *.out
clean:
	mkdir -p logfiles
	for file in $(extensions); do \
		if [ -a $$file ] ; \
		then \
			mv $$file logfiles/ ; \
		fi; \
	done

rm: # löscht den Ordner logfiles
	rm -rf logfiles
