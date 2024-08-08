#!/bin/bash

grep -q '# begin solution' ${1//vorlage/loesung} && : >$1
[ ! -f $1 ] || cp ${1//vorlage/loesung} $1
[ ! -f $1 ] || sed -i -e '/# begin solution/,/# end solution/d' $1
[ -s $1 ] || rm $1
