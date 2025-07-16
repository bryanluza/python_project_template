# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "{{ PROJECT_NAME }}"
copyright = "2025, {{ AUTHOR }}"
author = "{{ AUTHOR }}"
release = "{{ VERSION }}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # To automatically generate docs from docstrings
    "sphinx.ext.napoleon",  # If you use Google or NumPy style docstrings
    "sphinx.ext.todo",  # For todo notes in docs
    "sphinx.ext.viewcode",  # To link to source code
    "sphinx_rtd_theme",  # The Read the Docs theme
    "sphinx_autodoc_typehints",  # Better display of type hints
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Napoleon settings (for Google or NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# sphinx_autodoc_typehints settings
typehints_document_rtype = True
typehints_fully_qualified = False  # Use simpler names for types

todo_include_todos = True  # Set to False for production builds
