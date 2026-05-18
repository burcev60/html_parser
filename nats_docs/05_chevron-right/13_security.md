---
title: Security
source: https://docs.nats.io/nats-concepts/security
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/security.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../_unsorted/nats-concepts.md))

# Security

NATS has a lot of security features:

  * Connections can be [_encrypted_ with TLS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/tls.md))

  * Client connections can be [_authenticated_](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/auth-intro.md)) in many ways:

    * [Token Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/auth-intro/tokens.md))

    * [Username/Password credentials](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/auth-intro/username-password.md))

    * [TLS Certificate](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/auth-intro/tls-mutual-auth.md))

    * [NKEY with Challenge](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/auth-intro/nkey-auth.md))

    * [Decentralized JWT Authentication/Authorization](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt) ([local](./../14_hashtag-guided-tour/06_zero-trust-security.md))

    * You can also integrate NATS with your existing authentication/authorization system or create your own custom authentication using the [Auth callout](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/auth-callout.md))

  * Authenticated clients are identified as users and have a set of [_authorizations_](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/authorization.md))

You can use [accounts](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/accounts) ([local](./../_unsorted/running-a-nats-service/configuration/securing-nats/accounts.md)) for multi-tenancy: each account has its own independent 'subject namespace' and you control the import/export of both streams of messages and services between accounts, and any number of users that client applications can be authenticated as. The subjects or subject wildcards that a user is allowed to publish and/or subscribe to can be controlled either through server configuration or as part of signed JWTs.

JWT authentication/authorization administration is decentralized because each account private key holder can manage their users and their authorizations on their own, without the need for any configuration change on the NATS servers by minting their own JWTs and distributing them to the users. There is no need for the NATS server to ever store any user private keys as they only need to validate the signature chain of trust contained in the user JWT presented by the client application to validate that they have the proper public key for that user.

The JetStream persistence layer of NATS also provides [encryption at rest](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/encryption_at_rest) ([local](./../_unsorted/running-a-nats-service/nats-admin/jetstream-admin/encryption-at-rest.md)).

[PreviousNATS Adaptive Deployment Architectureschevron-left](https://docs.nats.io/nats-concepts/service_infrastructure/adaptive_edge_deployment) ([local](./../14_hashtag-guided-tour/05_deployment-strategies.md))[NextConnectivitychevron-right](https://docs.nats.io/nats-concepts/connectivity) ([local](./14_connectivity.md))

Last updated 2 years ago

Was this helpful?
