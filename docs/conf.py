# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bboxconverter'
author = "Olivier D'Ancona"
copyright = f"{datetime.datetime.now().year}, Olivier D'Ancona"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
autoapi_dirs = ["../src/bboxconverter"]  # location to parse for API reference

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_static_path = ['_static']
html_theme = "sphinx_rtd_theme"
html_logo = "_static/logo_doc.svg"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# -- Options for myst_nb -----------------------------------------------------

jupyter_execute_notebooks = "off"
