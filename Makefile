# Python
PYTHON=python3

# Repo
SCRIPTS=scripts
TEST=tests

# Rule
all:
	true

%_test:
	$(PYTHON) -m unittest $(TEST).$@

check:
	$(PYTHON) -m unittest \
		$(TEST).serialization_test \
		$(TEST).scheduler_test \
		$(TEST).roulette_test
#		$(TEST).reader_test \
#		$(TEST).mail_test \
