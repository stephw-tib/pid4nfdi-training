ePIC - Persistent Identifier Consortium for eResearch
=====================================================

What is an ePIC PID?
--------------------

The **ePIC (Persistent Identifier Consortium for eResearch) PID** is a globally unique, persistent identifier designed for
long-term management and referencing of digital and physical resources. Developed by the ePIC consortium, it ensures
that data, samples, publications, or other research outputs remain accessible and citable over time. The system supports
robust metadata and flexible resolution services, making it a versatile tool for managing research assets in a reliable
and interoperable manner.

The PIDs created and maintained are based on the `Handle System <https://www.handle.net/>`_. Every handle consists of
two parts ``prefix/suffix``: its naming authority, otherwise known as its prefix, and a unique local name under the naming
authority, otherwise known as its suffix. ePIC prefixes are allocated in the top level namespace 21., hence have the
format ``21.xxxx/xxxx``. Prefixes are often assigned per institution, with each suffix uniquely identifying objects within
this namespace. Thanks to the combination of prefix and suffix, any handle is globally unique within the context of the
Handle System.

Key features and common use-cases
---------------------------------
Key features and common use-cases of the ePIC Service include, but are not limited to:

- **Flexible Metadata Schema and Research Entities**: The ePIC PID Service does not preset a provider-specified metadata schema. Hence, ePIC PIDs can be assigned to any kind of research entities. Infrastructure managers have the possibility to register a metadata schema tailored to their use-case. The `ePIC Data Type Registry <https://typeregistry.lab.pidconsortium.net/>`_ is a typing service which can be used to define and openly register the metadata attributes of the PID.

- **PIDs for unpublished data**: ePIC PIDs can be assigned to data before being published. Another PID, such as DOI, can be additionally assigned at publication time, if desired.

- **Large numbers of PIDs**: Due to it's cost model, the ePIC service allows for cost-efficient PID assignment especially if large numbers of PIDs are generated.

How do I set up infrastructure to assign ePIC PIDs?
---------------------------------------------------
If you are an infrastructure manager and you would like to set up infrastructure (e.g. repository, PID service, ...) which enables end-users to assign ePIC PIDs, you need to work with a member of the ePIC Consortium. Here’s a short guide:

- **PID4NFDI Prefix Registration Service**: If you set up infrastructure for NFDI, please check out our `Prefix Registration Service <https://pid.services.base4nfdi.de/services/prefix-registration/>`_. A free of charge ePIC prefix (issued by GWDG as an ePIC member) can be directly requested via the service for your PID use-case with up to 50.000 ePIC PIDs per year.

If the prefix registration service does not fit your needs, you can proceed as follows:

- **Find a Service Provider and Register as a Client**: Identify an organization within the ePIC Consortium that offers PID (Persistent Identifier) services. Many are universities, research institutions, data centers, or National Research & Education Networks (NREN). Contact the provider to register and set up access to their PID services. The client will usually be provided with a dedicated namespace/prefix. The prefix is allocated in the top level namespace 21. Based on the policy of ePIC the Client will get access to the APIs for the management of PID and their metadata.

.. - **Obtain, Use and Manage Identifiers**: Submit the necessary metadata for the resource you want to identify. The specific requirements will depend on the infrastructure and the type of resource. Once your metadata is submitted, the infrastructure will issue a unique ePIC identifier.Integrate the ePIC into your workflows for citation, sharing, and resource management. Updates or additional metadata can often be added as needed.


For more detailed guidance
---------------

* Explore the ePIC Consortium website (https://www.pidconsortium.net/) for additional information and a list of participating providers..

* Start with the `FAQ section <https://www.pidconsortium.net/?page_id=1060>`_.

* The API documentation can be found here: https://doc.pidconsortium.eu/docs/. 

* To get support for the selection of metadata or the typing of metadata attributes, please contact: support@pidconsortium.net. 

Interoperability
----------------

The ePIC system is fully interoperable with DOI (Digital Object Identifier) standards. Any ePIC identifier, including its prefix, can also be resolved using the Global Handle Resolver, ensuring seamless integration into existing research infrastructures. 

Contact
-------

If you have a project for which PIDs need to be generated, please contact support@pidconsortium.eu or check out our `PID4NFDI Prefix Registration Service <https://pid.services.base4nfdi.de/services/prefix-registration/>`_.


----

Creators: Torsten Kahlert (https://orcid.org/0009-0003-3264-5006), Jana Böhm (https://orcid.org/0009-0004-9802-113X)
