ARK - Archival Resource Key
===========================

What is an ARK?
------------
ARK identifiers are globally unique PIDs that are openly available and can be assigned by any institution that commits to their persistence. Since 2001 these identifiers have been agnostic to resource type and have been used to cite datasets, texts, physical artifacts, persons, vocabulary terms, etc. They also support different levels of granularity, as well as containment and variant relationships (see: Structure and Features). A compact ARK looks like

`ark:/12148/btv1b8449691v/f29 <https://gallica.bnf.fr/ark:/12148/btv1b8449691v/f29>`_

where the 12148/ prefix is a Name Assigning Authority Number (NAAN) and the rest is the assigned name. The full ARK is created by prepending a resolver such as https://n2t.net/ to the compact ARK, which is used to make the above hyperlink actionable. This ARK is from the National Library of France, and identifies page 29 of a medieval manuscript. 


How can I create ARKs?
----------------------

To get started, `request a NAAN <https://docs.google.com/forms/d/e/1FAIpQLSf_847hNXtLGikR-XeDy1uT1AKd24DpHnt5UQh2i8ORRu7u-w/viewform>`_ for your organization and you should hear back from the ARK Alliance (`arks.org <https://arks.org/>`_) within about 2 business days. Once you have a unique 5-digit NAAN, you can assign and publicize (issue, publish) your ARKs with as much autonomy as you assign URLs. There are no fees. Except for redirection via the N2T (Name to Thing) resolver `(n2t.net) <https://n2t.net/>`_, NAAN maintenance, and documentation, there are no other services from the ARK Alliance.

Obtaining a NAAN for generating ARKs is free, and open-source software is available for minting ARKs and creating related metadata. The ARK Alliance provides information on `how to get started with ARKs <https://arks.org/about/getting-started-implementing-arks/>`_.


Community and History
---------------------
ARKs are commonly utilized by GLAM institutions and small publishers. There are over 1600 ARK organizations, each of which has the flexibility to establish its own policies and services. Because ARKs are decentralized, there is no comprehensive registry of all ARK identifiers in use. These identifiers can also serve purely internal purposes within databases. However, it is estimated that over 8 billion ARKs are currently publicly discoverable.

ARK was launched in 2001 by the California Digital Library (CDL). In 2018, CDL partnered with LYRASIS (formerly DuraSpace), a collaboration that culminated in the establishment of the ARK Alliance in 2021. That same year, the Alliance joined the U.S. National Digital Stewardship Alliance (NDSA) as a member.

Currently, ARK offers several social media channels and `discussion forums <https://arks.org/community/>`_ in English, French, and Spanish/Portuguese. Additionally, it facilitates various `working groups <https://arks.org/community-groups/>`_ focused on topics such as technical development, outreach, NAAN-curation, and an Advisory Group.


ARK Resolution
------------------

The global resolver for ARKs is n2t.net, but its use is not required. Among PIDs, ARKs are atypical in that an organization can choose to publish its ARKs based either at either n2t.net or at its own local organizational server (resolver). An estimated 75% of ARKs in the world are based in local resolvers, knowing that n2t.net can be a backup in case their organizational domain name is at risk. The example ARK above is usually published as

`https://gallica.bnf.fr/ark:/12148/btv1b8449691v/f29 <https://gallica.bnf.fr/ark:/12148/btv1b8449691v/f29>`_

The core, globally unique identity of every ARK is its compact form, which helps persistence because no organization lasts forever. If need be, the compact ARK retains its identity when it is appended to a different resolver.

As with all PIDs, the technical persistence mechanism for ARKs is web redirection. An unusual feature of the global ARK resolver, n2t.net, is that it extends its redirection services to hundreds of other identifier schemes (hence "ark" is not part of its name). This relieves users from having to remember 10 different resolver domain names for 10 different PID schemes. Instead, just remember the scheme prefix, such as "ark:", "handle:", or “pdb:” and append the compact identifier to n2t.net.


Structure and Features
----------------------
What does an ARK look like? Here is an example of the structure:

.. code-block:: console

    `https://gallica.bnf.fr/ark:/12148/btv1b8449691v/f29 <https://gallica.bnf.fr/ark:/12148/btv1b8449691v/f29>`_

    Elements:
    1. The overall URL begins with a resolver address: [https://gallica.bnf.fr/]
    2. The ARK Label indicates the identifier type [ark:/]
    3. The NAAN is assigned to the organization (in this case, the BnF – Bibliothèque nationale de France) managing the identifier: [12148]
    4. The Name or Local Identifier is a unique string, often opaque, representing the resource within the namespace of the managing organization: [btv1b8449691v]
    5. The Qualifier (optional) is an additional string used to refer to a specific version or subpart of the resource (in this case, page 29): [f29]


ARKs have very flexible metadata, from none to arbitrarily rich metadata following multiple schemata. So you can assign an ARK to a thing before you create it, and add metadata as the thing matures. Many ARKs have metadata following the Dublin Core or DataCite schemas. This design is intended to allow the registration of ARKs at every lifecycle stage of an entity and at every granularity level. For further information, please see overview of `features <https://arks.org/about/ark-features/>`_.

What are the Advantages of ARK Identifiers?
-------------------------------------------
ARKs offer flexibility: organizations can create and manage ARKs using open-source tools, without depending on centralized systems, while still enabling global resolution. They support multiple metadata formats and can be customized with additional information, making them useful across various use cases. ARKs can be assigned to anything from digital files and physical artifacts to conceptual entities.

ARKs are cost-efficient: There are no fees for registering or maintaining ARKs, which lowers financial barriers and makes PIDs more accessible to a wide range of institutions and communities.


More information
----------------

  * The ARK Alliance provides comprehensive information on ARKs, their functionalities and community: https://arks.org/
  * ARK identifiers `FAQ <https://arks.org/about/ark-faq-en/>`_ 
  * About the `N2T (meta-)resolver service <https://arks.org/about/n2t-global-resolver/>`_

  * A 30-minute summary is provided by John Kunze and Donny Winston in “Getting started with ARK (Archival Resource Key) Persistent Identifiers” (2024): https://www.youtube.com/watch?v=-RkMGFCGRic 

----

Creator: Stephanie Hagemann-Wilholt (https://orcid.org/0000-0002-0474-2410)
