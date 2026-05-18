---
title: What is NATS
source: https://docs.nats.io/nats-concepts/what-is-nats
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/what-is-nats/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../_unsorted/nats-concepts.md))

# What is NATS

Software applications and services need to exchange data. NATS is an infrastructure that allows such data exchange, segmented in the form of messages. We call this a "**message oriented middleware** ".

With NATS, application developers can:

  * Effortlessly build distributed and scalable client-server applications.

  * Store and distribute data in realtime in a general manner. This can flexibly be achieved across various environments, languages, cloud providers and on-premises systems.

### 

[hashtag](#nats-client-applications)

NATS Client Applications

Developers use one of the NATS client libraries in their application code to allow them to publish, subscribe, request and reply between instances of the application or between completely separate applications. Those applications are generally referred to as 'client applications' or sometimes just as 'clients' throughout this manual (since from the point of view of the NATS server, they are clients).

### 

[hashtag](#nats-service-infrastructure)

NATS Service Infrastructure

The NATS services are provided by one or more NATS server processes that are configured to interconnect with each other and provide a _NATS service infrastructure_. The NATS service infrastructure can scale from a single NATS server process running on an end device (the `nats-server` process is less than 20 MB in size!) all the way to a public global super-cluster of many clusters spanning all major cloud providers and all regions of the world such as Synadia's NGS.

### 

[hashtag](#connecting-nats-client-applications-to-the-nats-servers)

Connecting NATS Client applications to the NATS servers

To connect a NATS client application with a NATS service, and then subscribe or publish messages to subjects, it only needs to be configured with:

  1. **URL:** A ['NATS URL'](https://docs.nats.io/using-nats/developer/connecting#nats-url) ([local](./../_unsorted/using-nats/developer/connecting.md#nats-url)). This is a string (in a URL format) that specifies the IP address and port where the NATS server(s) can be reached, and what kind of connection to establish (plain TCP, TLS, or Websocket).

  2. **Authentication** (if needed): [Authentication](https://docs.nats.io/using-nats/developer/connecting#authentication-details) ([local](./../_unsorted/using-nats/developer/connecting.md#authentication-details)) details for the application to identify itself with the NATS server(s). NATS supports multiple authentication schemes (username/password, decentralized JWT, token, TLS certificates and Nkey with challenge).

## 

[hashtag](#simple-messaging-design)

Simple messaging design

NATS makes it easy for applications to communicate by sending and receiving messages. These messages are addressed and identified by subject strings, and do not depend on network location.

Data is encoded and framed as a message and sent by a publisher. The message is received, decoded, and processed by one or more subscribers.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-19a2ced7956b0b0681a8d97c2684d8669120eaec%252Fintro.svg%3Falt%3Dmedia%26token%3D2060c455-8ed1-4c18-b903-9cf12265117d&width=768&dpr=3&quality=100&sign=a79d6ea7&sv=2)

With this simple design, NATS lets programs share common message-handling code, isolate resources and interdependencies, and scale by easily handling an increase in message volume, whether those are service requests or stream data.

### 

[hashtag](#nats-quality-of-service-qos)

NATS Quality of service (QoS)

NATS offers multiple qualities of service, depending on whether the application uses just the _Core NATS_ functionality or also leverages the added functionalities enabled by _NATS JetStream_ (JetStream is built into `nats-server` but may not be enabled on all service infrastructures).

  * **At most once QoS:** _Core NATS_ offers an **at most once** quality of service. If a subscriber is not listening on the subject (no subject match), or is not active when the message is sent, the message is not received. This is the same level of guarantee that TCP/IP provides. _Core NATS_ is a fire-and-forget messaging system. It will only hold messages in memory and will never write messages directly to disk.

  * **At-least / exactly once QoS:** If you need higher qualities of service (**at least once** and **exactly once**), or functionalities such as persistent streaming, de-coupled flow control, and Key/Value Store, you can use [NATS JetStream](https://docs.nats.io/nats-concepts/jetstream) ([local](./08_jetstream-chevron-right.md)), which is built in to the NATS server (but needs to be enabled). Of course, you can also always build additional reliability into your client applications yourself with proven and scalable reference designs such as acks and sequence numbers.

[PreviousCompare NATSchevron-left](https://docs.nats.io/nats-concepts/overview/compare-nats) ([local](./../_unsorted/nats-concepts/overview/compare-nats.md))[NextWalkthrough Setupchevron-right](https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup) ([local](./../_unsorted/nats-concepts/what-is-nats/walkthrough-setup.md))

Last updated 4 years ago

Was this helpful?
