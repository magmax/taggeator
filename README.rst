Description
===========

From a file with a tag description format like:

.. include:: categories.yaml

Generates a new file after applying a template with the inverted file, that is,
a dict of tags with each app as a dict.

As an example, with the template:

.. include:: categories.jinja

The previous input file will generate:

.. include:: categories.html
