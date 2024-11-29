ROR - Research Organization Registry
====================================

What is a ROR ID?
---------------------

ROR is an open registry of research organization identifiers. It helps standardize the identification of institutions in scholarly communications, ensuring accurate attribution and easier data sharing. All ROR IDs and metadata are provided under the Creative Commons CC0. The registry data is openly available via a search interface, REST API, and data dump. 

`Research Organization Registry (ROR) | Home <https://ror.org/>`_

Structure
-------------

A ROR ID consists of a unique 9-character string appended to the ROR domain. The preferred form of a ROR identifier is the entire URL: `<https://ror.org/04aj4c181>`_ rather than ror.org/04aj4c181 or 04aj4c181, although the ROR API will recognize all three of these forms as ROR IDs.

Who runs ROR?
-----------------
ROR, the Research Organization Registry, is operated as a collaborative initiative by California Digital Library, Crossref, and DataCite, in conjunction with a broad network of community stakeholders.

How to get / update a ROR?
------------------------------
The process for registering ROR IDs and managing ROR records differs from the workflows used for ORCID iDs and DOIs. Unlike these systems, ROR IDs are created and maintained through a **centralized curation** process guided by the community.

Anyone can propose additions or updates to the registry, regardless of affiliation. You don't need to be connected to an organization to suggest changes to its record in ROR. There are **no fees** or access requirements for using ROR.

`How can I add an organization to ROR? <https://ror.org/about/faqs/#how-can-i-add-an-organization-to-ror>`_

See also here for the form to suggest changes: `<https://curation-request.ror.org/>`_

`More on the curation model and the workflows of updating or registering a ROR ID: 
  * `<https://ror.org/registry/>`_ and
  * `<https://github.com/ror-community/ror-updates/wiki/Curator-Evaluation-Workflow:-New-Records>`_

Why can I not get an ROR ID for my department?
--------------------------------------------------
ROR is designed as a high-level registry of organizations, primarily addressing the core use case of affiliation tracking and providing essential metadata that integrates seamlessly with other institutional identifiers. While ROR does not aim to map departments within institutions, it does include some sub-units like research institutes and laboratories. Its open data and infrastructure are intended to support and integrate with local efforts focused on mapping organizational hierarchies at a more granular level.

Metadata Schema Versions
----------------------------
ROR maintains two versions of its metadata schema. The current recommended version (as of Jan 2025) is `version 2 <https://ror.readme.io/v2/docs/data-structure>`_.

How to find an organization in the registry?
------------------------------------------------
There are three ways to look up organizations and organization records in ROR:

* Web Search ROR at `<https://ror.org/search>`_
* Read the ROR REST API v2 documentation: `<https://ror.readme.io/v2/docs/rest-api>`_
* Download the entire ROR dataset dump in JSON and CSV format at `<https://doi.org/10.5281/zenodo.6347574>`_

If you want to find out more about the different ways to get data out of ROR, see `ROR’s documentation <https://ror.org/registry/#accessing-the-registry>`_.

Interoperability
--------------------
ROR enables seamless integration with other PIDs and their associated provider infrastructure. Several DOI registration agencies, such as Crossref and DataCite, as well as ORCID, have integrated ROR into their services. This collaborative network of services connects research outputs to their creators and affiliations, fostering greater transparency and facilitating the tracking of research provenance.

from the FAQs
-------------
* Is ROR supported in ORCID? `<https://ror.org/about/faqs/#is-ror-supported-in-orcid>`_
* Is ROR supported in DOIs? `<https://ror.org/about/faqs/#is-ror-supported-in-dois>`_
* How do I integrate ROR in my system? `<https://ror.org/about/faqs/#how-do-i-integrate-ror-in-my-system>`_
* How do I implement ROR in my repository or system? `<https://ror.readme.io/docs/forms#implementation-approaches>`_

For more FAQ see: `<https://ror.org/about/faqs/>`_

Roadmap
-------
ROR provides transparent information on planned feature development, modifications of its data model and bug fixing on its roadmap: `<https://github.com/ror-community/ror-roadmap/issues>`_
