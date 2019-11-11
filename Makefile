py = python3
MAIN = data_collect.py
SUB = ranking.py
DEL = delete.sh
GEN = generate.sh

main: $(MAIN) $(SUB)
	$(py) $(MAIN)
	@echo '---------------------------------------------------------'
	$(py) $(SUB)

install: $(MAIN)
	$(py) $(MAIN)

run: $(SUB) $(GEN)
	@sh $(GEN)
	@echo 'Running ' + $(SUB) + ' script ...'
	$(py) $(SUB)

clean: $(SHELL)
	@echo 'Deleting directories and text files ...'
	@sh $(DEL)

reset-txt: $(GEN)
	@echo 'resetting only text files ...'
	@sh $(GEN)
