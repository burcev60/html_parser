---
title: Username/Password
source: https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/securing_nats/auth_intro/username_password.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Securing NATS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats) ([local](./../../securing-nats.md))chevron-right
  4. [Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) ([local](./../auth-intro.md))

# Username/Password

## 

[hashtag](#plain-text-passwords)

Plain Text Passwords

You can authenticate one or more clients using username and passwords; this enables you to have greater control over the management and issuance of credential secrets.

## 

[hashtag](#single-user)

Single User

Copy

```

    authorization: {
        user: a,
        password: b
    }

```

You can also specify a single username/password by:

Copy

```

    > nats-server --user a --pass b

```

## 

[hashtag](#multiple-users)

Multiple users

Copy

```

    authorization: {
        users: [
            {user: a, password: b},
            {user: b, password: a}
        ]
    }

```

## 

[hashtag](#bcrypted-passwords)

Bcrypted Passwords

Username/password also supports bcrypted passwords using the [`nats`](https://docs.nats.io/using-nats/nats-tools/nats_cli) ([local](./../../../../using-nats/nats-tools/nats-cli.md)) tool. Simply replace the clear text password with the bcrypted entries:

Copy

```

    > nats server passwd
    ? Enter password [? for help] **********************
    ? Reenter password [? for help] **********************
    
    $2a$11$V1qrpBt8/SLfEBr4NJq4T.2mg8chx8.MTblUiTBOLV3MKDeAy.f7u

```

And on the configuration file:

Copy

```

    authorization: {
        users: [
            {user: a, password: "$2a$11$V1qrpBt8/SLfEBr4NJq4T.2mg8chx8.MTblUiTBOLV3MKDeAy.f7u"},
            ...
        ]
    }

```

## 

[hashtag](#reloading-a-configuration)

Reloading a Configuration

As you add/remove passwords from the server configuration file, you'll want your changes to take effect. To reload without restarting the server and disconnecting clients, do:

Copy

```

    > nats-server --signal reload

```

[PreviousTokenschevron-left](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens) ([local](./tokens.md))[NextTLS Authenticationchevron-right](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth) ([local](./tls-mutual-auth.md))

Last updated 3 years ago

Was this helpful?
