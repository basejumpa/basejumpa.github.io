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

CONFIG_JSON_FILE := config.json
define CONFIG_JSON_DEFAULT
{
    "project" : "some-project",
    "year"    : "2024",
    "title"   : "title of some-doc",
    "author"  : "author", 
    "language": "en",

    "dirs" : {
        "source": "docs",
        "config": "docs",
        "build" : "out/docs"
    },

    "live": {
        "ports" : {
            "html": 1976
        }
    }
}
endef
export CONFIG_JSON_DEFAULT


Makefile: $(CONFIG_JSON_FILE)

$(CONFIG_JSON_FILE):
	@echo Creating $@
	@echo "$$CONFIG_JSON_DEFAULT" > $@


# Build´
DOC_CFG_SOURCE_DIR      ?= $(shell (cd docs ; python -m config    'dirs/source'))
DOC_CFG_CONFIG_DIR      ?= $(shell (cd docs ; python -m config    'dirs/config'))
DOC_CFG_BUILD_DIR       ?= $(shell (cd docs ; python -m config    'dirs/build'))

# Build-Live
DOC_CFG_HTML_LIVE_PORT  ?= $(shell (cd docs ; python -m config    'live/ports/html'))


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
                    Rebuild is being triggered by file changes inside folder DOC_CFG_BUILD_DIR. Start local webserver.
    clean         : Clean build output folder (default: out/docs)
    clean-install : Remove complete installation (located in .venv/)
                    Next other command will re-install tools.
    help          : Show this screen

Environment variables used:

    DOC_CFG_SOURCE_DIR    : Directory of documentation's source files
                            Absolute or relative to working directory
                            Default: docs
    DOC_CFG_CONFIG_DIR    : Directory where configuration file docs.conf
                            is located. Absolute or relative to working directory.
                            Default: docs
    DOC_CFG_BUILD_DIR     : Build output directory
                            Absolute or relative to working directory
                            Depending on html-live, make-html, make-pdf there
                            Create a subdirectory accordingly (html-live, html or pdf)
                            Default: out/docs

    DOC_CFG_HTML_LIVE_PORT : TCP/IP port of local web server. Default: 1976
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
	curl -L -o .tools/plantuml.jar https://github.com/plantuml/plantuml/releases/download/v1.2024.5/plantuml-1.2024.5.jar
	touch .tools/.are-up-to-date

# Additional tools being prerequisites:
#
# scoop install \
#    draw.io \
#    make \
#    npm \
#    miktex
#
# npm install -g \
#    @mermaid-js/mermaid-cli
#


.PHONY: deps-are-up-to-date
deps-are-up-to-date: poetry.toml pyproject.toml
	poetry update


.PHONY: deps-are-up-to-date-live
deps-are-up-to-date-live: poetry.toml pyproject.toml
	poetry update --with dev


clean-install:
	rm -rf .venv/
	rm -rf .tools/
	rm -f  poetry.lock


.PHONY: clean
clean:
	rm -rf "$(DOC_CFG_BUILD_DIR)"


.PHONY: html-live
html-live: .tools/.are-up-to-date deps-are-up-to-date-live
	mkdir -p "$(DOC_CFG_BUILD_DIR)/$@"
	# Start continuous build, open browser automatically which reloads on change.
	@echo "Building sources at $(DOC_CFG_SOURCE_DIR)"
	poetry run sphinx-autobuild \
        -j 10 \
        -W \
        -c "$(DOC_CFG_CONFIG_DIR)" \
        --watch $(DOC_CFG_CONFIG_DIR) \
        "$(DOC_CFG_SOURCE_DIR)" \
        "$(DOC_CFG_BUILD_DIR)/$@" \
        --re-ignore '_tags/.*' \
        --port "$(DOC_CFG_HTML_LIVE_PORT)" \
        --open-browser


.PHONY: html
html: .tools/.are-up-to-date deps-are-up-to-date
	mkdir -p "$(DOC_CFG_BUILD_DIR)/$@"
	@echo "Building sources at $(DOC_CFG_SOURCE_DIR)"
	poetry run sphinx-build \
        -W \
        -c "$(DOC_CFG_CONFIG_DIR)" \
        "$(DOC_CFG_SOURCE_DIR)" \
        "$(DOC_CFG_BUILD_DIR)/$@"
