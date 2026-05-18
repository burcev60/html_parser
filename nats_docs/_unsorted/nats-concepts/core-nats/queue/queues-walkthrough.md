---
title: Queueing Walkthrough
source: https://docs.nats.io/nats-concepts/core-nats/queue/queues_walkthrough
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/core-nats/queue-groups/queues_walkthrough.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../../nats-concepts.md))chevron-right
  2. [Core NATS](https://docs.nats.io/nats-concepts/core-nats) ([local](./../../../../05_chevron-right/06_core-nats-chevron-right.md))chevron-right
  3. [Queue Groups](https://docs.nats.io/nats-concepts/core-nats/queue) ([local](./../queue.md))

# Queueing Walkthrough

NATS supports a form of load balancing using [queue groups](https://docs.nats.io/nats-concepts/core-nats/queue) ([local](./../queue.md)). Subscribers register a queue group name. A single subscriber in the group is randomly selected to receive the message.

## 

[hashtag](#walkthrough-prerequisites)

Walkthrough prerequisites

If you have not already done so, you need to [install](https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup) ([local](./../../what-is-nats/walkthrough-setup.md)) the `nats` CLI tool and optionally the nats-server on your machine.

### 

[hashtag](#id-1.-start-the-first-member-of-the-queue-group)

1\. Start the first member of the queue group

The `nats reply` instances don't just subscribe to the subject but also automatically join a queue group (`"NATS-RPLY-22"` by default)

Copy

```

    nats reply foo "service instance A Reply# {{Count}}"

```

### 

[hashtag](#id-2.-start-a-second-member-of-the-queue-group)

2\. Start a second member of the queue group

In a new window

Copy

```

    nats reply foo "service instance B Reply# {{Count}}"

```

### 

[hashtag](#id-3.-start-a-third-member-of-the-queue-group)

3\. Start a third member of the queue group

In a new window

Copy

```

    nats reply foo "service instance C Reply# {{Count}}"

```

### 

[hashtag](#id-4.-publish-a-nats-message)

4\. Publish a NATS message

Copy

```

    nats request foo "Simple request"

```

### 

[hashtag](#id-5.-verify-message-publication-and-receipt)

5\. Verify message publication and receipt

You should see that only one of the my-queue group subscribers receives the message and replies to it, and you can also see which one of the available queue group subscribers processed the request from the reply message received (i.e. service instance A, B or C)

### 

[hashtag](#id-6.-publish-another-message)

6\. Publish another message

Copy

```

    nats request foo "Another simple request"

```

You should see that a different queue group subscriber receives the message this time, chosen at random among the 3 queue group members.

You can also send any number of requests back-to-back. From the received messages, you'll see the distribution of those requests amongst the members of the queue group. For example: `nats request foo --count 10 "Request {{Count}}"`

### 

[hashtag](#id-7.-stop-start-queue-group-members)

7\. Stop/start queue group members

You can at any time start yet another service instance, or stop one and see how the queue group automatically takes care of adding/removing those instances from the group.

## 

[hashtag](#see-also)

See Also

Queue groups using the NATS CLI

Queue Groups NATS CLI

[PreviousQueue Groupschevron-left](https://docs.nats.io/nats-concepts/core-nats/queue) ([local](./../queue.md))[NextJetStreamchevron-right](https://docs.nats.io/nats-concepts/jetstream) ([local](./../../../../05_chevron-right/08_jetstream-chevron-right.md))

Last updated 1 month ago

Was this helpful?
