# -*- coding: utf-8 -*-

import os
import re
import pkg_resources
from datetime import date

# -- General configuration -----------------------------------------------------

extensions = []

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['scipy-sphinx-theme', 'README.rst', '.pixi/*']

# General information about the project.
project = u'Numpy and Scipy documentation'
copyright = u'%s SciPy developers' % date.today().year
version = ''
release = ''
pygments_style = 'sphinx'

# -- Parse index.rst for _static/versionwarnings.js ----------------------------

with open('index.rst', 'r') as f:
    index_text = f.read()

scipy_versions = set(re.findall('scipy-([0-9.]{3,})', index_text))
scipy_latest_version = str(max(pkg_resources.parse_version(x) for x in scipy_versions if not x.startswith('0.')))
numpy_latest_version = '&gt; 1.17'

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

html_context = {
    'SCIPY_LATEST_VERSION': scipy_latest_version,
    'NUMPY_LATEST_VERSION': numpy_latest_version,
}

html_title = "Numpy and Scipy documentation"
html_static_path = ['_static']

html_use_modindex = False
html_use_index = False
html_show_sourcelink = False

