# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import builtins
import matplotlib

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

project = 'struct_post'
copyright = '2025, Chunhao Lyu'
author = 'Chunhao Lyu'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'nbsphinx', #MyST-NB
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'matplotlib.sphinxext.plot_directive',
    'IPython.sphinxext.ipython_console_highlighting'
]


templates_path = ['_templates']
exclude_patterns = []

# autodoc configuration
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
autodoc_inherit_docstrings = True
autoclass_content = 'both'

# MyST markdown enhancements
myst_enable_extensions = [
    "dollarmath",
    "colon_fence",
    "deflist",
    "fieldlist",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "navigation_depth": 4,
    "show_prev_next": False,
    "show_toc_level": 2,
    "collapse_navigation": False,
}
html_static_path = ['_static']

# -- Matplotlib plot directive 配置 -----------------------------------------
plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = [('png', 90)]
plot_include_source = True
plot_rcparams = {
    'savefig.bbox': 'tight',
    'savefig.dpi': 100,
}



if "sphinx" in builtins.__dict__:
    matplotlib.use("Agg")