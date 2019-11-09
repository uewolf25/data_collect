py = python3
MAIN = data_collect.py
SUB = ranking.py
DEL = delete.sh

run: $(MAIN) $(SUB)
	$(py) $(MAIN)
	echo '---------------------------------------------------------'
	$(py) $(SUB)

install: $(MAIN)
	$(py) $(MAIN)

clean: $(SHELL)
	sh $(DEL)
