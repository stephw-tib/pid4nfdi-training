PID4NFDI Cookbook: Getting started with PIDs
===================================

This is a **cookbook** to support you in getting started with PID registration and usage. 
It offers practical guidance on first steps for individuals and organiziations looking to implement PIDs in their workflows. It provides an introduction to what PIDs are, their importance in ensuring long-term access and citation of digital resources, and how they help in maintaining research data, publications, and other digital assets. 

The cookbook is an initiative of the `PID4NFDI project <https://pid.services.base4nfdi.de/>`_ to set up a basic service for Persistent Identifiers (PID) for the member consortia of the German `National Research Data Infrastructure (NFDI) <https://www.nfdi.de/?lang=en>`_ - a joint project of research and infrastructure institutions to optimise research data management within the German research landscape.

.. note::

   This cookbook is work in progress and will continuously grow. 

What is a PID?
---------------

A PID (Persistent Identifier) is a long-lasting reference that provides unique identification of research resources, persons, institutions, projects, devices and many more. Unlike regular URLs, 
which can break or change, PIDs are designed to be stable over time, 
ensuring consistent access to the associated content.

What are the Benefits of PIDs?
-----------------------------
Persistent Identifiers play a crucial role in managing the entire lifecycle of research data and associated entities. By providing a unique and stable reference, PIDs enable the creation of richer, more accurate, and standardized metadata to describe these entities. This enhanced metadata significantly improves the discoverability of research resources, making it easier for researchers to locate relevant data. Additionally, PIDs facilitate interoperability by ensuring that metadata conforms to standardized formats, enabling seamless integration and sharing across different systems and platforms.

PIDs also streamline administrative processes. They minimize the effort required for tasks such as data ingestion, updating, and curation by supporting automated data exchange. This reduces the risk of errors that can occur with manual input, enhancing both efficiency and reliability.

Furthermore, PIDs serve as connectors between various research resources, creating a web of relationships that provide essential context. For example, PIDs can link datasets to their provenance, such as the projects or experiments that generated them, their creators, associated publications, and even derived works. These connections enrich the metadata ecosystem, providing researchers and other stakeholders with a comprehensive understanding of the data's origin, usage, and significance.

By integrating PIDs into research workflows, organizations not only enhance the usability and reliability of research data but also contribute to a more robust and interconnected research infrastructure. This, in turn, accelerates scientific discovery and collaboration by enabling more efficient access to and reuse of research outputs.


**FAIR and Open Science - Related to PIDs?**

PIDs play a crucial role in supporting the `FAIR principles <https://doi.org/10.1038/sdata.2016.18>`_, which aim to ensure that digital resources are Findable, Accessible, Interoperable, and Reusable. Here's how PIDs align with each of the FAIR principles:

  **1. Findable:**
   PIDs help make resources easily findable by providing a unique, permanent identifier (e.g., DOI, ORCID, ARK) that can be indexed and searched in databases, repositories, and catalogs. The metadata associated with PIDs also makes it easier for users to locate resources.
  **2. Accessible:**
   PIDs ensure persistent access to digital objects, even if their location changes (e.g., through DOI resolution services). By linking to the current location of the resource, PIDs ensure that the resource remains accessible over time.
  **3. Interoperable:**
   PIDs, combined with well-structured metadata, support interoperability by allowing different systems, repositories, and platforms to understand and exchange information about the resource in a standardized way. PIDs often include metadata formats that adhere to common standards, making them usable across various systems.
  **4. Reusable:**
   PIDs ensure that resources can be reliably cited, tracked, and referenced in academic and research contexts. They support reuse by making sure the resource is consistently identified over time, regardless of where or how it is stored. Metadata linked to PIDs also often includes licensing and versioning information, which clarifies how the resource can be reused.


Contents
--------

.. toctree::
   choose
   ark
   doi
   epic
   factgrid
   igsn
   orcid
   pida
   ror
   wikidata
