.PHONY:	mkdir

TIMESTAMP := $(shell date +%Y%m%d%H%M)
FOLDER_NAME := $(shell echo "$@" | tr '_' ' ' | tr [:lower:] [:upper:] | cut -c1,2- | sed 's/^#//')

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

# Define a rule to create a folder with timestamp prepended
mkdir: ## Run "make mkdir FOLDER=my_folder_name" to create your new reprex folder.
	@echo "Creating $(TIMESTAMP)_$(FOLDER) folder..."
	@mkdir $(TIMESTAMP)_$(FOLDER)
	@touch $(TIMESTAMP)_$(FOLDER)/requirements.txt
	@touch $(TIMESTAMP)_$(FOLDER)/README.md
	@touch $(TIMESTAMP)_$(FOLDER)/main.py
	@python3 -m venv $(TIMESTAMP)_$(FOLDER)/venv
