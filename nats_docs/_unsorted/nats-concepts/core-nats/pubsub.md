---
title: Publish-Subscribe
source: https://docs.nats.io/nats-concepts/core-nats/pubsub
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/core-nats/publish-subscribe/pubsub.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../nats-concepts.md))chevron-right
  2. [Core NATS](https://docs.nats.io/nats-concepts/core-nats) ([local](./../../../05_chevron-right/06_core-nats-chevron-right.md))

# Publish-Subscribe

## 

[hashtag](#publish-subscribe)

Publish-Subscribe

NATS implements a publish-subscribe message distribution model for one-to-many communication. A publisher sends a message on a subject and any active subscriber listening on that subject receives the message. Subscribers can also register interest in wildcard subjects that work a bit like a regular expression (but only a bit). This one-to-many pattern is sometimes called a fan-out.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-22d59af386038cc2717176561ffc95c63c295926%252Fpubsub.svg%3Falt%3Dmedia%26token%3Dcc54babb-76c4-4389-87fc-11e63429b341&width=768&dpr=3&quality=100&sign=13bec88f&sv=2)

## 

[hashtag](#messages)

Messages

Messages are composed of:

  1. A subject.

  2. A payload in the form of a byte array.

  3. Any number of header fields.

  4. An optional 'reply' address field.

Messages have a maximum size (which is set in the server configuration with `max_payload`). The size is set to 1 MB by default, but can be increased up to 64 MB if needed (though we recommend keeping the max message size to something more reasonable like 8 MB).

[PreviousCore NATSchevron-left](https://docs.nats.io/nats-concepts/core-nats) ([local](./../../../05_chevron-right/06_core-nats-chevron-right.md))[NextPub/Sub Walkthroughchevron-right](https://docs.nats.io/nats-concepts/core-nats/pubsub/pubsub_walkthrough) ([local](./pubsub/pubsub-walkthrough.md))

Last updated 4 years ago

Was this helpful?
