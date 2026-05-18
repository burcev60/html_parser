---
title: OCSP Stapling
source: https://docs.nats.io/running-a-nats-service/configuration/securing_nats/ocsp
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/ocsp.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Securing NATS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats) ([local](./../securing-nats.md))

# OCSP Stapling

 _Supported since NATS Server version 2.3_

[OCSP Staplingarrow-up-right](https://en.wikipedia.org/wiki/OCSP_stapling) is honored by default for certificates that have the [status_request Must-Staple flagarrow-up-right](https://datatracker.ietf.org/doc/html/rfc6961).

When a certificate is configured with OCSP Must-Staple, the NATS Server will fetch staples from the configured OCSP responder URL that is present in a certificate. For example, given a certificate with the following configuration:

Copy

```

    [ ext_ca ]
    ...                                                                           
    authorityInfoAccess = OCSP;URI:http://ocsp.example.net:80
    tlsfeature = status_request
    ...

```

The NATS server will make a request to the OCSP responder to fetch a new staple which will then be presented to any TLS connection that is accepted by the server during the TLS handshake.

OCSP Stapling can be explicitly enabled or disabled in the NATS Server by setting the following flag in the NATS configuration file at the top-level:

Copy

```

    ocsp: false

```

**Note** : When OCSP Stapling is disabled, the NATS Server will not request staples even if the certificate has the Must-Staple flag.

## 

[hashtag](#advanced-configuration)

Advanced Configuration

By default, the NATS Server will be running in OCSP `auto` mode. In this mode the server will only fetch staples when the Must-Staple flag is configured in the certificate.

There are other OCSP modes that control the behavior as to whether OCSP should be enforced and the server should shutdown if the certificate runs with a revoked staple:

Mode

Description

Server shutdowns when revoked

auto

Enables OCSP Stapling when the certificate has the must staple/status_request flag

No

must

Enables OCSP Staping when the certificate has the must staple/status_request flag

Yes

always

Enables OCSP Stapling for all certificates

Yes

never

Disables OCSP Stapling even if must staple flag is present (same as `ocsp: false`)

No

For example, in the following OCSP configuration, the mode is set to `must`. This means that staples will be fetched only for certificates that have the Must-Staple flag enabled as well, but in case of revocation the server will shutdown rather than run with a revoked staple. In this configuration, the `url` will also override the OCSP responder URL that may have been configured in the certificate.

Copy

```

    ocsp {
      mode: must
      url: "http://ocsp.example.net"
    }

```

If staples are always required, regardless of the configuration of the certificate, you can enforce the behavior as follows:

Copy

```

    ocsp {
      mode: always
      url: "http://ocsp.example.net"
    }

```

## 

[hashtag](#caching-of-staples)

Caching of Staples

When a `store_dir` is configured in the NATS Server, the directory will be used to cache staples on disk to allow the server to resume in case of restarts without having to make another request to the OCSP responder if the staple is still valid.

Copy

```

    ocsp: true
    
    store_dir: "/path/to/store/dir"
    
    tls {
        cert_file: "configs/certs/ocsp/server-status-request-url.pem"
        key_file: "configs/certs/ocsp/server-status-request-url-key.pem"
        ca_file: "configs/certs/ocsp/ca-cert.pem"
        timeout: 5
    }

```

If JetStream is enabled, then the same `store_dir` will be reused and disk caching will be automatically enabled.

[PreviousMulti Tenancy using Accountschevron-left](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/accounts) ([local](./accounts.md))[NextAuth Calloutchevron-right](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout) ([local](./auth-callout.md))

Last updated 4 years ago

Was this helpful?
