# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile examples

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

tutorial: 
	tools/nb_to_doc.py examples/tutorial

examples:
	tools/nb_to_doc.py examples/example_05_08_01 examples/example_05_08_02 examples/example_05_09_01 examples/example_05_09_02 examples/example_05_09_04 examples/example_05_09_05 examples/example_05_09_06 examples/example_05_09_09
