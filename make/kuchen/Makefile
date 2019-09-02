Kuchen: Teig Backofen
	@echo "\n\033[31mBacken\033[0m"
	@echo "Backofen wird vorgeheizt"
	@cat Backofen
	@sleep 5
	@echo "Kuchen wird gebacken..."
	@sleep 5
	@echo "Kuchen ist fertig"
	@touch Kuchen
	@echo "           The cake is a lie!" > Kuchen
	@sleep 2
	@clear -x
	@cat Kuchen
	@cat portal

Teig: Milch Eier Mehl Zucker Rumrosinen | Schüssel
	@echo "\n\033[31mTeig\033[0m"
	@echo "Eier schlagen..."
	@sleep 2
	@cat Eier > Schüssel
	@echo "Milch hinzugeben..."
	@sleep 2
	@cat Milch >> Schüssel
	@echo "Zucker hinzugeben..."
	@sleep 2
	@cat Zucker >> Schüssel
	@echo "Mehl hinzugeben..."
	@sleep 2
	@cat Mehl >> Schüssel
	@echo "Rumrosinen unterrühren..."
	@sleep 2
	@cat Rumrosinen >> Schüssel
	@echo "Teig ist fertig!"
	@cat Schüssel
	@sleep 1

Rumrosinen: Rum Rosinen
	@echo "\033[31mRumrosinen\033[0m"
	@touch Rumrosinen
	@echo "Rosinen werden in Rum eingelegt"
	@cat Rum     >> Rumrosinen
	@cat Rosinen >> Rumrosinen
	@cat Rumrosinen
	@echo "Vier Wochen warten......"
	@sleep 10

Schüssel:
	@touch Schüssel

clean:
	rm -f Schüssel
	rm -f Rumrosinen
	rm -f Kuchen
