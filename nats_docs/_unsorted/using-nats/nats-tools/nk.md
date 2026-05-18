---
title: nk
source: https://docs.nats.io/using-nats/nats-tools/nk
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/nats-tools/nk.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../using-nats.md))chevron-right
  2. [NATS Tools](https://docs.nats.io/using-nats/nats-tools) ([local](./../../../07_chevron-right/01_nats-tools-chevron-right.md))

# nk

`nk` is a command line tool that generates `nkeys`. NKeys are a highly secure public-key signature system based on [Ed25519arrow-up-right](https://ed25519.cr.yp.to/).

With NKeys the server can verify identity without ever storing secrets on the server. The authentication system works by requiring a connecting client to provide its public key and digitally sign a challenge with its private key. The server generates a random challenge with every connection request, making it immune to playback attacks. The generated signature is validated a public key, thus proving the identity of the client. If the public key validation succeeds, authentication succeeds.

> NKey is an awesome replacement for token authentication, because a connecting client will have to prove it controls the private key for the authorized public key.

## 

[hashtag](#installing-nk)

Installing nk

To get started with NKeys, you’ll need the `nk` tool from <https://github.com/nats-io/nkeys/tree/master/nk>[arrow-up-right](https://github.com/nats-io/nkeys/tree/master/nk) repository. If you have _go_ installed, enter the following at a command prompt:

Copy

```

    go install github.com/nats-io/nkeys/nk@latest

```

## 

[hashtag](#generating-nkeys-and-configuring-the-server)

Generating NKeys and Configuring the Server

To generate a _User_ NKEY:

Copy

```

    nk -gen user -pubout

```

Copy

```

    SUACSSL3UAHUDXKFSNVUZRF5UHPMWZ6BFDTJ7M6USDXIEDNPPQYYYCU3VY
    UDXU4RCSJNZOIQHZNWXHXORDPRTGNJAHAHFRGZNEEJCPQTT2M7NLCNF4

```

The first output line starts with the letter `S` for _Seed_. The second letter `U` stands for _User_. Seeds are private keys; you should treat them as secrets and guard them with care.

The second line starts with the letter `U` for _User_ , and is a public key which can be safely shared.

To use `nkey` authentication, add a user, and set the `nkey` property to the public key of the user you want to authenticate. You are only required to use the public key and no other properties are required. Here is a snippet of configuration for the `nats-server`:

Copy

```

    authorization: {
      users: [
        { nkey: UDXU4RCSJNZOIQHZNWXHXORDPRTGNJAHAHFRGZNEEJCPQTT2M7NLCNF4 }
      ]
    }

```

To complete the end-to-end configuration and use an `nkey`, the [client is configuredarrow-up-right](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth#client-configuration) ([local](./../../running-a-nats-service/configuration/securing-nats/auth-intro/nkey-auth.md#client-configuration)) to use the seed, which is the private key.

[Previousnats benchchevron-left](https://docs.nats.io/using-nats/nats-tools/nats_cli/natsbench) ([local](./nats-cli/natsbench.md))[Nextnscchevron-right](https://docs.nats.io/using-nats/nats-tools/nsc) ([local](./nsc.md))

Last updated 2 years ago

Was this helpful?
