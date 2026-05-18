---
title: Authentication Timeout
source: https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/auth_timeout
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/securing_nats/auth_intro/auth_timeout.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Securing NATS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats) ([local](./../../securing-nats.md))chevron-right
  4. [Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) ([local](./../auth-intro.md))

# Authentication Timeout

You can specify a timeout to limit how long the server will wait for a client to authenticate.

If you don't specify a value, or if you specify the value "0", then the default will be 1 second more than the `tls_timeout`.

If you do specify an invalid value, it will use a default of 1 second.

If a client doesn't authenticate to the server within the specified time, the server disconnects the server to prevent abuses.

Timeouts are specified in seconds (and can be fractional). Unlike `tls_timeout`, you cannot use "human readable" values like `10s`, you must specify a number, which will be interpreted as seconds. `10` will be 10 seconds, `3.5` will be 3 seconds and 500 milliseconds, etc.

As with TLS timeouts, long timeouts can be an opportunity for abuse. If setting the authentication timeout, it is important to note that it should be longer than the `tls timeout` option, as the authentication timeout includes the TLS upgrade time.

Copy

```

    authorization: {
        timeout: 3
        users: [
            {user: a, password b},
            {user: b, password a}
        ]
    }

```

[PreviousNKeyschevron-left](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth) ([local](./nkey-auth.md))[NextDecentralized JWT Authentication/Authorizationchevron-right](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt) ([local](./../../../../../14_hashtag-guided-tour/06_zero-trust-security.md))

Last updated 1 year ago

Was this helpful?
