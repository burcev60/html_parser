---
title: Core NATS
source: https://docs.nats.io/nats-concepts/core-nats
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/core-nats/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../_unsorted/nats-concepts.md))

# Core NATS

Core NATS is the foundational functionality in a NATS system. It operates on a publish-subscribe model using subject/topic-based addressing. This model offers two significant advantages: location independence and a default many-to-many (M:N) communication pattern. These fundamental concepts enable powerful and innovative solutions for common development patterns, such as microservices, without requiring additional technologies like load balancers, API gateways, or DNS configuration.

NATS systems can be enhanced with [JetStream](https://docs.nats.io/nats-concepts/jetstream) ([local](./08_jetstream-chevron-right.md)), which adds persistence capabilities. While Core NATS provides best-effort, at-most-once message delivery, JetStream introduces at-least-once and exactly-once semantics.

[PreviousSubject-Based Messagingchevron-left](https://docs.nats.io/nats-concepts/subjects) ([local](./05_subject-based-messaging.md))[NextPublish-Subscribechevron-right](https://docs.nats.io/nats-concepts/core-nats/pubsub) ([local](./../_unsorted/nats-concepts/core-nats/pubsub.md))

Last updated 1 year ago

Was this helpful?
