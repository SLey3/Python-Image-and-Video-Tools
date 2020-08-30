# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Python Image and Video Tools'
copyright = '2020, Sergio Ley Languren'
author = 'Sergio Ley Languren'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_rtd_theme
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.doctest',
    'sphinx_rtd_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'canonical_url': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_link': False,
    'navigation_depth': 2,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'include_hidden': False,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Doctest configuration -------------------------------------------------

# If this is a nonempty string (the default is 'default'), 
# standard reST doctest blocks will be tested too. They will be assigned to the group name given.
# reST doctest blocks are simply doctests put into a paragraph of their own
# (Note that no special :: is used to introduce a doctest block; 
#  docutils recognizes them from the leading >>>. 
#  Also, no additional indentation is used, though it doesn’t hurt.)
doctest_test_doctest_blocks = 'default'

# -- todo configuration -------------------------------------------------

#  todo and todolist produce output.
todo_include_todos = True