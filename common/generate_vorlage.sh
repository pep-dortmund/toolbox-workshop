#!/bin/bash

find . -name 'vorlage.py' -exec "cp loesung.py vorlage.py \
		& sed -i -e '/# begin solution/,/# end solution' {} \;"

