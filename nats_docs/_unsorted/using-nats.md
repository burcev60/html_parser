---
title: NATS Tools
source: https://docs.nats.io/using-nats
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/nats-tools/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. Using NATS

# NATS Tools

## 

[hashtag](#using-nats-from-client-application)

Using NATS from client application

The most common form of connecting to the NATS messaging system will be through an application built with any of the [40+ client libraries](https://docs.nats.io/using-nats/developer) ([local](./../07_chevron-right/03_developing-with-nats-chevron-right.md)) available for NATS.

The client application will connect to an instance of the NATS server, be it a single server, a cluster of servers or even a global super-cluster such as [Synadia Cloudarrow-up-right](https://www.synadia.com/cloud?utm_source=nats_docs&utm_medium=nats), sending and receiving messages via a range of subscribers contracts. If the application is written in GoLang the NATS server can even be [embedded into a Goarrow-up-right](https://dev.to/karanpratapsingh/embedding-nats-in-go-19o) application.

Client APIs will also allow access to almost all server configuration tasks when using an account with sufficient permissions.

## 

[hashtag](#command-line-tooling)

Command Line Tooling

Besides using the client API to manage NATS servers, the NATS ecosystem also has many tools to interact with other applications and services over NATS and streams, support server configuration, enhance monitoring or tune performance such as:

  * General interaction and management

    * [nats](https://docs.nats.io/using-nats/nats-tools/nats_cli) ([local](./using-nats/nats-tools/nats-cli.md)) \- The `nats` Command Line Tool is the easiest way to interact with, test and manage NATS and JetStream from a terminal or from scripts. It's list of features are ever growing, so please download the [latest versionarrow-up-right](https://github.com/nats-io/natscli/releases).

  * Security

    * [nk](https://docs.nats.io/using-nats/nats-tools/nk) ([local](./using-nats/nats-tools/nk.md)) \- Generate NKeys for use with JSon Web Tokens (JWT) used with nsc

    * [nsc](https://docs.nats.io/using-nats/nats-tools/nsc) ([local](./using-nats/nats-tools/nsc.md)) \- Configure Operators, Accounts, Users and permission offline to later push them to a production server. This is the preferred tools to create security configuration unless you are using [Synadia Control Planearrow-up-right](https://www.docs.synadia.com/platform/control-plane?utm_source=nats_docs&utm_medium=nats)

    * [nats account serverarrow-up-right](https://nats-io.gitbook.io/legacy-nats-docs/nats-account-server) \- (**legacy, replaced by the built-in NATS resolver**) a custom security server. NAS can still be used as a reference implementation for you tailor-made security integration.

  * Monitoring

    * [nats top](https://docs.nats.io/using-nats/nats-tools/nats_top) ([local](./using-nats/nats-tools/nats-top.md)) \- Monitor NATS Servers

    * [prometheus-nats-exporterarrow-up-right](https://github.com/nats-io/prometheus-nats-exporter) \- Export NATS server metrics to [Prometheusarrow-up-right](https://prometheus.io/) and a [Grafanaarrow-up-right](https://grafana.com) dashboard.

  * Benchmarking

    * see [nats bench](https://docs.nats.io/using-nats/nats-tools/nats_cli/natsbench) ([local](./using-nats/nats-tools/nats-cli/natsbench.md)) subcommand of the [nats](https://docs.nats.io/using-nats/nats-tools/nats_cli) ([local](./using-nats/nats-tools/nats-cli.md)) tool

[PreviousConnectivitychevron-left](https://docs.nats.io/nats-concepts/connectivity) ([local](./../05_chevron-right/14_connectivity.md))[Nextnatschevron-right](https://docs.nats.io/using-nats/nats-tools/nats_cli) ([local](./using-nats/nats-tools/nats-cli.md))

Last updated 1 year ago

Was this helpful?
