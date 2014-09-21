CATEGORIES := 1-python 2-numpy 3-matplotlib 4-uncertainties 5-make 6-git 7-all

all:
	for category in $(CATEGORIES) ; do \
		make -C "$$category" ; \
	done

package: all
	rm -rf build/exercises
	mkdir -p build/exercises
	cp -r $(CATEGORIES) build/exercises
	rm build/exercises/*/Makefile
	rm build/exercises/*/.gitignore
	rm build/exercises/*/*/.gitignore
	rm -r build/exercises/*/*/__pycache__
	cd build && zip -r exercises.zip exercises

clean:
	git clean -Xf
