# -*- coding: utf-8 -*-

# pylint: skip-file

import os
import platform
import sys

### Import project configuration ##############################################
_conf_location = os.path.realpath(os.path.dirname(__file__))
sys.path.append(_conf_location)

import config as configuration

config = configuration.Config()


###############################################################################

### SPHINX CONFIGURATION (GENERAL) ############################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html

# The configuration values shall be placed in the same order as they are placed in the documenting manual.
# The documenting chapter of the manual shall be reflected by a section in this config file.
# The hyperlink to that chapter shall be placed in the very first line of that section.

# Helper variables which are used inside this configuration file which support a calculation of a
# configuration value shall be named so they start with an underscore ("_") so it"s obvious
# that they are local helper variables only used here.
# This is not a function by the interpreter but a common syntax hint to the programmer.

### Project information #######################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project   = config.get("project")
author    = config.get("author")
copyright = config.get("year") + ", " + author


### General configuration #####################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
language = config.get("language")

templates_path = []

exclude_patterns = [
]

## Let's expand `some string` to `some string` instead of *some string*
default_role = "code"

master_doc = "index"

numfig = True


### Options for HTML output ###################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = []

html_extra_path = []

html_show_sourcelink = True

html_theme = "pydata_sphinx_theme"

html_title = project

if "classic" == html_theme: ###################################################
    pass

elif "pydata_sphinx_theme" == html_theme: #####################################
    html_theme_options = {
    "show_toc_level": 2
    }
    pass

else:
    pass


###############################################################################
### EXTENSIONS AND THEIR SETTINGS #############################################
###############################################################################

# Ordered list. Order: Most general first, then for more and more special usescases
extensions = []

### Draw diagrams with "draw.io" ##############################################
# @see https://pypi.org/project/sphinxcontrib-drawio/

extensions.append("sphinxcontrib.drawio")

# Prevent from nasty console flickering
drawio_disable_verbose_electron = True

# Linux-only settings:
if "Linux" == platform.system():

    # Run virtual X-Server.
    drawio_headless = True

    # Make it work in docker containers
    drawio_no_sandbox = True


### Embedd diagrams as code in plantuml language with "plantuml" #############
# @see https://github.com/sphinx-contrib/plantuml
# @see https://crashedmind.github.io/PlantUMLHitchhikersGuide/

extensions.append("sphinxcontrib.plantuml")

_plantuml_config_file="plantuml.config"

plantuml = f"java -jar {_conf_location}/../.tools/plantuml.jar -config {_conf_location}/{_plantuml_config_file}"

plantuml_batch_size = 500

plantuml_output_format = "svg"

plantuml_latex_output_format = "pdf"


### Author diagrams of arbitrary types with "Mermaid" #########################
# @see https://sphinxcontrib-mermaid-demo.readthedocs.io
# @see https://mermaid.js.org/syntax/gitgraph.html

extensions.append("sphinxcontrib.mermaid")

# Set the output format depending on builder:
# Use svg but overwrite it in case we want to build a pdf via latex-builder

mermaid_output_format = "svg"

def setup(app):
    app.connect('builder-inited', _mermaid_on_builder_inited)

def _mermaid_on_builder_inited(app):

    if "latex" == app.builder.name:
        # Override setting(s)
        app.config.mermaid_output_format = "pdf"

# This allows commands other than binary executables to be executed on Windows.
# Does work on Windows, only.
if "Windows" == platform.system():
    mermaid_cmd_shell = "True"

# For individual parameters, a list of parameters can be added. Refer to https://github.com/mermaidjs/mermaid.cli#options.
mermaid_params =  []

# Make it work under Linux as root (in CI in docker container)
# Works on Windows with any user as well.
mermaid_params += ["-p", os.path.join(_conf_location, "puppeteer-config.json")]

# Styling
mermaid_params += [ "--backgroundColor", "transparent"]
mermaid_params += ["--theme", "forest"]
mermaid_params += ["--width", "400" ]

mermaid_d3_zoom = True


### Author diagrams of arbitrary types with "Graphviz" ########################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html
# @see https://graphviz.org/gallery/
# @see https://graphviz.org/docs/attrs/rankdir/

extensions.append("sphinx.ext.graphviz")


### Add copy-to-clipboard button to codeblocks ################################
# @see https://sphinx-copybutton.readthedocs.io

extensions.append("sphinx_copybutton")


### Manage todos with "todo" ##################################################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

extensions.append("sphinx.ext.todo")

todo_include_todos = True


### Add sophistic html elements - use with care ###############################
# @see https://sphinx-design.readthedocs.io

extensions.append("sphinx_design")

tags_create_tags = False


### Enable bibliography in bibtex format ######################################
# @see https://sphinxcontrib-bibtex.readthedocs.io/

extensions.append("sphinxcontrib.bibtex")

bibtex_bibfiles = [
    "references.bib",
]


### EOF #######################################################################
