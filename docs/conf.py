#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# packit_app documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
import packit_app
from packit_app import __version__

sys.path.insert(0, os.path.abspath('..'))

# -- Project configuration ---------------------------------------------

project = u'packit-app'
copyright = u"2018-2019, Arne Wohletz"
author = u"Arne Wohletz"
version = packit_app.__version__
release = packit_app.__version__

# -- General configuration ---------------------------------------------

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext'
}

source_encoding = 'utf-8-sig'
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
default_role = 'py:obj'
pygments_style = 'sphinx'
add_module_names = True


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': False,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_build/_static']
html_last_updated_fmt = '%Y %b %d'
html_show_sourcelink = True
html_show_copyright = True
html_show_sphinx = True

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'packit_appdoc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'packit_app.tex',
     u'packit-app Documentation',
     u'Arne Wohletz', 'manual'),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'packit_app',
     u'packit-app Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'packit_app',
     u'packit-app Documentation',
     author,
     'packit_app',
     'One line description of project.',
     'Miscellaneous'),
]


# -- Extensions configuration ------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
