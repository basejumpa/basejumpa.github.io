# Entry points for docs-as-code framework                                     #
###############################################################################
###############################################################################

# Deactivate all default rules
.SUFFIXES:

# Deactivate all built-in implicit targets
.DEFAULT:

# Run w/o explicit target(s)
.PHONY: default
default: help


### CONFIGURATION #############################################################
# You can set these variables from the command line, and also
# from the environment for the first two.

# Determine the directory where the current Makefile is located
MAKEFILE_PATH := $(abspath $(firstword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(dir $(MAKEFILE_PATH))

include $(MAKEFILE_DIR)/.config


### FIDDLE AREA ###############################################################

.PHONY: fiddle
fiddle:
	echo fiddle


### IMPLEMENTATION ############################################################

define HELP_SCREEN
Usage: make -f doc/Makefile <target>
Make target for working with the documentation

Known targets are are:

    install       : (Re)-install necessary development environment.
                    The environment is being installed in a virtual environment in subfolder .venv/ of the
                    local repository folder.
                    All tools except Latex, necessary for command build-pdf are installed.
    html          : Make documentation in HTML format
    html-live     : Continuous (re-)build of HTML output.
                    Rebuild is being triggered by file changes inside folder CONFIG_BUILD__DIRS__BUILD. Start local webserver.
    clean         : Clean build output folder (default: out/docs)
    clean-install : Remove complete installation (located in .venv/)
                    Next other command will re-install tools.
    help          : Show this screen
endef


# Create configuration file with defaults if it doesn't exist



# Always invoke one shell for all lines in a recipe
# @see https://www.gnu.org/software/make/manual/html_node/One-Shell.html
.ONESHELL:


ifeq ($(OS),Windows_NT)
SHELL = git-bash
else
SHELL = /bin/bash
endif

PYTHON = python3


# Disable all implicit targets
MAKEFLAGS += --no-builtin-rules
.SUFFIXES:


# Enable parallel execution (where possible)
MAKEFLAGS += ---jobs=5


.PHONY: help
help:
	$(info $(HELP_SCREEN))


.PHONY: install
install: clean-install .tools/.are-up-to-date


.tools/.are-up-to-date:
	$(PYTHON) -m pipx install poetry
	export PATH="$$PATH:$$HOME/.local/bin" # Works for root. Not tested for other users.
	mkdir .tools/
	curl -L -o .tools/plantuml.jar https://github.com/plantuml/plantuml/releases/download/v1.2024.6/plantuml-1.2024.6.jar
	touch .tools/.are-up-to-date

# Additional tool prerequisites:
#
# scoop install \
#    draw.io \
#    make \
#    npm \
#    miktex
#
# npm install -g \
#    @mermaid-js/mermaid-cli


.PHONY: deps-are-up-to-date
deps-are-up-to-date: poetry.toml pyproject.toml
	poetry update


.PHONY: deps-are-up-to-date-dev
deps-are-up-to-date-dev: poetry.toml pyproject.toml
	poetry update --with dev


.PHONY: clean
clean:
	rm -rf "$(CONFIG_BUILD__DIRS__BUILD)"


clean-install:
	rm -rf .venv/
	rm -rf .tools/
	rm -f  poetry.lock


.PHONY: config
config: .tools/.are-up-to-date deps-are-up-to-date-dev
	(cd "$(CONFIG_BUILD__DIRS__CONFIG)" ; poetry run menuconfig )


.PHONY: html
html: .tools/.are-up-to-date deps-are-up-to-date
	mkdir -p "$(CONFIG_BUILD__DIRS__BUILD)/$@"
	@echo "Building sources at $(CONFIG_BUILD__DIRS__SOURCE)"
	poetry run sphinx-build \
        -W \
        -c  "$(CONFIG_BUILD__DIRS__CONFIG)" \
            "$(CONFIG_BUILD__DIRS__SOURCE)" \
            "$(CONFIG_BUILD__DIRS__BUILD)/$@"


.PHONY: html-live
html-live: .tools/.are-up-to-date deps-are-up-to-date-dev
	mkdir -p "$(CONFIG_BUILD__DIRS__BUILD)/$@"
	# Start continuous build, open browser automatically which reloads on change.
	@echo "Building sources at $(CONFIG_BUILD__DIRS__SOURCE)"
	poetry run sphinx-autobuild \
        -j 10 \
        -W \
        -c      "$(CONFIG_BUILD__DIRS__CONFIG)" \
        --watch "$(CONFIG_BUILD__DIRS__CONFIG)" \
                "$(CONFIG_BUILD__DIRS__SOURCE)" \
                "$(CONFIG_BUILD__DIRS__BUILD)/$@" \
        --re-ignore '_tags/.*' \
        --port  "$(CONFIG_BUILD__LIVE__PORTS__HTML)" \
        --open-browser

