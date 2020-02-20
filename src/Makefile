py = python3
MAIN = search.py
# SUB = ranking.py
DEL = delete.sh

install: $(MAIN) $(DEL)
	@echo 'Deleting directories and text files ...'
	@sh $(DEL)
	$(py) $(MAIN)


clean: $(DEL)
	@echo 'Deleting directories and text files ...'
	@sh $(DEL)
