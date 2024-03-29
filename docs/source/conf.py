#import sphinx_minoo_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IFDA'
copyright = '2024, Abdulrahman'
author = 'Abdulrahman'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ar'

html_theme_options = {
    'logo_only': True
}


html_logo = 'images\IFDA-logo.png'

html_show_sourcelink = False

html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'style_nav_header_background': 'white',

}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

#html_theme_path = [sphinx_minoo_theme.get_html_theme_path()]

html_static_path = ['_static']

html_css_files = ['css/custom.css']




