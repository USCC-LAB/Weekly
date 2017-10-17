# Python
PYTHON = python3

# Repo
SCRIPTS = scripts
TEST = tests

# Src
SRCS = $(shell find -name "*.py")

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

# autopep8 refers to https://github.com/hhatto/autopep8
# pep8 refers to manual page
pep8diff:
	$(Q)autopep8 --diff $(SRCS) | colordiff

pep8stat:
	$(Q)pep8 --statistic -qq $(SRCS)

pep8replace:
	$(Q)autopep8 --in-place --aggressive -a $(SRCS)
