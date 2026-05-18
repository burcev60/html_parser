---
title: Tokens
source: https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/securing_nats/auth_intro/tokens.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Securing NATS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats) ([local](./../../securing-nats.md))chevron-right
  4. [Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) ([local](./../auth-intro.md))

# Tokens

Token authentication is a string that if provided by a client, allows it to connect. It is the most straightforward authentication provided by the NATS server.

To use token authentication, you can specify an `authorization` section with the `token` property set:

Copy

```

    authorization {
        token: "s3cr3t"
    }

```

Token authentication can be used in the authorization section for clients and clusters.

Or start the server with the `--auth` flag:

Copy

```

    nats-server --auth s3cr3t

```

A client can easily connect by specifying the server URL:

Copy

```

    nats sub -s nats://s3cr3t@localhost:4222 ">"

```

## 

[hashtag](#bcrypted-tokens)

Bcrypted Tokens

Tokens can be bcrypted enabling an additional layer of security, as the clear-text version of the token would not be persisted on the server configuration file.

You can generate bcrypted tokens and passwords using the [`nats`](https://docs.nats.io/using-nats/nats-tools/nats_cli) ([local](./../../../../using-nats/nats-tools/nats-cli.md)) tool:

Copy

```

    nats server passwd

```

Copy

```

    ? Enter password [? for help] **********************
    ? Reenter password [? for help] **********************
    
    $2a$11$PWIFAL8RsWyGI3jVZtO9Nu8.6jOxzxfZo7c/W0eLk017hjgUKWrhy

```

Here's a simple configuration file:

Copy

```

    authorization {
        token: "$2a$11$PWIFAL8RsWyGI3jVZtO9Nu8.6jOxzxfZo7c/W0eLk017hjgUKWrhy"
    }

```

The client will still require the clear-text token to connect:

Copy

```

    nats sub -s nats://dag0HTXl4RGg7dXdaJwbC8@localhost:4222 ">"

```

[PreviousAuthenticationchevron-left](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) ([local](./../auth-intro.md))[NextUsername/Passwordchevron-right](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) ([local](./username-password.md))

Last updated 4 years ago

Was this helpful?
