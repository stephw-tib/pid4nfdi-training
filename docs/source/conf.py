# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PID4NFDI Cookbook'
copyright = '2025, PID4NFDI'
author = 'PID4NFDI'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_last_updated_by_git',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_templates']
html_last_updated_fmt = '%b %d, %Y'

# -- Options for EPUB output

epub_show_urls = 'footnote'

# Force Sphinx to include the imprint page without it appearing in toctree
from sphinx.application import Sphinx

def setup(app: Sphinx):
    app.add_config_value('extra_docs', [], 'env')

extra_docs = ['imprint']
