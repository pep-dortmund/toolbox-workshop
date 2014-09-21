EXERCISES := "303 Der Lock-In-Verstärker" "354 Gedaempfte und erzwungene Schwingungen" "406 Beugung am Spalt" "702 Aktivierung mit Neutronen"

all:
	for exercise in $(EXERCISES) ; do \
		make -C "$$exercise" -f Makefile-loesung ; \
	done
