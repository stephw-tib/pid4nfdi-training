IGSN - International Generic Sample Number
==========================================

What is a IGSN?
---------------

An IGSN ID is a globally unique and persistent identifier for material samples. The core purpose of the IGSN ID is to enable transparent and traceable connections between research activities and objects, including samples, collections, instruments, grants, data, publications, people, and organizations.

An IGSN ID can be applied to an individual material sample (including to a destroyed or discarded sample), an aggregation of samples, or to a sample collection site. An IGSN ID cannot be used for an image of a material sample, analytical data about the sample, or instruments used for sample measurements.

Although the IGSN ID originates from the Geosciences, IGSN IDs can be applied to all material samples and features-of-interest from any discipline.

How is an IGSN ID structured?
-----------------------------

Functionally, an IGSN ID is a Digital Object Identifier (Digital Object Identifier). As a result, an IGSN ID shares the same format as a DOI: an IGSN ID name is composed of a prefix beginning with 10. and a suffix, separated by a forward slash; for example, `<https://doi.org/10.60510/icdp5054ehw1001>`_. The prefix ensures that the IGSN ID is globally unique. The suffix can be customized to capture any local identifiers already assigned to the material sample.

Who governs the IGSN ID?
--------------

In 2021, `DataCite <https://datacite.org/>`_ and the `IGSN Organization (IGSN e.V.) <https://ev.igsn.org/>`_ `announced a partnership <https://doi.org/10.5438/7z70-1155>`_ to support the global adoption, implementation, and use of material sample identifiers. Within the partnership:
* DataCite provides the IGSN ID registration services and supports their ongoing sustainability.
* IGSN e.V implements and promotes standard methods for identifying, citing, and locating material samples by fostering `disciplinary Communities of Practice (CoPs) <https://ev.igsn.org/communities>`_.

How do I register/update an IGSN ID?
----------------------------

Through the partnership with IGSN e.V., DataCite services to register IGSN IDs for material samples are open to DataCite Members and Consortium Organizations. Because IGSN IDs are functionally DOIs, the same DataCite systems and APIs used for generating and modifying DOIs are also used for IGSN IDs. See above for more details.

IGSN IDs are distinguished from DOIs for other physical objects at the DataCite Repository account and prefix level. To enable this, DataCite has created the IGSN ID Catalog Repository type within its Fabrica service. IGSN IDs must be registered only in an IGSN ID Catalog Repository, and an IGSN ID Catalog Repository must be only used for registering IGSN IDs.

What Metadata Schema is used for IGSN IDs?
------------------------------------------

Again, due to IGSN IDs being functionally DOIs, they are registered with metadata structured according to the DataCite Metadata Schema. The DataCite Metadata Schema thus forms a shared set of common, core IGSN ID metadata properties for all material samples in a standardized format (e.g., author, collection date, geolocation). The IGSN–DataCite partnership has worked together to create a crosswalk recommendation for encapsulating material sample metadata within the DataCite Metadata Schema. It has furthermore developed best practices for enriching IGSN ID metadata.
Important points to note, include:

* IGSN IDs are registered with the resourceTypeGeneral property set to ‘PhysicalObject’. resourceType should at a minimum capture whether the research output being registered is a ‘material sample’ or a ‘feature-of-interest’.
* relatedIdentifier metadata is used to create links between parent and child samples identified by IGSN IDs, and between a material sample and associated citations in resources identified by PIDs. It is also used to point to any institutional/community/domain metadata schema on the web that is being used to richly describe a sample.

The partnership strives to better support material samples within DataCite services, and the IGSN ID crosswalk recommendation and metadata best practices will be augmented and updated as the partnership continues to work closely with disciplinary samples communities globally.

How do I search for an IGSN ID?
-------------------------------

IGSN IDs created in DataCite services are of relatedIdentifierType ‘DOI’. Hence, Findable IGSN IDs appear in search queries through `DataCite Commons <https://commons.datacite.org/>`_, DataCite APIs, and other discovery services. They are also represented in the `PID Graph <https://support.datacite.org/docs/datacite-graphql-api-guide>`_. To limit a search to IGSN IDs only, one must take advantage of the IGSN ID Catalog Repository type. For example, the following search query displays all findable IGSN IDs within `DataCite Commons <https://commons.datacite.org/doi.org?query=client.client_type%3AigsnCatalog+types.resourceTypeGeneral%3APhysicalObject>`_. This query string is not intuitively obvious, and DataCite will soon release a feature in DataCite Commons to facilitate querying and reporting on IGSN IDs.

Interoperability
----------------

IGSN IDs provide a common standard for identifying and describing samples, enabling different systems and platforms to recognize and understand their associated metadata, and making it easier to integrate metadata and samples across different systems. In particular, interoperability is enhanced due to IGSN IDs being encoded in the DataCite Metadata Schema:

* There are 30 resourceTypes supported within the DataCite Metadata Schema—the DataCite Metadata Schema is well-known by the research community and a number of mappings from other schemata to the DataCite Metadata Schema have been developed by the community.
* DOIs/IGSN IDs can be explored and exported in several different formats within DataCite services.
* Domain/community vocabularies and classifications can be included into DataCite Metadata Schema properties.

What support documentation is available for IGSN IDs?
-----------------------------------------------------

In addition to the `IGSN e.V. website <https://www.igsn.org/>`_, DataCite has drafted specific IGSN ID documentation on its `Support site: <https://support.datacite.org/docs/about-igsn-ids-for-material-samples>`_. 

  
Who do I contact to find out more about IGSN IDs?
-------------------------------------------------

Please send all questions concerning DataCite membership and IGSN ID registration to: support@datacite.org. If you wish to join the IGSN e.V. or learn about its disciplinary CoPs, then please email: info@igsn.org. 

