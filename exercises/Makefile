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
	mkdir -p build/exercises
	cp -r $(CATEGORIES) build/exercises
	rm build/exercises/*/Makefile
	rm build/exercises/*/.gitignore
	rm build/exercises/*/*/.gitignore
	rm -r build/exercises/*/*/__pycache__
	cd build && zip -r exercises.zip exercises

clean:
	git clean -Xf
