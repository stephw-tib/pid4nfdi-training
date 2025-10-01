PID for Instruments
===================

What is a PID for Instruments?
------------------------------
A **Persistent Identifier (PID) for Instruments** is a globally unique and enduring reference assigned to scientific instruments, such as sensors, microscopes, or telescopes. It is used for the identification of individual physical devices, not to categorize model types in general. These PIDs ensure that instruments are unambiguously identifiable across various platforms and over time, facilitating data provenance, reproducibility, and proper attribution in research.

The **Persistent Identification of Instruments Working Group (PIDINST)**, under the Research Data Alliance (RDA), has developed a standardized `metadata schema <https://docs.pidinst.org/en/latest/white-paper/metadata-schema.html>`_ to support the assignment of PIDs to instruments. This schema has so far been implemented with the PID providers DataCite and ePIC, enabling the integration of instrument identification into existing research infrastructures.

What is the main purpose of the PID service?
--------------------------------------------
The primary purposes of assigning PIDs to instruments include:

* **Unambiguous Identification:** Ensuring each instrument can be uniquely referenced, preventing confusion between similar instruments.
* **Data Provenance:** Linking datasets to the specific instruments that generated them, enhancing transparency and reproducibility.
* **Attribution and Citation:** Allowing instruments to be cited in publications, acknowledging their role in data generation.
* **Lifecycle Management:** Tracking the history, usage, and maintenance of instruments over time.
* **Interoperability:** Facilitating integration and data sharing across different research infrastructures and disciplines.
* **Findability:** Increasing discoverability of instruments.
* **Equality:** Promoting equal research opportunities by improving access to instruments for all institutions, regardless of their resources.
* **Tracking Errors:** Potentially finding systematic errors induced by a specific instrument.
* **Funding:** Supporting stakeholders in their funding decisions.

What are the prerequisites to use the service?
----------------------------------------------
To assign PIDs to instruments, consider the following prerequisites:

* **Affiliation with a PID Provider:** Collaborate with organizations like DataCite or ePIC that offer PID services for instruments directly or work with one of their members.
* **Metadata Preparation:** Collect detailed metadata about the instrument, adhering to the `PIDINST metadata schema <https://docs.pidinst.org/en/latest/white-paper/metadata-schema.html>`_, which includes information such as the instrument's name, type, owner, and associated datasets.
* **Technical Integration:** Ensure your systems can interact with the PID provider's APIs or platforms for PID registration and management.

How to get started?
-------------------
Here’s a step-by-step guide to assigning PIDs to instruments:

1.	**Learn About PIDINST:** Familiarize yourself with the PIDINST Working Group's efforts and the importance of instrument identification by visiting their `official documentation <https://docs.pidinst.org/>`_.
2.	**Select a PID Provider:** Choose a PID provider that supports instrument identification, namely DataCite or ePIC.
3.	**Review the Metadata Schema:** Examine the `PIDINST metadata schema <https://docs.pidinst.org/en/latest/white-paper/metadata-schema.html>`_ to understand the required and recommended metadata fields for instrument identification.
4.	**Prepare Instrument Metadata:** Gather comprehensive information about your instrument, ensuring it aligns with the metadata schema.
5.	**Register with a PID Provider:** Contact your chosen PID provider to set up an account or establish a collaboration for PID assignment.
6.	**Assign the PID:** Use the provider’s platform or API to register the instrument, submit the metadata, and obtain a PID.
7.	**Integrate and Use the PID:** Incorporate the PID into your data management systems, publications, and workflows to ensure consistent referencing.

For detailed instructions, refer to the `DataCite Cookbook <https://docs.pidinst.org/en/latest/datacite-cookbook/index.html>`_, `the ePIC Cookbook <https://docs.pidinst.org/en/latest/epic-cookbook/index.html>`_ or the `B2INST User Guide <https://docs.eudat.eu/b2inst/forusers/>`_.

