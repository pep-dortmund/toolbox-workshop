CATEGORIES := 1-python 2-numpy 3-matplotlib 4-uncertainties 5-make 6-git 7-all 8-latex

all: package

exercises:
	for category in $(CATEGORIES) ; do \
		if [ -e "$$category/Makefile" ] ; then \
			make -C "$$category" ; \
		fi ; \
	done

package: exercises
	rm -rf build
	mkdir -p build/exercises-{1,2,3,4,5}
	cp -r 1-python 2-numpy build/exercises-1
	cp -r 3-matplotlib 4-uncertainties build/exercises-2
	cp -r 5-make build/exercises-3
	cp -r 6-git build/exercises-4
	cp -r 7-all build/exercises-5
	cp -r 8-latex build/exercises-latex
	rm -f build/exercises-{1,2,3,4,5,latex}/*/Makefile
	rm -f build/exercises-{1,2,3,4,5,latex}/*/*/Makefile
	rm -f build/exercises-{1,2,3,4,5,latex}/*/.gitignore
	rm -f build/exercises-{1,2,3,4,5,latex}/*/*/.gitignore
	rm -rf build/exercises-{1,2,3,4,5,latex}/*/*/__pycache__
	cd build/exercises-latex ; \
	for dir in * ; do \
		cd "$$dir" && mv build/loesung.pdf . && rm -r build && cd .. || true ; \
	done
	cd build ; \
	for day in 1 2 3 4 5 latex ; do \
		zip -r exercises-$$day.zip exercises-$$day ; \
	done

clean:
	git clean -Xf
