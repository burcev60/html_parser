---
title: Flags
source: https://docs.nats.io/running-a-nats-service/introduction/flags
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/running/flags.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Installing, running and deploying a NATS Server](https://docs.nats.io/running-a-nats-service/introduction) ([local](./../../../09_chevron-right/01_installing-running-and-deploying-a-nats-server-chevron-right.md))

# Flags

The NATS server has many flags to customize its behavior without having to write a configuration file.

The configuration flags revolve around:

  * Server Options

  * Logging

  * Authorization

  * TLS Security

  * Clustering

  * Information

## 

[hashtag](#server-options)

Server Options

Flag

Description

`-a`, `--addr`, `--net`

Host address to bind to (default: `0.0.0.0` \- all interfaces).

`-p`, `--port`

NATS client port (default: 4222).

`-n`, `--name`, `--server_name`

Server name (default auto).

`-P`, `--pid`

File to store the process ID (PID).

`-m`, `--http_port`

HTTP port for monitoring dashboard (exclusive of `--https_port`).

`-ms`, `--https_port`

HTTPS port monitoring for monitoring dashboard (exclusive of `--http_port`).

`-c`, `--config`

Path to NATS server configuration file.

`-sl`, `--signal`

Send a signal to nats-server process. See [process signaling](https://docs.nats.io/running-a-nats-service/nats_admin/signals) ([local](./../nats-admin/signals.md)).

`--client_advertise`

Client HostPort to advertise to other servers.

`-t`

Test configuration and exit

`--ports_file_dir

Creates a ports file in the specified directory (<executable_name>_.ports).

## 

[hashtag](#jetstream-options)

JetStream Options

Flag

Description

`-js`, `--jetstream`

Enable JetStream functionality.

`-sd`, `--store_dir`

Set the storage directory.

## 

[hashtag](#authentication-options)

Authentication Options

The following options control straightforward authentication:

Flag

Description

`--user`

Required _username_ for connections (exclusive of `--auth`).

`--pass`

Required _password_ for connections (exclusive of `--auth`).

`--auth`

Required _authorization token_ for connections (exclusive of `--user` and `--password`).

See [token authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens) ([local](./../configuration/securing-nats/auth-intro/tokens.md)), and [username/password](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) ([local](./../configuration/securing-nats/auth-intro/username-password.md)) for more information.

## 

[hashtag](#logging-options)

Logging Options

The following flags are available on the server to configure logging:

Flag

Description

`-l`, `--log`

File to redirect log output

`-T`, `--logtime`

Specify `-T=false` to disable timestamping log entries

`-s`, `--syslog`

Log to syslog or windows event log

`-r`, `--remote_syslog`

The syslog server address, like `udp://localhost:514`

`-D`, `--debug`

Enable debugging output

`-V`, `--trace`

Enable protocol trace log messages

`-VV`

Verbose trace (traces system account as well)

`-DV`

Enable both debug and protocol trace messages

`-DVV`

Debug and verbose trace (traces system account as well)

`--max_traced_msg_len`

Maximum printable length for traced messages. 0 for unlimited

`--max_traced_msg_len`

Maximum printable length for traced messages (default: unlimited)

You can read more about [logging configuration here](https://docs.nats.io/running-a-nats-service/configuration/logging) ([local](./../configuration/logging.md)).

## 

[hashtag](#tls-options)

TLS Options

Flag

Description

`--tls`

Enable TLS, do not verify clients

`--tlscert`

Server certificate file

`--tlskey`

Private key for server certificate

`--tlsverify`

Enable client TLS certificate verification

`--tlscacert`

Client certificate CA for verification

You can read more about [tls configuration here](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls) ([local](./../configuration/securing-nats/tls.md)).

## 

[hashtag](#cluster-options)

Cluster Options

The following flags are available on the server to configure clustering:

Flag

Description

`--routes`

Comma-separated list of cluster URLs to solicit and connect

`--cluster`

Cluster URL for clustering requests

`--no_advertise`

Do not advertise known cluster information to clients

`--cluster_advertise`

Cluster URL to advertise to other servers

`--connect_retries`

For implicit routes, number of connect retries

`--cluster_listen`

Cluster url from which members can solicit routes

You can read more about [clustering configuration here](https://docs.nats.io/running-a-nats-service/configuration/clustering) ([local](./../configuration/clustering.md)).

## 

[hashtag](#common-options)

Common Options

Flag

Description

`-h`, `--help`

Show this message

`-v`, `--version`

Show version

`--help_tls`

TLS help

[PreviousWindows Servicechevron-left](https://docs.nats.io/running-a-nats-service/introduction/windows_srv) ([local](./windows-srv.md))[NextEnvironmental considerationschevron-right](https://docs.nats.io/running-a-nats-service/environment) ([local](./../../../09_chevron-right/03_environmental-considerations.md))

Last updated 1 year ago

Was this helpful?
