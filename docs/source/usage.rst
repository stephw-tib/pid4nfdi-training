DOI - Digital Object Identifier
=====
A **DOI (Digital Object Identifier)** is a type of **Persistent Identifier (PID)** used to uniquely identify and provide a stable link to digital objects, such as academic papers, research datasets, reports, or other online content.
Key features of a DOI include:
 #. **Unique and Persistent:** Each DOI is unique and remains associated with its resource, even if the resource's location (URL) changes.
 #. **Resolvable:** DOIs can be entered into the DOI resolver (e.g., https://doi.org/) to redirect users to the current location of the resource.
 #. **Widely Used:** DOIs are commonly used in scholarly publishing, ensuring reliable citations and access to academic work.
 #. **Format:** A DOI typically follows a format like 10.xxxx/xxxxx, where the prefix identifies the publisher or organization, and the suffix identifies the specific object.
For example, a DOI for a research article may look like https://doi.org/10.1000/xyz123.



.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

