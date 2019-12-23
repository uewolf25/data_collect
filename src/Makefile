py = python3
MAIN = data_collect.py
SUB = ranking.py
DEL = delete.sh
TFIDF = tf_idf.py
# GEN = generate.sh

tfidf: $(TFIDF)
	@echo 'calculation tf-idf ...'
	@$(py) $(TFIDF)

rank: $(SUB)
	@echo ''
	@$(py) $(SUB)

all: $(SUB) $(DEL)
	@echo 'Deleting text files ...'
	@sh $(DEL)
	@echo 'Running ' $(SUB) ' script ...'
	$(py) $(SUB)

main: $(MAIN) $(SUB)
	$(py) $(MAIN)
	@echo '---------------------------------------------------------'
	$(py) $(SUB)

install: $(MAIN)
	$(py) $(MAIN)

# run: $(SUB) $(GEN)
# 	@sh $(GEN)
# 	@echo 'Running ' $(SUB) ' script ...'
# 	$(py) $(SUB)

clean: $(DEL)
	@echo 'Deleting directories and text files ...'
	@sh $(DEL)

# reset-txt: $(GEN)
# 	@echo 'resetting only text files ...'
# 	@sh $(GEN)
