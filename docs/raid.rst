RAiD - Research Activity Identifier
===================================

What is RAiD?
--------------
The `Research Activity Identifier (RAiD) <https://www.raid.org/what-is-raid>`_ system provides persistent identifiers (PIDs) for research projects and other research activities. It also serves as a global registry of such projects/activities. Unlike local project identifiers used by research institutions, RAiDs enable globally unique and machine-readable identification of research activities across different systems as well as long-term referencing across the entire lifecycle of a project. This supports improved tracking, reporting, linking, and sharing of related metadata, inputs, and outputs of a project.

Who provides the RAiD system?
-----------------------------
The system was developed by the `Australian Research Data Commons (ARDC) <https://ardc.edu.au/>`_, which acts as the Registration Authority for the RAiD system under the international `ISO 23527:2022 <https://www.iso.org/standard/75931.html>`_.
ARDC is responsible for 
  * Developing and maintaining the RAiD infrastructure and registry.
  * Coordinating with global partners to ensure international adoption and interoperability.
  * Managing RAiD registration services for Australia and New Zealand.

In Europe, `SURF <https://www.surf.nl/en>`_, a provider of digital services for research and education in the Netherlands, is working with ARDC to establish a regional RAiD Registration Agency. SURF will offer its RAiD Service within the Netherlands as well as integrate it into the `European Open Science Cloud (EOSC) <https://eosc.eu/>`_ service portfolio, and it invites organizations to express their interest in collaborating with SURF.

→ More information on the `SURF website <https://www.surf.nl/en/themes/open-science/open-research-information/research-activity-identifier-raid>`_

The `Digital Object Identifier (DOI) <https://pid4nfdi-training.readthedocs.io/en/latest/doi.html>`_ Registration Agency `DataCite <https://datacite.org/>`_ and ARDC have established a strategic partnership to deliver RAiD, integrating it into DataCite’s PID ecosystem. This enables RAiDs to be part of the PID Graph, supports scalable and cost-efficient registration, and simplifies integration for organizations already using DataCite services. RAiD Registration Agencies can issue DOIs using DataCite’s infrastructure to submit a core subset of RAiD metadata to DataCite while retaining detailed, project-specific metadata within the RAiD system. 

→ More information can be found on the `DataCite support pages <https://support.datacite.org/docs/raids>`_ and `blog <https://datacite.org/blog/get-started-with-raid-registration-through-the-new-raid-consortium/>`_.

What is the difference between a RAiD and a DataCite DOI?
----------------------------------------------------------
RAiD is a standard specifically designed to uniquely identify research activities, and to collaboratively collect and publicly share information about them. Its metadata schema is tailored to capture the lifecycle of a project, offering a version history to display changes of (for example) a project’s contributors, funding, outputs, or relations to other projects. In contrast, DataCite DOIs cover a broader scope of potential research activities and outputs with more general metadata requirements.

What is the difference between a RAiD and a grant or award PID?
----------------------------------------------------------------
RAiDs and `grant <https://www.crossref.org/documentation/research-nexus/grants/>`_  or `award <https://support.datacite.org/docs/registering-datacite-dois-for-awards#applying-the-datacite-metadata-properties-to-awards>`_ PIDs serve different purposes in the research ecosystem. A RAiD is minted by those leading a project. It uniquely identifies and captures information about the research activities: how has a project evolved and what has actually been achieved during its duration?  A grant or award PID is registered by a funding agency and refers specifically to a financial instrument that supports research; it identifies the grant or award as a contractual or administrative entity rather than the research activity it funds. While a project may be funded by one or more grants or awards, a RAiD tracks the research endeavor as a whole, independent of the source or number of grants. Linking RAiDs to grant/award PIDs enables clear attribution of funding while preserving a comprehensive view of the research activity.

What are the metadata requirements of RAiDs?
--------------------------------------------
RAiD metadata captures a comprehensive, structured description of a research project throughout its lifecycle. At a minimum, RAiD records include the project’s title, description, start and end dates, and status, along with detailed information about contributors, their roles and affiliations, ideally linked to ORCID iDs and ROR IDs. Funding information, such as grant numbers and sponsoring organizations, should be included, as well as links to related inputs and outputs such as publications, datasets, software, or other resources assigned with PIDs. RAiD also captures relationships with other projects, contact and organizational information, and supports versioning and provenance to track updates over time.

→ More information on the metadata requirements is available on the `RAiD Metadata Schema website <https://metadata.raid.org/en/v1.6/>`_.

What does it cost to use RAiD services?
---------------------------------------
Currently, RAiD services are available only through the service portfolios of ARDC and SURF, serving organizations in Australia and New Zealand, and the Netherlands. A cost and governance model for integration with EOSC is still under development.
In the USA, the San Diego Supercomputer Center and Lyrasis have `launched a pilot program for RAiD services <https://lyrasis.org/us-raid-pilot-faqs/>`_.

How to get started?
--------------------
If you are based in Europe and are interested in integrating RAiDs into your infrastructure, you can contact the RAiD team at SURF to receive updates on the `launch of the EOSC RAiD Service <https://www.surf.nl/en/themes/open-science/open-research-information/research-activity-identifier-raid>`_.
The ARDC RAiD service provides a `demo system <https://documentation.ardc.edu.au/raid/give-raid-a-test-drive>`_ for testing RAiD functionality.
As a DataCite member, you can register DataCite DOIs with the `ResourceType “project” <https://datacite-metadata-schema.readthedocs.io/en/4.6/appendices/appendix-1/resourceTypeGeneral/#project>`_ using your client account. Learn more about DataCite membership and DOI registration `in our cookbook <https://pid4nfdi-training.readthedocs.io/en/latest/doi.html#registering-a-doi-with-datacite>`_. 

Additional Resources & FAQs
---------------------------
  * `ARDC RAiD Service <https://ardc.edu.au/services/ardc-identifier-services/raid-research-activity-identifier-service/>`_
  * RAiD service provider `roadmap <https://documentation.raid.org/raid/sign-up-for-a-raid-service>`_
  * RAID as a `Component of EOSC service portfolio <https://faircore4eosc.eu/eosc-core-components/research-activity-identifier-service-raid>`_
  * RAiD as a planned `European PID service <https://www.surf.nl/en/themes/open-science/open-research-information/research-activity-identifier-raid>`_ outside the Netherlands 
  * `DataCite on RAiDs <https://support.datacite.org/docs/raids>`_, including `FAQs <https://support.datacite.org/docs/raid-faq>`_
  * RAiD `API usage <https://documentation.ardc.edu.au/raid/using-the-raid-api>`_



