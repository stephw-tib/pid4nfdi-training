EUPID - European Patient Identity Services
==========================================

What are the EUPID Services?
-----------------------------

The EUPID Services are a privacy-preserving record linking service designed for managing pseudonymous patient identities in clinical and research settings. It provides a secure way to manage patient identities across different contexts while ensuring data privacy and interoperability.

The development started during the EU-funded ENCCA project [#encca]_ by the Austrian Institute of Technology (AIT) who is currently further developing, maintaining, operating and distributing the system.


What is the main purpose of the EUPID Service?
-----------------------------------------------

The primary goal of the EUPID Services is to enable the secure linkage of patient records across various data sources without compromising patient privacy. This is achieved through the generation of context-specific pseudonyms that are linked to a unique internal virtual patient identifier. Contexts that use the same patient identity data for registering patients in the EUPID Services receive individually different pseudonyms but are linked to the same virtual patient.

The EUPID Services help to connect patient data from multiple registries or healthcare settings in a privacy-preserving manner. They facilitate data linkage across diverse systems and studies involving the same individual, primarily in the context of health and biomedical research. They support secondary use of pseudonymised data in areas such as clinical trials, biobanking, and rare disease registries without compromising privacy.

GDPR compliance of the EUPID Services has been confirmed by an accredited certification body under article 43 of the GDPR [#gdpr]_.

The EUPID Services are used in various projects and research infrastructures related to rare diseases, including several SIOPEN studies and the SIOPEN BIOPORTAL [#bioportal]_, MONALISA [#monalisa]_, the European Reference Network for Paediatric Oncology [#ern]_, PanCareSurPass [#pancare]_, PRIMAGE [#primage]_, EJP-RD [#ejprd]_, or ERDERA [#erdera]_. Additionally, they are used in Austrian research infrastructures for heart failure and data donation.


What are the prerequisites to use the EUPID Service (e.g., registering Persistent Identifiers (PIDs))?
-------------------------------------------------------------------------------------------------------

To use the EUPID Services, providers of data management services (e.g., providers of trial databases, etc.) must integrate the service into their existing systems using an REST API. This involves client-side scripts (e.g., JavaScript, Python) to hash / encrypt identity data, authenticate to and calling the EUPID Services API and handling the respective API response. Specific prerequisites may include:

* Technical capability to integrate with the EUPID Services API.
* Compliance with data protection laws and regulations.


How to get started?
--------------------

To get started with the EUPID Services, contact the AIT Austrian Institute of Technology GmbH at contact@eupid.eu to organize a meeting to discuss the setup needed for your specific use case. After the initial meeting, you will get access to the developer and API documentation and initiate the process to set up a test application with a EUPID Services test instance.


Where do I find general information?
--------------------------------------

General information about the EUPID Services can be found on the EUPID Services website: https://services.eupid.eu/. The website provides an overview of the service, its features, and how it can be used to manage patient identities securely. A video describing what the EUPID Services are and how they work is provided on the website as well.


Related research articles and case studies
-------------------------------------------

* Hayn D, Sandner E, Baumgartner M, Jammerbund B, Wiesmüller F, Beyer S, Vinatzer H, Rzepka A, Donsa K, Kreiner K and Schreier G (2026) EUPID—configurable privacy-preserving record linkage in federated health data spaces. *Front. Digit. Health* 8:1751234. doi: 10.3389/fdgth.2026.1751234

* Hayn, D., Kreiner, K., Sandner, E., Baumgartner, M., Jammerbund, B., Falgenhauer, M., Düster, V., Devi-Marulkar, P., Schleiermacher, G., Ladenstein, R., & Schreier, G. (2024). Use Cases Requiring Privacy-Preserving Record Linkage in Paediatric Oncology. *Cancers*, 16(15), 2696. https://doi.org/10.3390/cancers16152696

* Demelius, L., Kreiner, K., Hayn, D., Nitzlnader, M., & Schreier, G. (2020). Encoding of Numerical Data for Privacy-Preserving Record Linkage. in L. Demelius, K. Kreiner, D. Hayn, M. Nitzlnader, & G. Schreier (Hrsg.), dHealth 2020 - Biomedical Informatics for Health and Care (S. 23-30). IOS Press. https://doi.org/10.3233/SHTI200070

* Wiesmüller, Fabian, Dieter Hayn, Karl Kreiner, und Günter Schreier. „Use of QR Codes in a Mobile App to Support Privacy-Preserving Record Linkage Via the EUPID Services". 67. Jahrestagung Der Deutschen Gesellschaft Für Medizinische Informatik, Biometrie Und Epidemiologie e. V. (GMDS), 13. Jahreskongress Der Technologie- Und Methodenplattform Für Die Vernetzte Medizinische Forschung e.V. (TMF), 2022. https://doi.org/10.3205/22GMDS033

* Hayn, D., Sandner, E., Jammerbund, B., Okuyan, E. S., Koster, J., Wittens, M. M. J., Tytgat, G. A. M., Taschner-Mandl, S., & Schleiermacher, G. (2025). MONALISA: A Privacy-Preserving Infrastructure Supporting Liquid Biopsies to Monitor Relapsed Neuroblastoma. *Studies in health technology and informatics*, 327, 773–774. https://doi.org/10.3233/SHTI250462

* Hayn, D., Sandner, E., Jammerbund, B., Zalatnai, L., Papakonstantinou, A., Beltran, S., Piscia, D., Devi-Marulkar, P., Schleiermacher, G., Kreiner, K., & Schreier, G. (2024). *Privacy-Preserving Record Linkage between the SIOPEN BIOPORTAL and the RD-Connect Genome Phenome Analysis Platform via the EUPID Services*. Paper presented at Europe Biobank Week 2024, Wien, Austria

* Hayn, D., Sandner, E., Vengadeswaran, A., Tãtaru, E. A., Wilkinson, M., Hanauer, M., Kreiner, K., & Schreier, G. (2024). Privacy-Preserving Linkage of Distributed Pseudonymised Datasets in a Virtual European Rare Disease Platform. *Studies in health technology and informatics*, 316, 1442–1446. https://doi.org/10.3233/SHTI240683

* Hayn, D., Falgenhauer, M., Kropf, M., Nitzlnader, M., Welte, S., Ebner, H., Ladenstein, R., Schleiermacher, G., Hero, B., & Schreier, G. (2016). IT Infrastructure for Merging Data from Different Clinical Trials and Across Independent Research Networks. *Studies in health technology and informatics*, 228, 287–291

* Ebner, H., Hayn, D., Falgenhauer, M., Nitzlnader, M., Schleiermacher, G., Haupt, R., Erminio, G., Defferrari, R., Mazzocco, K., Kohler, J., Tonini, G. P., Ladenstein, R., & Schreier, G. (2016). Piloting the European Unified Patient Identity Management (EUPID) Concept to Facilitate Secondary Use of Neuroblastoma Data from Clinical Trials and Biobanking. *Studies in health technology and informatics*, 223, 31–38


What are the first steps?
--------------------------

The first steps in integrating the EUPID Services involve understanding the service's capabilities and how it can be integrated into your organization's workflow. This includes:

* Reviewing the documentation and API specifications.
* Setting up a test environment to experiment with the service.
* Ensuring that all stakeholders are aware of the benefits and requirements of using the EUPID Services.

Please get in contact with the EUPID Services Team at contact@eupid.eu to organize an onboarding meeting and discuss your use case and integration steps in more detail.


What are the main/urgent questions people approach you with?
-------------------------------------------------------------

Common questions include:

* How to integrate the EUPID Services with existing systems?
* What are the data protection measures in place?
* How to generate and manage pseudonyms?
* What are the costs associated with using the EUPID Services?
* How do the EUPID Services ensure compliance with GDPR?
* Where are the EUPID Services hosted?
* Can a EUPID Services instance be hosted on premise?


Do any FAQs exist?
-------------------

No, currently not.


What costs are charged for use?
---------------------------------

The usage of the EUPID Services is license based and depends on the specific use case you want to use them for. The costs may vary depending on the scale of implementation (mainly the number of contexts and pseudonyms), the specific requirements of the organization and the application scenario. For more detailed information on service agreements please contact the EUPID Services Team directly via contact@eupid.eu.


.. rubric:: Footnotes

.. [#encca] https://siope.eu/encca/
.. [#gdpr] https://gdpr-info.eu/art-43-gdpr/
.. [#bioportal] https://clinicaltrials.gov/study/NCT05192980
.. [#monalisa] https://siope.eu/monalisa
.. [#ern] https://paedcan.ern-net.eu/
.. [#pancare] https://siope.eu/activities/joint-projects/survivorship-passport/
.. [#primage] https://www.primageproject.eu/
.. [#ejprd] https://www.ejprarediseases.org/
.. [#erdera] https://erdera.org/
