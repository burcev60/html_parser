---
title: Managing and Monitoring your NATS Server Infrastructure
source: https://docs.nats.io/running-a-nats-service/nats_admin
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../_unsorted/running-a-nats-service.md))

# Managing and Monitoring your NATS Server Infrastructure

Managing a NATS Server is simple, typical lifecycle operations include:

  * Using the [`nats`](https://docs.nats.io/using-nats/nats-tools/nats_cli) ([local](./../_unsorted/using-nats/nats-tools/nats-cli.md)) CLI tool to check server cluster connectivity and latencies, as well as get account information, and manage and interact with streams (and other NATS applications). Try the following examples to learn about the most common ways to use `nats`.

    * `nats cheat`

    * `nats cheat server`

    * `nats stream --help` to monitor, manage and interact with streams

    * `nats consumer --help` to monitor, manage stream consumers

    * `nats context --help` if you need to switch between servers, clusters or user credentials

  * Using the [`nsc`](https://docs.nats.io/using-nats/nats-tools/nsc) ([local](./../_unsorted/using-nats/nats-tools/nsc.md)) CLI tool when using JWT based authentication and authorization, to create, revoke operators, accounts, and user (i.e. client applications) JWTs and keys.

  * [Sending signals](https://docs.nats.io/running-a-nats-service/nats_admin/signals) ([local](./../_unsorted/running-a-nats-service/nats-admin/signals.md)) to a server to reload a configuration or rotate log files

  * [Upgrading](https://docs.nats.io/running-a-nats-service/nats_admin/upgrading_cluster) ([local](./../_unsorted/running-a-nats-service/nats-admin/upgrading-cluster.md)) a server (or cluster)

  * Understanding [slow consumers](https://docs.nats.io/running-a-nats-service/nats_admin/slow_consumers) ([local](./../_unsorted/running-a-nats-service/nats-admin/slow-consumers.md))

  * Monitoring the server via:

    * The monitoring [endpoint](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring) ([local](./../_unsorted/running-a-nats-service/nats-admin/monitoring.md)) and tools like [nats-top](https://docs.nats.io/using-nats/nats-tools/nats_top) ([local](./../_unsorted/using-nats/nats-tools/nats-top.md))

    * By subscribing to [system events](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts) ([local](./../_unsorted/running-a-nats-service/configuration/sys-accounts.md))

      * Commerical option for high-cardinality monitoring via the system account: [Synadia Insightsarrow-up-right](https://www.synadia.com/insights)

  * Gracefully shut down a server with [Lame Duck Mode](https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode) ([local](./../_unsorted/running-a-nats-service/nats-admin/lame-duck-mode.md))

[PreviousConfigurationchevron-left](https://docs.nats.io/running-a-nats-service/configuration/websocket/websocket_conf) ([local](./../_unsorted/running-a-nats-service/configuration/websocket/websocket-conf.md))[NextMonitoringchevron-right](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring) ([local](./../_unsorted/running-a-nats-service/nats-admin/monitoring.md))

Last updated 11 days ago

Was this helpful?
