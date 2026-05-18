---
title: Pub/Sub Walkthrough
source: https://docs.nats.io/nats-concepts/core-nats/pubsub/pubsub_walkthrough
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/core-nats/publish-subscribe/pubsub_walkthrough.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../../nats-concepts.md))chevron-right
  2. [Core NATS](https://docs.nats.io/nats-concepts/core-nats) ([local](./../../../../05_chevron-right/06_core-nats-chevron-right.md))chevron-right
  3. [Publish-Subscribe](https://docs.nats.io/nats-concepts/core-nats/pubsub) ([local](./../pubsub.md))

# Pub/Sub Walkthrough

NATS is a [publish subscribe](https://docs.nats.io/nats-concepts/core-nats/pubsub) ([local](./../pubsub.md)) messaging system [based on subjects](https://docs.nats.io/nats-concepts/subjects) ([local](./../../../../05_chevron-right/05_subject-based-messaging.md)). Subscribers listening on a subject receive messages published on that subject. If the subscriber is not actively listening on the subject, the message is not received. Subscribers can use the wildcard tokens such as `*` and `>` to match a single token or to match the tail of a subject.

## 

[hashtag](#nats-pub-sub-walkthrough)

NATS Pub/Sub Walkthrough

This simple walkthrough demonstrates some ways in which subscribers listen on subjects, and publishers send messages on specific subjects.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-a0d442c25fbeedf8400da6e26a2894e78df505ed%252Fpubsubtut.svg%3Falt%3Dmedia%26token%3D6e58b7ba-9f48-4b32-9cd1-46a70d3d3739&width=768&dpr=3&quality=100&sign=1d1e81f8&sv=2)

### 

[hashtag](#walkthrough-prerequisites)

Walkthrough prerequisites

If you have not already done so, you need to [install](https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup) ([local](./../../what-is-nats/walkthrough-setup.md)) the `nats` CLI Tool and optionally the nats-server on your machine.

#### 

[hashtag](#id-1.-create-subscriber-1)

1\. Create Subscriber 1

In a shell or command prompt session, start a client subscriber program.

Copy

```

    nats sub <subject>

```

Here, `<subject>` is a subject to listen on. It helps to use unique and well thought-through subject strings because you need to ensure that messages reach the correct subscribers even when wildcards are used.

For example:

Copy

```

    nats sub msg.test

```

You should see the message: _Listening on [msg.test]_

#### 

[ hashtag](#id-2.-create-a-publisher-and-publish-a-message)

2\. Create a Publisher and publish a message

In another shell or command prompt, create a NATS publisher and send a message.

Copy

```

    nats pub <subject> <message>

```

Where `<subject>` is the subject name and `<message>` is the text to publish.

For example:

Copy

```

    nats pub msg.test "NATS MESSAGE"

```

#### 

[hashtag](#id-3.-verify-message-publication-and-receipt)

3\. Verify message publication and receipt

You'll notice that the publisher sends the message and prints: _Published [msg.test] : 'NATS MESSAGE'_.

The subscriber receives the message and prints: _[#1] Received on [msg.test]: 'NATS MESSAGE'_.

If the receiver does not get the message, you'll need to check if you are using the same subject name for the publisher and the subscriber.

#### 

[hashtag](#id-4.-try-publishing-another-message)

4\. Try publishing another message

Copy

```

    nats pub msg.test "NATS MESSAGE 2"

```

You'll notice that the subscriber receives the message. Note that a message count is incremented each time your subscribing client receives a message on that subject.

#### 

[hashtag](#id-5.-create-subscriber-2)

5\. Create Subscriber 2

In a new shell or command prompt, start a new NATS subscriber.

Copy

```

    nats sub msg.test

```

#### 

[hashtag](#id-6.-publish-another-message-using-the-publisher-client)

6\. Publish another message using the publisher client

Copy

```

    nats pub msg.test "NATS MESSAGE 3"

```

Verify that both subscribing clients receive the message.

#### 

[hashtag](#id-7.-create-subscriber-3)

7\. Create Subscriber 3

In a new shell or command prompt session, create a new subscriber that listens on a different subject.

Copy

```

    nats sub msg.test.new

```

#### 

[hashtag](#id-8.-publish-another-message)

8\. Publish another message

Copy

```

    nats pub msg.test "NATS MESSAGE 4"

```

Subscriber 1 and Subscriber 2 receive the message, but Subscriber 3 does not. Why? Because Subscriber 3 is not listening on the message subject used by the publisher.

#### 

[hashtag](#id-9.-alter-subscriber-3-to-use-a-wildcard)

9\. Alter Subscriber 3 to use a wildcard

Change the last subscriber to listen on msg.* and run it:

Copy

```

    nats sub msg.*

```

Note: NATS supports the use of wildcard characters for message subscribers only. You cannot publish a message using a wildcard subject.

#### 

[hashtag](#id-10.-publish-another-message)

10\. Publish another message

Copy

```

    nats pub msg.test "NATS MESSAGE 5"

```

This time, all three subscribing clients should receive the message.

Do try out a few more variations of substrings and wildcards to test your understanding.

## 

[hashtag](#see-also)

See Also

Publish-subscribe pattern with the NATS CLI

Publish-subscribe pattern - NATS CLI

[PreviousPublish-Subscribechevron-left](https://docs.nats.io/nats-concepts/core-nats/pubsub) ([local](./../pubsub.md))[NextRequest-Replychevron-right](https://docs.nats.io/nats-concepts/core-nats/reqreply) ([local](./../reqreply.md))

Last updated 1 year ago

Was this helpful?
