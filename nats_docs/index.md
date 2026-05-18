---
title: Welcome
source: https://docs.nats.io/
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/README.md)chevron-down

block-quoteOn this pageblock-quote

# Welcome

## 

[hashtag](#the-official-nats-documentation)

The official [NATSarrow-up-right](https://nats.io/) documentation

NATS is a simple, secure and high performance open source data layer for cloud native applications, IoT messaging, and microservices architectures.

We feel that it should be the backbone of your communication between services. It doesn't matter what language, protocol, or platform you are using; NATS is the best way to connect your services.

### 

[hashtag](#id-10-000-foot-view)

10,000 foot view

  * Publish and subscribe to messages at millions of messages per second. At most once delivery.

  * Supports fan-in/out delivery patterns

  * Request/reply

  * Every major language is supported

  * Persistence via JetStream

    * at least once delivery or **exactly once** delivery

    * work queues

    * stream processing

    * data replication

    * data retention

    * data deduplication

    * Higher order data structures

      * Key/Value with watchers, versioning, and TTL

      * Object storage with versioning

  * Security

    * TLS

    * JWT-based zero trust security

  * Clustering

    * High availability

    * Fault tolerance

    * Auto-discovery

  * Protocols supported

    * TCP

    * MQTT

    * WebSockets

All of this in a single binary that is easy to deploy and manage. No external dependencies, just drop it in and add a configuration file to point to other NATS servers and you are ready to go. In fact, you can even embed NATS in your application (for Go users)!

## 

[hashtag](#guided-tour)

Guided tour

  1. In general we recommend trying to solve your problems first using [Core NATS](https://docs.nats.io/nats-concepts/core-nats) ([local](./05_chevron-right/06_core-nats-chevron-right.md)).

  2. If you need to share state between services, take a look at the [KV](https://docs.nats.io/nats-concepts/jetstream/key-value-store) ([local](./14_hashtag-guided-tour/02_kv.md)) or [Object Store](https://docs.nats.io/nats-concepts/jetstream/obj_store) ([local](./14_hashtag-guided-tour/03_object-store.md)) in JetStream.

  3. When you need lower level access to persistence streams, move on to using [JetStream](https://docs.nats.io/nats-concepts/jetstream) ([local](./05_chevron-right/08_jetstream-chevron-right.md)) directly for more advanced messaging patterns.

  4. Learn about [deployment strategies](https://docs.nats.io/nats-concepts/service_infrastructure/adaptive_edge_deployment) ([local](./14_hashtag-guided-tour/05_deployment-strategies.md))

  5. Secure your deployments with [zero trust security](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt) ([local](./14_hashtag-guided-tour/06_zero-trust-security.md))

## 

[hashtag](#contribute)

Contribute

NATS is Open Source as is this documentation. Please [let us knowenvelope](mailto:info@nats.io) if you have updates and/or suggestions for these docs. You can also create a Pull Request using the `Edit on GitHub` link on each page.

## 

[hashtag](#additional-questions)

Additional questions?

Feel free to chat with us on Slack [slack.nats.ioarrow-up-right](https://slack.nats.io).

Thank you from the entire NATS Team of Maintainers for your interest in NATS!

[NextWhat's New!chevron-right](https://docs.nats.io/release-notes/whats_new) ([local](./03_chevron-right/01_what-s-new-chevron-right.md))

Last updated 9 months ago

Was this helpful?
