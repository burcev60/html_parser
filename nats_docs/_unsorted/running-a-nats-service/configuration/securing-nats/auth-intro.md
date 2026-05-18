---
title: Authentication
source: https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/securing_nats/auth_intro/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Securing NATS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats) ([local](./../securing-nats.md))

# Authentication

NATS authentication is multi-level. All of the security modes have an _accounts_ level with [_users_](#user-configuration-map) belonging to those accounts. The decentralized JWT Authentication also has an _operator_ to which the accounts belong.

Each account has its own independent subject namespace: a message published on subject 'foo' in one account will not be seen by subscribers to 'foo' in other accounts. Accounts can however define exports and imports of subject(s) streams as well as expose request-reply services between accounts. Users within an account will share the same subject namespace but can be restricted to only be able to publish-subscribe to specific subjects.

## 

[hashtag](#authentication-methods)

Authentication Methods

The NATS server provides various ways of authenticating clients:

  * [Token Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens) ([local](./auth-intro/tokens.md))

  * [Plain Text Username/Password credentials](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password#plain-text-passwords) ([local](./auth-intro/username-password.md#plain-text-passwords))

  * [Bcrypted Username/Password credentials](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password#bcrypted-passwords) ([local](./auth-intro/username-password.md#bcrypted-passwords))

  * [TLS Certificate](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth) ([local](./auth-intro/tls-mutual-auth.md))

  * [NKEY with Challenge](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth) ([local](./auth-intro/nkey-auth.md))

  * [Decentralized JWT Authentication/Authorization](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt) ([local](./../../../../14_hashtag-guided-tour/06_zero-trust-security.md))

Authentication deals with allowing a NATS client to connect to the server. Except for JWT authentication, authentication and authorization are configured in the `authorization` section of the configuration. With JWT authentication the account and user information are stored in the [resolver](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt/resolver) ([local](./auth-intro/jwt/resolver.md)) rather than in the server configuration file.

## 

[hashtag](#authorization-map)

Authorization Map

The `authorization` block provides _authentication_ configuration as well as [_authorization_](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization) ([local](./authorization.md)) :

Property

Description

[`token`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens) ([local](./auth-intro/tokens.md))

Specifies a global token that can be used to authenticate to the server (exclusive of user and password)

[`user`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password#single-user) ([local](./auth-intro/username-password.md#single-user))

Specifies a single _global_ user name for clients to the server (exclusive of token)

[`password`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) ([local](./auth-intro/username-password.md))

Specifies a single _global_ password for clients to the server (exclusive of `token`)

[`users`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password#multiple-users) ([local](./auth-intro/username-password.md#multiple-users))

A list of [user configuration](#user-configuration-map) maps. For multiple username and password credentials, specify a `users` list.

[`timeout`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/auth_timeout) ([local](./auth-intro/auth-timeout.md))

Maximum number of seconds to wait for client authentication

[`auth_callout`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout) ([local](./auth-callout.md))

Enables the auth callout extension

## 

[hashtag](#user-configuration-map)

User Configuration Map

A `user` configuration map specifies credentials and permissions options for a single user:

Property

Description

[`user`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) ([local](./auth-intro/username-password.md))

username for client authentication. (Can also be a user for [tls authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth#mapping-client-certificates-to-a-user) ([local](./auth-intro/tls-mutual-auth.md#mapping-client-certificates-to-a-user)))

[`password`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) ([local](./auth-intro/username-password.md))

password for the user entry

[`nkey`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth) ([local](./auth-intro/nkey-auth.md))

public nkey identifying an user

[`permissions`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization) ([local](./authorization.md))

permissions map configuring subjects accessible to the user

[PreviousEnabling TLSchevron-left](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls) ([local](./tls.md))[NextTokenschevron-right](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens) ([local](./auth-intro/tokens.md))

Last updated 2 years ago

Was this helpful?
