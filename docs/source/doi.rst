DOI - Digital Object Identifier
=====
What is a DOI?
---------------

A **DOI (Digital Object Identifier)** is a type of PID used to uniquely identify and provide a stable link to digital objects, such as academic papers, research datasets, reports, or other online content.


Key features of a DOI include:
 * **Unique:** Each DOI is unique and remains associated with its resource, even if the resource's location (URL) changes.
 * **Persistent:** DOIs are managed in a distributed environment with shared responsibilities, guaranteeing their persistence on a technical and organizational level.
 * **Resolvable:** DOIs can be entered into the DOI resolver (e.g., https://doi.org/) to redirect users to the current location of the resource.
 * **Widely Used:** DOIs are commonly used in scholarly publishing, ensuring reliable citations and access to academic work.
 * **Format:** A DOI typically follows a format like 10.xxxx/xxxxx, where the prefix identifies the publisher or organization, and the suffix identifies the specific object.
For example, a DOI for a research article may look like:

.. code-block:: console

    https://doi.org/10.1000/xyz123

Learn more about DOI with the `DOI Handbook <https://www.doi.org/the-identifier/resources/handbook/>`_.


**How can I get a DOI for my publication?**


DOIs are usually not provided to researchers directly. DOIs for research resources such as publications, datasets, software and other entities will be e.g. registered by a repository provider such as your university library repository, a generic or discipline-specific data repository or the journal you are publishing with.


Responsibilities
-----------------

The management of DOIs works in an environment of distributed responsibilities to enable actual persistence:

1. The `DOI foundation <https://www.doi.org/the-foundation/about-us/>`_ is a non-profit organization and the authority overseeing the DOI system under the ISO standard ISO 26324. The DOI foundation is governed collaboratively by the DOI regstration agencies.

2. DOI registration is managed by `DOI registration agencies (RA) <https://www.doi.org/the-community/what-are-registration-agencies/ >`_ which provide the technical infrastructure to mint DOIs. The registration agencies are representing `different communities <https://www.doi.org/the-community/existing-registration-agencies/>`_ , the most prominent agencies are DataCite and Crossref within the scientific landscape. 

3. A Registrant - e.g. a repository of a research organization - actually registers DOIs and is responsible for creating, updating and maintaing a DOI and its metadata providing the landing page and repository URL the DOI is resolving to. 

Registering a DOI with DataCite
----------------

Registering DOIs with DataCite requires an institutional membership with DataCite - either as a direct member or in a consortium. `Membership and service fees <https://datacite.org/fee-model/>`_ are charged for the service, depending on the `type of membership <https://datacite.org/become-a-member/>`_.

In Germany, there are five consortia working as intermediaries between DataCite and registering organizations, focussing on different subject fields:

  * `TIB DOI Consortium <https://projects.tib.eu/pid-service/en/tib-doi-konsortium/become-a-member/>`_ for the sciences and technology
  * `da|ra <https://www.da-ra.de/>`_ for social and economic data
  * `ZB Med DOI service <https://www.publisso.de/en/working-for-you/doi-service>`_ for the life sciences
  * `SUB Göttingen DOI Registration Service <https://www.eresearch.uni-goettingen.de/knowledge-base/howto/getting-an-identifier/>`_ for the humanities
  * `DOI Consortium <https://service-wiki.hbz-nrw.de/display/DOI/FAQ+zum+DOI-Konsortium>`_ of Hochschulbibliothekszentrum (hbz) Nordrhein-Westfalen, a service for the libraries of universities in Northrhine-Westphalia.

The `DataCite support <https://support.datacite.org/>`_ offers a rich documentation on using the services and `getting started <https://support.datacite.org/docs/getting-started>`_

DataCite offers several ways to mint DOIs and `test accounts <https://support.datacite.org/docs/testing-guide>`_  to get started:

  * via `REST API <https://support.datacite.org/docs/api>`_
  * via its user interface `Fabrica <https://support.datacite.org/docs/doi-fabrica>`_

The TIB DOI consortium services provides a `German translation <https://wiki.tib.eu/confluence/display/pid/DataCite+Fabrica+Handbuch+Startseite>`_  of DataCite's Fabrica guide, including a growing collection of `FAQs <https://wiki.tib.eu/confluence/display/pid/FAQs>`_  on DOI registration. 

DataCite supports the registration of DOIs for a wide range of resource types. The documentation of the `DataCite Metadata Schema <https://schema.datacite.org/>`_ provides an overview of `resource types <https://datacite-metadata-schema.readthedocs.io/en/4.5/properties/resourcetype/>`_ and how to register them.

You can use `DataCite Suggestions on GitHub <https://github.com/datacite/datacite-suggestions>`_ to communicate further requirements for DOI registration that are not already covered by the service.


In the following, you can find information to start registration with the most common registration agencies Crossref and DataCite. Both of these PID providers collaborate with each other and with other providers such as ROR and ORCID.

Registering a DOI with Crossref
-------------------
Minting a DOI with Crossref also requires `membership <https://www.crossref.org/membership/>`_ including `service and a membership fees <https://www.crossref.org/fees/>`_ based on content registration and type and revenue of your organization.

The content to be registered must be scholarly in nature - e.g. journal articles, books, conference proceedings, datasets - and must be provided via a landing page URL the DOI resolves to.

Crossref offers several ways to deposit metadata and mint a DOI:

With Helper Tools:
  * `Web deposit form for publications <https://www.crossref.org/documentation/register-maintain-records/web-deposit-form/>`_
  * `Record registration form for grants <https://www.crossref.org/documentation/register-maintain-records/record-registration-form/>`_
  * `Plugin for Open Journal Systems (OJS) <https://www.crossref.org/documentation/register-maintain-records/ojs-plugin/>`_

Direct registration of metadata XML:
  * `Upload JATS XML with web deposit form <https://www.crossref.org/documentation/register-maintain-records/direct-deposit-xml/jats-xml/>`_
  * `Upload XML with admin tool <https://www.crossref.org/documentation/register-maintain-records/direct-deposit-xml/admin-tool/>`_
  * `XML deposit using HTTPS POST <https://www.crossref.org/documentation/register-maintain-records/direct-deposit-xml/https-post/>`_

The Crossref Documentation provides further `guidance <https://www.crossref.org/documentation/register-maintain-records/choose-content-registration-method/>`_ on choosing the appropriate method for your registration workflow.

----

Creators: Torsten Kahlert (https://orcid.org/0009-0003-3264-5006), Stephanie Hagemann-Wilholt (https://orcid.org/0000-0002-0474-2410)
