# import os
# import sys

# sys.path.insert(0, os.path.abspath('.'))

project = 'mole'
copyright = '2024, CSRC'
author = 'CSRC'
release = '1.0.0'

extensions = [
    'breathe',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# Breathe configuration
breathe_projects = {
    "MoleCpp": "../../api_docs/cpp/xml" 
    # "MoleMatlab": "../../api_docs/matlab",  
}
breathe_default_project = "MoleCpp"

html_static_path = ['_static']
html_output_dir = '../sphinx/build'