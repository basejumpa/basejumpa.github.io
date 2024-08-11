# -*- coding: utf-8 -*-

# pylint: skip-file

# Modules built into Sphinx distribution
import re
import os
import platform
import sys
import time

# Modules from additional packages
from git import Repo
from sphinx.util.logging import getLogger

logger = getLogger(__name__)

_conf_location = os.path.realpath(os.path.dirname(__file__))

### Import project configuration ##############################################
# @see https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html

def translate_config_file(input_file=".config", output_file="config.py"):
    CONFIG_PREFIX = r"^CONFIG_"

    # Define the path for the input and output files
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_directory, input_file)
    output_file_path = os.path.join(current_directory, output_file)

    # Check if the output file needs to be created or updated
    if (not os.path.exists(output_file_path) or
        os.path.getmtime(config_file_path) > os.path.getmtime(output_file_path)):

        # Read the input file
        with open(config_file_path, "r") as config_file:
            lines = config_file.readlines()

        # Process the lines
        processed_lines = []
        for line in lines:
            if re.match(CONFIG_PREFIX, line):
                # Remove the CONFIG_PREFIX
                processed_lines.append(re.sub(CONFIG_PREFIX, "", line))
            else:
                processed_lines.append(line)

        # Write to the output file
        with open(output_file_path, "w") as output_file:
            output_file.write("n = False\n")
            output_file.write("y = True\n")
            output_file.writelines(processed_lines)

# Call the function
translate_config_file()

# Import the generated config module
sys.path.append(f"{os.getcwd()}")
import config



### Get SCM information #######################################################

def _calculate_repo_root_dir(source_path):
    if not source_path:
        return '.'

    # Split the path by the forward slash
    subdirectories = source_path.split(os.pathsep)

    # Create the reversed path using ".."
    reversed_path = os.pathsep.join([".."] * len(subdirectories))

    return reversed_path


_scm_git_branch = None
try:
    __repo = Repo(_calculate_repo_root_dir(config.BUILD__DIRS__SOURCE))
    _scm_git_branch = __repo.active_branch.name
except:
    logger.warning(f"Couldn't get git branch.")

### SPHINX CONFIGURATION (GENERAL) ############################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html


### Project information #######################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project   = config.DOC__PROJECT
author    = config.DOC__AUTHOR
gcopyright = ", ".join([str(config.DOC__YEAR), config.DOC__AUTHOR])


### General configuration #####################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
language = config.DOC__LANGUAGE

exclude_patterns = [
]

## Let's expand `some string` to `some string` instead of *some string*
default_role = "code"

master_doc = "index"

numfig = True


### Options for HTML output ###################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = config.DOC__TITLE

html_meta = {
    'description': config.DOC__DESCRIPTION,
    'keywords': 'config.DOC__KEYWORDS',
    'author': config.DOC__AUTHOR,
}

templates_path = ["_templates"]

html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "custom.css",
]

html_extra_path = ["_root"]

html_show_sourcelink = False

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "icon_links": [
        {
            "name": "Paypal",
            "url": "https://www.paypal.com/donate/?hosted_button_id=DDV9AQBFJNMVU", # TODO: Move this to Kconfig
            "icon": "fa-solid fa-coffee"
        },
        {
            "name": "GitHub",
            "url": "https://github.com/basejumpa",  # TODO: Move this to Kconfig
            "icon": "fa-brands fa-github",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/mann-wahrenberg", # TODO: Move this to Kconfig
            "icon": "fa-brands fa-linkedin"
        },
    ],
}

html_sidebars = {
    "*": ["me.html"],
}


# Enable and configure edit page link if branch is known
if _scm_git_branch:
    html_theme_options["use_edit_page_button"] = True
    html_context = {
        "github_user":    "basejumpa",           # TODO: Move this to Kconfig: config.DOC__SCM_OWNER,
        "github_repo":    "basejumpa.github.io", # TODO: Move this to Kconfig: config.DOC__SCM_REPO,
        "github_version": _scm_git_branch,
        "doc_path":       config.BUILD__DIRS__SOURCE,
    }

###############################################################################
### EXTENSIONS AND THEIR SETTINGS #############################################
###############################################################################

# Ordered list. Order: Most general first, then for more and more special usescases
extensions = []


### Create sitemap.xml for search engines ####################################
# @see https://sphinx-sitemap.readthedocs.io

extensions.append("sphinx_sitemap")

html_baseurl = config.PUBLISH__BASEURL


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

# For individual parameters, a list of parameters can be added.
# Refer to https://github.com/mermaidjs/mermaid.cli#options.
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


### Enable blogging ###########################################################
# @see https://ablog.readthedocs.io/en/stable/

extensions.append("ablog")

post_date_format = "%Y-%m-%d"
post_date_format_short = post_date_format

blog_authors = {
#    config.DOC__AUTHOR__NICKNAME: (config.DOC__AUTHOR, config.DOC__AUTHOR__URL),
    "basejumpa": ("Alexander Mann-Wahrenberg", 'https://github.com/basejumpa'), # TODO: Move this to Kconfig
}
blog_default_author = "basejumpa" # TODO: Move this to Kconfig: config.DOC__AUTHOR__NICKNAME

html_sidebars["blog/**"] = [
    "ablog/postcard.html",
    "ablog/recentposts.html",
    "ablog/tagcloud.html",
]


### Enable embedding of Videos ################################################
# @see https://sphinxcontrib-youtube.readthedocs.io

extensions.append("sphinxcontrib.youtube")


### EOF #######################################################################
