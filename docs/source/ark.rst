ARK - Archival Resource Key
===========================

What is ARK?
------------

ARK identifiers are decentralised managed PIDs that are openly available and can be assigned by any institution. The identifiers are agnostic to the resource type. They can be applied to datasets, texts, artifacts, persons etc. on different levels of granularity: e.g. they also support identifying subsets of resources (see: Structure and Features).

ARKs are commonly utilized by GLAM institutions. Each institution generating ARKs has the flexibility to establish its own policies and services. As a decentralized service, ARK does not maintain a comprehensive registry of all ARK identifiers in use. These identifiers can also serve purely internal purposes within databases. However, it is estimated that over 8 billion ARKs are currently publicly discoverable.


History and Community
---------------------

ARK was launched in 2001 by the California Digital Library (CDL). In 2018, CDL partnered with LYRASIS (formerly DuraSpace), a collaboration that culminated in the establishment of the ARK Alliance in 2021. That same year, the Alliance joined the U.S. National Digital Stewardship Alliance (NDSA) as a member.

Currently, ARK offers several social media channels and `discussion forums <https://arks.org/community/>`_ in English, French, and Spanish/Portuguese. Additionally, it facilitates various `working groups <https://arks.org/community-groups/>`_ focused on topics such as technical development, outreach, NAAN-related issues, and an Advisory Group.


How to get an ARK?
------------------

ARKs rely on distributed resolution through institutions that manage the Name Assigning Authority Numbers (NAAN). ARK is using the Name-to-Thing (N2T) resolver service hosted by CDL. N2T is identifier agnostic, supporting various identifier systems beyond ARKs, including handle-based DOIs. It functions as both a resolver and a meta-resolver by redirecting identifiers to appropriate targets, ensuring stable and persistent links across systems.

Obtaining a NAAN for generating ARKs is free, and open-source software is available for minting ARKs and creating related metadata. 
The ARK Alliance provides information on `how to get started with ARKs <https://arks.org/about/getting-started-implementing-arks/>`_. 


Structure and Features
----------------------
How does an ARK look like? Here is an example of the structure:

.. code-block:: console

    https://n2t.net/ark:/12345/abc123/section1

    Elements:
    1. The Base URL begins with a resolver address: [https://n2t.net/]
    2. The ARK Label indicates the identifier type [ark:]
    3. The NAAN is assigned to the organization managing the identifier: [12345]
    4. The Name or Local Identifier is a unique string representing the resource within the namespace of the managing organization: [abc123]
    5. The Qualifier (optional) is an additional string used to  
        a. refer to a specific version or subset of the resource: [section1]
        b. contain further metadata information using a [?] suffix: e.g. http://example.org/ark:/12345/abcde?

ARKs are designed to be human- and machine-readable, making them versatile for use across various systems. The identifier does not require any metadata, but supports the usage of multiple schemata. This design is intended to allow the registration of ARKs at every lifecycle stage of an entity and at every granularity level. For further information, please see overview of `features <https://arks.org/about/ark-features/>`_.


More information
----------------

  * The ARK Alliance provides comprehensive information on ARKs, their functionalities and community: https://arks.org/
  * ARK identifiers Wiki with `FAQ <https://wiki.lyrasis.org/display/ARKs/ARK+Identifiers+FAQ>`_ 
  * About the `N2T (meta) resolver service <https://legacy-n2t.n2t.net/e/about.html>`_
  * A quick summary is provided by John Kunze and Donny Winston in “Getting started with ARK (Archival Resource Key) Persistent Identifiers” (2024): https://www.youtube.com/watch?v=-RkMGFCGRic 


