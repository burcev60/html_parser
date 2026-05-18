---
title: TLS Authentication in clusters
source: https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth/cluster_tls
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/clustering/cluster_tls.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Securing NATS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats) ([local](./../../../securing-nats.md))chevron-right
  4. [Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) ([local](./../../auth-intro.md))chevron-right
  5. [TLS Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth) ([local](./../tls-mutual-auth.md))

# TLS Authentication in clusters

When setting up clusters, all servers in the cluster, if using TLS, will both verify the connecting endpoints and the server responses. So certificates are checked in [both directions](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls#wrong-key-usage) ([local](./../../tls.md#wrong-key-usage)). Certificates can be configured only for the server's cluster identity, keeping client and server certificates separate from cluster formation.

TLS Mutual Authentication _is the only way_ of securing routes.

Copy

```

    cluster {
      listen: 127.0.0.1:4244
    
      tls {
        # Route cert
        cert_file: "./configs/certs/srva-cert.pem"
        # Private key
        key_file:  "./configs/certs/srva-key.pem"
        # Optional certificate authority verifying connected routes
        # Required when we have self-signed CA, etc.
        ca_file:   "./configs/certs/ca.pem"
      }
      # Routes are actively solicited and connected to from this server.
      # Other servers can connect to us if they supply the correct credentials
      # in their routes definitions from above.
      routes = [
        nats://127.0.0.1:4246
      ]
    }

```

[PreviousTLS Authenticationchevron-left](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth) ([local](./../tls-mutual-auth.md))[NextNKeyschevron-right](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth) ([local](./../nkey-auth.md))

Last updated 3 years ago

Was this helpful?
