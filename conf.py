# -*- coding: utf-8 -*-

import os
from datetime import date

# -- General configuration -----------------------------------------------------

extensions = []

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['scipy-sphinx-theme', 'README.rst']

# General information about the project.
project = u'Numpy and Scipy documentation'
copyright = u'%s SciPy developers' % date.today().year
version = ''
release = ''
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

html_theme_path = [os.path.join('scipy-sphinx-theme', '_theme')]

html_theme = 'scipy'
html_theme_options = {
    'rootlinks': [('http://scipy.org/', 'SciPy.org')],
    'sidebar': 'right',
    'navigation_links': False,
    "scipy_org_logo": True,
    "edit_link": False,
}
html_sidebars = {
    'index': ['sitenav.html', 'searchbox.html'],
}

html_title = "Numpy and Scipy documentation"
html_static_path = ['_static']

html_use_modindex = False
html_use_index = False
html_show_sourcelink = False

