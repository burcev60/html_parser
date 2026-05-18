---
title: Request-Reply
source: https://docs.nats.io/nats-concepts/core-nats/reqreply
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/core-nats/request-reply/reqreply.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../nats-concepts.md))chevron-right
  2. [Core NATS](https://docs.nats.io/nats-concepts/core-nats) ([local](./../../../05_chevron-right/06_core-nats-chevron-right.md))

# Request-Reply

Request-Reply is a common pattern in modern distributed systems. A request is sent, and the application either waits on the response with a certain timeout, or receives a response asynchronously.

The increased complexity of modern systems necessitates features like [location transparencyarrow-up-right](https://en.wikipedia.org/wiki/Location_transparency), scale-up and scale-down, observability (measuring a system's state based on the data it generates) and more. In order to implement this feature-set, various other technologies needed to incorporate additional components, sidecars (processes or services that support the primary application) and proxies. NATS on the other hand, implemented Request-Reply much more easily.

### 

[hashtag](#nats-makes-request-reply-simple-and-powerful)

NATS makes Request-Reply simple and powerful

  * NATS supports the Request-Reply pattern using its core communication mechanism — publish and subscribe. A request is published on a given subject using a reply subject. Responders listen on that subject and send responses to the reply subject. Reply subjects are called "**inbox** ". These are unique subjects that are dynamically directed back to the requester, regardless of the location of either party.

  * Multiple NATS responders can form dynamic queue groups. Therefore, it's not necessary to manually add or remove subscribers from the group for them to start or stop being distributed messages. It’s done automatically. This allows responders to scale up or down as per demand.

  * NATS applications "drain before exiting" (processing buffered messages before closing the connection). This allows the applications to scale down without dropping requests.

  * Since NATS is based on publish-subscribe, observability is as simple as running another application that can view requests and responses to measure latency, watch for anomalies, direct scalability and more.

  * The power of NATS even allows multiple responses, where the first response is utilized and the system efficiently discards the additional ones. This allows for a sophisticated pattern to have multiple responders, reduce response latency and jitter.

### 

[hashtag](#the-pattern)

The pattern

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-dc10798d4afca301adba55c1e85c599b25a2ae24%252Freqrepl.svg%3Falt%3Dmedia%26token%3Dc224906b-c08b-492f-b083-cf247bc60efd&width=768&dpr=3&quality=100&sign=3e8a6ff3&sv=2)

Try NATS request-reply on your own, using a live server by walking through the [request-reply walkthrough.](https://docs.nats.io/nats-concepts/core-nats/reqreply/reqreply_walkthrough) ([local](./reqreply/reqreply-walkthrough.md))

### 

[hashtag](#no-responders)

No responders

When a request is sent to a subject that has no subscribers, it can be convenient to know about it right away. For this use-case, a NATS client can [opt-into no_responder messages](https://docs.nats.io/reference/reference-protocols/nats-protocol#syntax-1) ([local](./../../reference/reference-protocols/nats-protocol.md#syntax-1)). This requires a server and client that support headers. When enabled, a request sent to a subject with no subscribers will immediately receive a reply that has no body, and a `503` status.

Most clients will represent this case by raising or returning an error. For example:

Copy

```

    m, err := nc.Request("foo", nil, time.Second);
    # err == nats.ErrNoResponders

```

[PreviousPub/Sub Walkthroughchevron-left](https://docs.nats.io/nats-concepts/core-nats/pubsub/pubsub_walkthrough) ([local](./pubsub/pubsub-walkthrough.md))[NextRequest-Reply Walkthroughchevron-right](https://docs.nats.io/nats-concepts/core-nats/reqreply/reqreply_walkthrough) ([local](./reqreply/reqreply-walkthrough.md))

Last updated 3 years ago

Was this helpful?
