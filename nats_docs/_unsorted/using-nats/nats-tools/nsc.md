---
title: nsc
source: https://docs.nats.io/using-nats/nats-tools/nsc
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/nats-tools/nsc/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../using-nats.md))chevron-right
  2. [NATS Tools](https://docs.nats.io/using-nats/nats-tools) ([local](./../../../07_chevron-right/01_nats-tools-chevron-right.md))

# nsc

NATS account configurations are built using the `nsc` tool. The NSC tool allows you to:

  * Create and edit Operators, Accounts, Users

  * Manage publish and subscribe permissions for Users

  * Define Service and Stream exports from an account

  * Reference Service and Streams from another account

  * Generate Activation tokens that grants access to a private service or stream

  * Generate User credential files

  * Describe Operators, Accounts, Users, and Activations

  * Push and pull account JWTs to an account JWTs server

## 

[hashtag](#installation)

Installation

Installing `nsc` is easy:

Copy

```

    curl -L https://raw.githubusercontent.com/nats-io/nsc/master/install.py | python

```

> Additional ways of installing nsc are described at [nsc's github repositoryarrow-up-right](https://github.com/nats-io/nsc#install)

The script will download the latest version of `nsc` and install it into your system.

In case NSC is not initialized already do `nsc init`

Output of `tree -L 2 nsc/`

Copy

```

    nsc/
    ├── accounts
    │   ├── nats
    │   └── nsc.json
    └── nkeys
        ├── creds
        └── keys
    5 directories, 1 file

```

**IMPORTANT** : `nsc` version 2.2.0 has been released. This version of nsc only supports `nats-server` v2.2.0 and `nats-account-server` v1.0.0. For more information please refer to the [nsc 2.2.0 release notesarrow-up-right](https://github.com/nats-io/nsc/releases/tag/2.2.0).

## 

[hashtag](#tutorials)

Tutorials

You can find various task-oriented tutorials to working with the tool here:

  * [Basic Usage](https://docs.nats.io/using-nats/nats-tools/nsc/basics) ([local](./nsc/basics.md))

  * [Configuring Account Streams Import/Export](https://docs.nats.io/using-nats/nats-tools/nsc/streams) ([local](./nsc/streams.md))

  * [Configuring Account Services Import/Export](https://docs.nats.io/using-nats/nats-tools/nsc/services) ([local](./nsc/services.md))

  * [Signing Keys](https://docs.nats.io/using-nats/nats-tools/nsc/signing_keys) ([local](./nsc/signing-keys.md))

  * [Revoking Users or Activations](https://docs.nats.io/using-nats/nats-tools/nsc/revocation) ([local](./nsc/revocation.md))

  * [Working with Managed Operators](https://docs.nats.io/using-nats/nats-tools/nsc/managed) ([local](./nsc/managed.md))

## 

[hashtag](#tool-documentation)

Tool Documentation

For more specific browsing of the tool syntax, check out the `nsc` tool documentation. It can be found within the tool itself:

Copy

```

    nsc help

```

Or an online version [herearrow-up-right](https://nats-io.github.io/nsc).

[Previousnkchevron-left](https://docs.nats.io/using-nats/nats-tools/nk) ([local](./nk.md))[NextBasicschevron-right](https://docs.nats.io/using-nats/nats-tools/nsc/basics) ([local](./nsc/basics.md))

Last updated 3 years ago

Was this helpful?
