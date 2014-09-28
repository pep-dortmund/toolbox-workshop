CATEGORIES := 1-python 2-numpy 3-matplotlib 4-uncertainties 5-make 6-git 7-all

all: package

exercises:
	for category in $(CATEGORIES) ; do \
		if [ -e "$$category/Makefile" ] ; then \
			make -C "$$category" ; \
		fi ; \
	done

package: exercises
	rm -rf build
	mkdir -p build/exercises-toolbox-{1,2,3,4,5}
	cp -r 1-python 2-numpy build/exercises-toolbox-1
	cp -r 3-matplotlib 4-uncertainties build/exercises-toolbox-2
	cp -r 5-make build/exercises-toolbox-3
	cp -r 6-git build/exercises-toolbox-4
	cp -r 7-all build/exercises-toolbox-5
	rm -f build/exercises-toolbox-{1,2,3,4,5}/*/Makefile
	rm -f build/exercises-toolbox-{1,2,3,4,5}/*/*/Makefile
	rm -f build/exercises-toolbox-{1,2,3,4,5}/*/.gitignore
	rm -f build/exercises-toolbox-{1,2,3,4,5}/*/*/.gitignore
	rm -rf build/exercises-toolbox-{1,2,3,4,5}/*/*/__pycache__
	cd build ; \
	for day in 1 2 3 4 5 ; do \
		zip -r exercises-toolbox-$$day.zip exercises-toolbox-$$day ; \
	done

clean:
	git clean -Xdf
