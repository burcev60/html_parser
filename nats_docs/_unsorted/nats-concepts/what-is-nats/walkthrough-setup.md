---
title: Walkthrough Setup
source: https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/what-is-nats/walkthrough_setup.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../nats-concepts.md))chevron-right
  2. [What is NATS](https://docs.nats.io/nats-concepts/what-is-nats) ([local](./../../../05_chevron-right/03_what-is-nats-chevron-right.md))

# Walkthrough Setup

We have provided Walkthroughs for you to try NATS (and JetStream) on your own. In order to follow along with the walkthroughs, you could choose one of these options:

  * The `nats` CLI tool must be installed, and a local NATS server must be installed (or you can use a remote server you have access to).

  * You can use Synadia's NGS.

  * You could even use the demo server from where you installed NATS. This is accessible via `nats://demo.nats.io` (this is a NATS connection URL; not a browser URL. You pass it to a NATS client application).

## 

[hashtag](#installing-the-nats-cli-tool)

Installing the [`nats`](https://docs.nats.io/using-nats/nats-tools/nats_cli) ([local](./../../using-nats/nats-tools/nats-cli.md)) CLI Tool

Please refer to the [installation section in the readmearrow-up-right](https://github.com/nats-io/natscli?tab=readme-ov-file#installation).

## 

[hashtag](#installing-the-nats-server-locally-if-needed)

Installing the NATS server locally (if needed)

If you are going to run a server locally you need to first install it and start it. Please refer to the [nats server installation doc](https://docs.nats.io/running-a-nats-service/introduction/installation) ([local](./../../running-a-nats-service/introduction/installation.md))

Alternatively if you already know how to use NATS on a remote server, you only need to pass the server URL to `nats` using the `-s` option or preferably create a context using `nats context add`, to specify the server URL(s) and credentials file containing your user JWT.

### 

[hashtag](#start-the-nats-server-if-needed)

Start the NATS server (if needed)

To start a simple demonstration server locally, simply run:

Copy

```

    nats-server

```

(or `nats-server -m 8222` if you want to enable the HTTP monitoring functionality)

When the server starts successfully, you will see the following messages:

Copy

```

    [14524] 2021/10/25 22:53:53.525530 [INF] Starting nats-server
    [14524] 2021/10/25 22:53:53.525640 [INF]   Version:  2.6.1
    [14524] 2021/10/25 22:53:53.525643 [INF]   Git:      [not set]
    [14524] 2021/10/25 22:53:53.525647 [INF]   Name:     NDAUZCA4GR3FPBX4IFLBS4VLAETC5Y4PJQCF6APTYXXUZ3KAPBYXLACC
    [14524] 2021/10/25 22:53:53.525650 [INF]   ID:       NDAUZCA4GR3FPBX4IFLBS4VLAETC5Y4PJQCF6APTYXXUZ3KAPBYXLACC
    [14524] 2021/10/25 22:53:53.526392 [INF] Starting http monitor on 0.0.0.0:8222
    [14524] 2021/10/25 22:53:53.526445 [INF] Listening for client connections on 0.0.0.0:4222
    [14524] 2021/10/25 22:53:53.526684 [INF] Server is ready

```

The NATS server listens for client connections on TCP Port 4222.

[PreviousWhat is NATSchevron-left](https://docs.nats.io/nats-concepts/what-is-nats) ([local](./../../../05_chevron-right/03_what-is-nats-chevron-right.md))[NextSubject-Based Messagingchevron-right](https://docs.nats.io/nats-concepts/subjects) ([local](./../../../05_chevron-right/05_subject-based-messaging.md))

Last updated 1 year ago

Was this helpful?
