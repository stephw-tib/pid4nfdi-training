ePIC - Persistent Identifier Consortium for eResearch
===========================

What is an ePIC PID?
-------------

The ePIC (Persistent Identifier Consortium for eResearch) PID is a globally unique, persistent identifier designed for
long-term management and referencing of digital and physical resources. Developed by the ePIC consortium, it ensures
that data, samples, publications, or other research outputs remain accessible and citable over time. The system supports
robust metadata and flexible resolution services, making it a versatile tool for managing research assets in a reliable
and interoperable manner. The PIDs created and maintained are based on the `Handle System <https://www.handle.net/>`_.

Key features and common use-cases of the ePIC Service include:

- **Flexible Metadata Schema and Research Entities**: The ePIC PID Service does not preset a provider-specified metadata schema. Hence, ePIC PIDs can be assigned to any kind of research entities. Infrastructure managers have the possibility to register a metadata schema tailored to their use-case. The `ePIC Data Type Registry <https://typeregistry.lab.pidconsortium.net/>`_ is a tool which can be used to define and openly register the metadata schema based on JSON.

- **PIDs for unpublished data**: ePIC PIDs can be assigned to data before being published. Another PID, such as DOI, can be additionally assigned at publication time.

- **Large numbers of PIDs**: Due to it's cost model, the ePIC service allows for cost-efficient PID assignment even if large numbers of PIDs are generated.

How do I get an ePIC PID?
---------------------
todo: as a researcher, ask your institution. as a service provider, as email-contact; divide 1&2 from 3,4,5
todo: add information about prefix registration service and fee model by GWDG

If you are an infrastructure provider and you would like to set up ...
To obtain an ePIC PID, you need to work with a registered ePIC service provider, which is typically a member of the ePIC Consortium. Here’s a step-by-step guide:

1. **Find a Service Provider**: Identify an organization within the ePIC Consortium that offers PID (Persistent Identifier) services. Many are universities, research institutions, data centers, or National Research & Education Networks (NREN).

2. **Register as a Client**: Contact the provider to register and set up access to their PID services. The client will usually be provided with a dedicated namespace/prefix. The prefix is allocated in the top level namespace 21. Based on the policy of ePIC the Client will get access to the APIs for the management of PID and their metadata.

If you are a researcher,
3. **Provide Metadata**: Submit the necessary metadata for the resource you want to identify. The specific requirements will depend on the service provider and the type of resource. The metadata attributes of the PID can be standardize by using the typing service https://typeregistry.lab.pidconsortium.net/

4. **Obtain the Identifier**: Once your metadata is submitted, the service provider will issue a unique ePIC identifier.

5. **Use and Manage the Identifier**: Integrate the ePIC into your workflows for citation, sharing, and resource management. Updates or additional metadata can often be added as needed.

For more detailed guidance
---------------

* explore the ePIC Consortium website (https://www.pidconsortium.net/) for additional information and a list of participating providers.. 

* start with the `FAQ section <https://www.pidconsortium.net/?page_id=1060>`_. 

* The API documentation can be found here: https://doc.pidconsortium.eu/docs/. 

* To get support for the selection of metadata or the typing of metadata attributes, please contact: support@pidconsortium.net. 

Interoperability
----------------

The ePIC system is fully interoperable with DOI (Digital Object Identifier) standards. Any ePIC identifier, including its prefix, can also be resolved using the Global Handle Resolver, ensuring seamless integration into existing research infrastructures. 

Contact
-------

If you have a project for which PIDs need to be generated, please contact support@pidconsortium.eu.
todo: prefix registration service
