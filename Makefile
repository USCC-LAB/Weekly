# Python
PYTHON=python3

# Repo
SCRIPTS=scripts
TEST=tests

# Control verbosity
ifeq ("$(V)", "1")
    Q :=
else
    Q := @
endif

# Rule
all:
	$(Q)true

%_test:
	$(Q)$(PYTHON) -m unittest -v $(TEST).$@

check:
	$(Q)$(PYTHON) -m unittest -v \
		$(TEST).serializer_test \
		$(TEST).scheduler_test \
		$(TEST).roulette_test
#		$(TEST).reader_test \
#		$(TEST).mail_test \
