#!/bin/bash

[ ! -f 'vorlage.py.dummy' ] || cp loesung.py vorlage.py
[ ! -f 'vorlage.py.dummy' ] || find . -name 'vorlage.py' \
		-exec sed -i -e '/# begin solution/,/# end solution/d' {} \;

