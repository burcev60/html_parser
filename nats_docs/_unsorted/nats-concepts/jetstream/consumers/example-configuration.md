---
title: Example
source: https://docs.nats.io/nats-concepts/jetstream/consumers/example_configuration
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/example_configuration.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../../nats-concepts.md))chevron-right
  2. [JetStream](https://docs.nats.io/nats-concepts/jetstream) ([local](./../../../../05_chevron-right/08_jetstream-chevron-right.md))chevron-right
  3. [Consumers](https://docs.nats.io/nats-concepts/jetstream/consumers) ([local](./../consumers.md))

# Example

Consider this architecture

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-dedcc17f082fa1e39497c54ed8191b6424ee7792%252Fstreams-and-consumers-75p.png%3Falt%3Dmedia%26token%3D3dc2026b-8ef1-4f5b-a844-b3dbce6abbd9&width=768&dpr=3&quality=100&sign=a3db84fb&sv=2)

Orders

While it is an incomplete architecture it does show a number of key points:

  * Many related subjects are stored in a Stream

  * Consumers can have different modes of operation and receive just subsets of the messages

  * Multiple Acknowledgement modes are supported

A new order arrives on `ORDERS.received`, gets sent to the `NEW` Consumer who, on success, will create a new message on `ORDERS.processed`. The `ORDERS.processed` message again enters the Stream where a `DISPATCH` Consumer receives it and once processed it will create an `ORDERS.completed` message which will again enter the Stream. These operations are all `pull` based meaning they are work queues and can scale horizontally. All require acknowledged delivery ensuring no order is missed.

All messages are delivered to a `MONITOR` Consumer without any acknowledgement and using Pub/Sub semantics - they are pushed to the monitor.

As messages are acknowledged to the `NEW` and `DISPATCH` Consumers, a percentage of them are Sampled and messages indicating redelivery counts, ack delays and more, are delivered to the monitoring system.

## 

[hashtag](#example-configuration)

Example Configuration

[Additional documentation](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/administration) ([local](./../../../running-a-nats-service/configuration/clustering/jetstream-clustering/administration.md)) introduces the `nats` utility and how you can use it to create, monitor, and manage streams and consumers, but for completeness and reference this is how you'd create the ORDERS scenario. We'll configure a 1 year retention for order related messages:

Copy

```

    nats stream add ORDERS --subjects "ORDERS.*" --ack --max-msgs=-1 --max-bytes=-1 --max-age=1y --storage file --retention limits --max-msg-size=-1 --discard=old
    nats consumer add ORDERS NEW --filter ORDERS.received --ack explicit --pull --deliver all --max-deliver=-1 --sample 100
    nats consumer add ORDERS DISPATCH --filter ORDERS.processed --ack explicit --pull --deliver all --max-deliver=-1 --sample 100
    nats consumer add ORDERS MONITOR --filter '' --ack none --target monitor.ORDERS --deliver last --replay instant

```

[PreviousConsumerschevron-left](https://docs.nats.io/nats-concepts/jetstream/consumers) ([local](./../consumers.md))[NextJetStream Walkthroughchevron-right](https://docs.nats.io/nats-concepts/jetstream/js_walkthrough) ([local](./../js-walkthrough.md))

Last updated 4 years ago

Was this helpful?
