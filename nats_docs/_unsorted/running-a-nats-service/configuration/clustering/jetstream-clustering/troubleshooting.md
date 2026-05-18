---
title: Troubleshooting
source: https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/troubleshooting
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/clustering/jetstream_clustering/troubleshooting.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Clustering](https://docs.nats.io/running-a-nats-service/configuration/clustering) ([local](./../../clustering.md))chevron-right
  4. [JetStream Clustering](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering) ([local](./../jetstream-clustering.md))

# Troubleshooting

Diagnosing problems in NATS JetStream clusters requires:

  * knowledge of [JetStream concepts](https://docs.nats.io/nats-concepts/jetstream) ([local](./../../../../../05_chevron-right/08_jetstream-chevron-right.md))

  * knowledge of the [NATS Command Line Interface (CLI)arrow-up-right](https://github.com/nats-io/natscli#the-nats-command-line-interface)

The following tips and commands (while not an exhaustive list) can be useful when diagnosing problems in NATS JetStream clusters:

## 

[hashtag](#troubleshooting-tips)

Troubleshooting tips

  1. Look at [nats-serverarrow-up-right](https://github.com/nats-io/nats-server) logs. By default, only warning and error logs are produced, but debug and trace logs can be turned on from the command line using `-D` and `-DV`, respectively. Alternatively, enabling `debug` or `trace` in the [server configarrow-up-right](https://docs.nats.io/running-a-nats-service/configuration#monitoring-and-tracing) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md#monitoring-and-tracing)).

  2. Make sure that in the [NATS JetStream configuration](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering#configuration) ([local](./../jetstream-clustering.md#configuration)), at least one system user is configured in this section: `{ $SYS { users } }`.

### 

[hashtag](#nats-account-commands)

`nats account` commands

Command

Description

[`nats account info`](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/account) ([local](./../../../nats-admin/jetstream-admin/account.md))

Verify that JetStream is enabled on account

### 

[hashtag](#basic-nats-server-commands)

Basic `nats server` commands

Command

Description

`nats server ls`

List known servers

`nats server ping`

Ping all servers

`nats server info`

Show information about a single server

[`nats server check`](https://docs.nats.io/running-a-nats-service/clients#testing-your-setup) ([local](./../../../../../09_chevron-right/07_nats-server-clients.md#testing-your-setup))

Health check for NATS servers

### 

[hashtag](#nats-server-report-commands)

`nats server report` commands

Command

Description

`nats server report connections`

Report on connections

`nats server report accounts`

Report on account activity

[`nats server report jetstream`](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/administration#viewing-the-cluster-state) ([local](./administration.md#viewing-the-cluster-state))

Report on JetStream activity

### 

[hashtag](#nats-server-request-commands)

`nats server request` commands

Command

Description

[`nats server request jetstream`](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/administration#viewing-the-cluster-state) ([local](./administration.md#viewing-the-cluster-state))

Show JetStream details

`nats server request subscriptions`

Show subscription information

`nats server request variables`

Show runtime variables

`nats server request connections`

Show connection details

`nats server request routes`

Show route details

`nats server request gateways`

Show gateway details

`nats server request leafnodes`

Show leafnode details

`nats server request accounts`

Show account details

### 

[hashtag](#nats-server-cluster-commands)

`nats server cluster` commands

Command

Description

[`nats server cluster step-down`](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/administration#forcing-stream-and-consumer-leader-election) ([local](./administration.md#forcing-stream-and-consumer-leader-election))

Force a new leader election by standing down the current meta leader

[`nats server cluster peer-remove`](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/administration#evicting-a-peer) ([local](./administration.md#evicting-a-peer))

Removes a server from a JetStream cluster

### 

[hashtag](#experimental-commands)

Experimental commands

Command

Description

[`nats traffic`arrow-up-right](https://github.com/nats-io/natscli/blob/main/cli/traffic_command.go)

Monitor NATS traffic. (**Experimental command**)

## 

[hashtag](#further-troubleshooting-references)

Further troubleshooting references

  * [Testing your setup](https://docs.nats.io/running-a-nats-service/clients#testing-your-setup) ([local](./../../../../../09_chevron-right/07_nats-server-clients.md#testing-your-setup))

[PreviousAdministrationchevron-left](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/administration) ([local](./administration.md))[NextSuper-cluster with Gatewayschevron-right](https://docs.nats.io/running-a-nats-service/configuration/gateways) ([local](./../../gateways.md))

Last updated 2 years ago

Was this helpful?
