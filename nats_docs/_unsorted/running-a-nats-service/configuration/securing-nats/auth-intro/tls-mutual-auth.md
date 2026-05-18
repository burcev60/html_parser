---
title: TLS Authentication
source: https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Securing NATS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats) ([local](./../../securing-nats.md))chevron-right
  4. [Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) ([local](./../auth-intro.md))

# TLS Authentication

The server can require TLS certificates from a client. When needed, you can use the certificates to:

  * Validate the client certificate matches a known or trusted CA

  * Extract information from a trusted certificate to provide authentication

> Note: To simplify the common scenario of maintainers looking at the monitoring endpoint, `verify` and `verify_and_map` do not apply to the monitoring port.

The examples in the following sections make use of the certificates you [generated](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls#self-signed-certificates-for-testing) ([local](./../tls.md#self-signed-certificates-for-testing)) locally.

## 

[hashtag](#validating-a-client-certificate)

Validating a Client Certificate

The server can verify a client certificate using a CA certificate. To require verification, add the option `verify` to the TLS configuration section as follows:

Copy

```

    tls {
      cert_file: "server-cert.pem"
      key_file:  "server-key.pem"
      ca_file:   "rootCA.pem"
      verify:    true
    }

```

Or via the command line:

Copy

```

    nats-server --tlsverify --tlscert=server-cert.pem --tlskey=server-key.pem --tlscacert=rootCA.pem

```

This option verifies the client's certificate is signed by the CA specified in the `ca_file` option. When `ca_file` is not present it will default to CAs in the system trust store. It also makes sure that the client provides a certificate with the extended key usage `TLS Web Client Authentication`.

## 

[hashtag](#mapping-client-certificates-to-a-user)

Mapping Client Certificates To A User

In addition to verifying that a specified CA issued a client certificate, you can use information encoded in the certificate to authenticate a client. The client wouldn't have to provide or track usernames or passwords.

To have TLS Mutual Authentication map certificate attributes to the user's identity use `verify_and_map` as shown as follows:

Copy

```

    tls {
      cert_file: "server-cert.pem"
      key_file:  "server-key.pem"
      ca_file:   "rootCA.pem"
      # Require a client certificate and map user id from certificate
      verify_and_map: true
    }

```

> Note that `verify` was changed to `verify_and_map`.

When present, the server will check if a Subject Alternative Name (SAN) maps to a user. It will search all email addresses first, then all DNS names. If no user could be found, it will try the certificate subject.

> Note: This mechanism will pick the user it finds first. There is no configuration to restrict this.

Copy

```

    openssl x509 -noout -text -in  client-cert.pem

```

Copy

```

    Certificate:
    ...
            X509v3 extensions:
                X509v3 Subject Alternative Name:
                    DNS:localhost, IP Address:0:0:0:0:0:0:0:1, email:email@localhost
                X509v3 Extended Key Usage:
                    TLS Web Client Authentication
    ...

```

The configuration to authorize this user would be as follow:

Copy

```

    authorization {
      users = [
        {user: "email@localhost"}
      ]
    }

```

Use the [RFC 2253 Distinguished Namesarrow-up-right](https://tools.ietf.org/html/rfc2253) syntax to specify a user corresponding to the certificate subject:

Copy

```

    openssl x509 -noout -text -in client-cert.pem

```

Copy

```

    Certificate:
        Data:
    ...
            Subject: O=mkcert development certificate, OU=testuser@MacBook-Pro.local (Test User)
    ...

```

> Note that for this example to work you will have to modify the user to match what is in your certificates subject. In doing so, watch out for the order of attributes!

The configuration to authorize this user would be as follows:

Copy

```

    authorization {
      users = [
        {user: "OU=testuser@MacBook-Pro.local (Test User),O=mkcert development certificate"}
      ]
    }

```

## 

[hashtag](#tls-timeout)

TLS Timeout

[TLS timeout](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls#tls-timeout) ([local](./../tls.md#tls-timeout)) is described here.

[PreviousUsername/Passwordchevron-left](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) ([local](./username-password.md))[NextTLS Authentication in clusterschevron-right](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth/cluster_tls) ([local](./tls-mutual-auth/cluster-tls.md))

Last updated 4 years ago

Was this helpful?
