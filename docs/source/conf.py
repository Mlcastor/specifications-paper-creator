# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = "Specification Paper Creator"
copyright = "2024, Micastor (CEO of SaaSphere Technologies)"
author = "Micastor (CEO of SaaSphere Technologies)"
version = "1.0"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for Markdown output ---------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# -- Options for autodoc ----------------------------------------------------
autodoc_mock_imports = []
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "inherited-members": True,
    "show-inheritance": True,
}

# -- Options for todo extension ----------------------------------------------
todo_include_todos = True

# -- Options for coverage extension ------------------------------------------
coverage_write_headline = True
coverage_show_missing_items = True