How do I Search for PIDs for instruments?
-----------------------------------------
Unlike PID registration, the PID provider’s search platforms can be accessed without being affiliated with DataCite or ePIC. Instrument PIDs registered with DataCite are discoverable via the `DataCite REST API <https://support.datacite.org/docs/api>`_ (filter: ``"resource-type-id": "Instrument"``), or through the `DataCite GraphQL API <https://support.datacite.org/docs/datacite-graphql-api-guide>`_ (``resourceTypeId: "Instrument"``). Based on these APIs, `DataCite Commons <https://commons.datacite.org/doi.org?query=types.resourceTypeGeneral%3AInstrument>`_ also offers an easy-to-use browser-based search interface (``types.resourceTypeGeneral:Instrument``). For instrument PIDs and associated metadata registered via ePIC, B2INST provides a `web-based user interface <https://b2inst-test.gwdg.de>`_. Here, all metadata fields belonging to the instruments are searchable. Alternatively, the `EUDAT B2INST HTTP REST API <https://docs.eudat.eu/b2inst/httpapi/>`_ can be used for this purpose.

In addition, the federated search tool `search.pidinst.org <https://search.pidinst.org>`_ has been developed by PID4NFDI. It allows you to query the key metadata fields of the PIDINST schema for all instruments registered with B2INST or DataCite. You can export the result lists as JSON- or CSV-files. The tool also allows you to generate statistics in the form of line graphs and frequency tables for the found instruments. The `search.pidinst.org/all <https://search.pidinst.org/all>`_ route skips the search and directly displays these statistics for all instruments that have a PID.

Implementation of the PIDINST Metadata Schema and Interoperability
------------------------------------------------------------------
For ePIC, the PIDINST metadata schema has been adopted without modification. However, B2INST has provided the opportunity for community-specific customization of the metadata schema. When registering PIDs via B2INST, users are required to assign themselves to one of currently eleven scientific `communities <https://b2inst-test.gwdg.de/communities>`_. In this context, they can see whether the metadata schema has been adapted to meet domain-specific needs.

With the new relation types `"IsCollectedBy" <https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscollectedby>`_ and `"Collects" <https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#collects>`_, DataCite made adjustments to allow interlinking instruments with datasets. However, as the DataCite Metadata Schema contains thirty different resource types, it has to maintain a certain degree of generality. Because of this, the `mapping of the PIDINST metadata schema to the DataCite metadata schema <https://datacite-metadata-schema.readthedocs.io/en/4.5/mappings/pidinst/>`_ is not complete. The PIDINST Working Group thus gives further `advice <https://docs.pidinst.org/en/latest/datacite-cookbook/metadata.html>`_ on how to represent their metadata schema best within DataCite’s schema. This includes recommendations on (sometimes mandatory) DataCite properties where it is hard to see how they apply to instruments.

In addition to the implementation with well-known PID providers, whose platforms are widely used, and for which mappings to other metadata schemas exist, interoperability is promoted by the PIDINST Working Group’s `recommendation <https://docs.pidinst.org/en/latest/white-paper/metadata-schema-recommendations.html#using-common-terminologies>`_ to use established, common terminologies within the PIDINST metadata schema. Standardized terms and classifications improve the consistency and understandability of metadata across different platforms. However, it should also be noted that there is currently no general ontology for key metadata fields such as instrument type or measured variables that extends beyond individual subdomains.

Do any FAQs exist?
-------------------
Yes, the PIDINST Working Group provides comprehensive documentation and resources, including FAQs, to assist with the implementation of PIDs for instruments. Visit their `official documentation <https://docs.pidinst.org/>`_ for more information.

What costs are charged for use?
-------------------------------
The costs associated with assigning PIDs to instruments vary depending on the chosen PID provider and the scope of services required. Some providers may offer free services for academic or non-profit institutions, while others might charge fees for registration, metadata management, or API access. It is advisable to contact the PID provider directly to obtain detailed information about any potential costs.

-----------------

Creators: Torsten Kahlert (https://orcid.org/0009-0003-3264-5006), Frederik Springer (https://orcid.org/0000-0001-5379-0059) 

Reviewer: Markus Stocker (https://orcid.org/0000-0001-5492-3212)
