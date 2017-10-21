Kuchen: Teig Backen

Teig: Milch Eier Mehl Zucker Rumrosinen | Schüssel
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

Backen: Backofen
	@echo "Backofen wird vorgeheizt"
	@sleep 5
	@echo "Kuchen wird gebacken..."
	@sleep 5
	@echo "Kuchen ist fertig"
	@touch kuchen
	@echo "The cake is a lie!" > kuchen

Rumrosinen: Rum Rosinen
	@touch Rumrosinen
	@echo "Rosinen werden in Rum eingelegt"
	@echo "Vier Wochen warten......"
	@sleep 10
	@cat Rum     >> Rumrosinen
	@cat Rosinen >> Rumrosinen

Schüssel:
	@touch Schüssel

clean:
	rm Schüssel
	rm Rumrosinen
	rm kuchen
