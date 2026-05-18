---
title: Request-Reply Walkthrough
source: https://docs.nats.io/nats-concepts/core-nats/reqreply/reqreply_walkthrough
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/core-nats/request-reply/reqreply_walkthrough.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../../nats-concepts.md))chevron-right
  2. [Core NATS](https://docs.nats.io/nats-concepts/core-nats) ([local](./../../../../05_chevron-right/06_core-nats-chevron-right.md))chevron-right
  3. [Request-Reply](https://docs.nats.io/nats-concepts/core-nats/reqreply) ([local](./../reqreply.md))

# Request-Reply Walkthrough

NATS supports [request-reply](https://docs.nats.io/nats-concepts/core-nats/reqreply) ([local](./../reqreply.md)) messaging. In this tutorial you explore how to exchange point-to-point messages using NATS.

## 

[hashtag](#prerequisites)

Prerequisites

If you have not already done so, you need to [install](https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup) ([local](./../../what-is-nats/walkthrough-setup.md)) the `nats` CLI Tool and optionally, the nats-server on your machine.

## 

[hashtag](#walkthrough)

Walkthrough

Start two terminal sessions. These will be used to run the NATS request and reply clients.

### 

[hashtag](#in-one-terminal-run-the-reply-client-listener)

In one terminal, run the reply client listener

Copy

```

    nats reply help.please 'OK, I CAN HELP!!!'

```

You should see the message: _Listening on [help.please]_

This means that the NATS receiver client is listening for request messages on the "help.please" subject. In NATS, the receiver is a subscriber.

### 

[hashtag](#in-the-other-terminal-run-the-request-client)

In the other terminal, run the request client

Copy

```

    nats request help.please 'I need help!'

```

The NATS requestor client makes a request by sending the message "I need help!" on the “help.please” subject.

The NATS receiver client receives the message, formulates the reply ("OK, I CAN HELP!!!"), and sends it to the inbox of the requester.

[PreviousRequest-Replychevron-left](https://docs.nats.io/nats-concepts/core-nats/reqreply) ([local](./../reqreply.md))[NextQueue Groupschevron-right](https://docs.nats.io/nats-concepts/core-nats/queue) ([local](./../queue.md))

Last updated 4 years ago

Was this helpful?
