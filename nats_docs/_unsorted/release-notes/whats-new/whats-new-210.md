---
title: NATS 2.10
source: https://docs.nats.io/release-notes/whats_new/whats_new_210
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/release_notes/whats_new_210.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Release Notes](https://docs.nats.io/release-notes) ([local](./../../release-notes.md))chevron-right
  2. [What's New!](https://docs.nats.io/release-notes/whats_new) ([local](./../../../03_chevron-right/01_what-s-new-chevron-right.md))

# NATS 2.10

This guide is tailored for existing NATS users upgrading from NATS version 2.9.x. This will read as a summary with links to specific documentation pages to learn more about the feature or improvement.

## 

[hashtag](#upgrade-considerations)

Upgrade considerations

### 

[hashtag](#client-versions)

Client versions

Although all existing client versions will work, new client versions will expose additional options used to leverage new features. The minimum client versions that have full 2.10.0 support include:

  * CLI - [v0.1.0arrow-up-right](https://github.com/nats-io/natscli/releases/tag/v0.1.0)

  * nats.go - [v1.30.0arrow-up-right](https://github.com/nats-io/nats.go/releases/tag/v1.30.0)

  * nats.rs - [v0.32.0arrow-up-right](https://github.com/nats-io/nats.rs/releases/tag/async-nats%2Fv0.32.0)

  * nats.deno - [v1.17.0arrow-up-right](https://github.com/nats-io/nats.deno/releases/tag/v1.17.0)

  * nats.js - [v2.17.0arrow-up-right](https://github.com/nats-io/nats.js/releases/tag/v2.17.0)

  * nats.ws - [v1.18.0arrow-up-right](https://github.com/nats-io/nats.ws/releases/tag/v1.18.0)

  * nats.java - [v2.17.0arrow-up-right](https://github.com/nats-io/nats.java/releases/tag/2.17.0)

  * nats.net - [v1.1.0arrow-up-right](https://github.com/nats-io/nats.net/releases/tag/1.1.0)

  * nats.net.v2 - Coming soon!

  * nats.py - Coming soon!

  * nats.c - Coming soon!

### 

[hashtag](#helm-charts)

Helm charts

  * k8s/nats - [v1.1.0arrow-up-right](https://github.com/nats-io/k8s/releases/tag/nats-1.1.0)

  * k8s/nack - [v0.24.0arrow-up-right](https://github.com/nats-io/k8s/releases/tag/nack-0.24.0)

### 

[hashtag](#downgrade-warnings)

Downgrade warnings

For critical infrastructure like NATS, zero downtime upgrades are table stakes. Although the best practice for all infrastructure like this is for users to thoroughly test a new release against your specific workloads, inevitably there are cases where an upgrade occurs in production followed by a decision to downgrade. This is never recommended and can cause more harm than good for most infrastructure and data systems.

Below are a few important considerations if downgrading is required.

#### 

[hashtag](#storage-format-changes)

Storage format changes

2.10.0 brings on-disk storage changes which bring significant performance improvements. These are not compatible with previous versions of the NATS Server. If an upgrade is performed to a server with existing stream data on disk, followed by a downgrade, the older version server will not understand the stream data in the new format.

However, being mindful of the possibility of the need to downgrade, a special version of the 2.9.x series was released with awareness of key changes in the new storage format, allowing it to startup properly.

The takeaway is that if a downgrade is the only resort, it must be to 2.9.22 or later to ensure storage format changes are handled appropriately.

#### 

[hashtag](#stream-and-consumer-config-options)

Stream and consumer config options

There are new stream and consumer configuration options that could be problematic if a downgrade occurs since previous versions of the server have no awareness of them. Examples include:

  * Multi-filter consumers - Downgrading would result in no filter being applied since the new field is configured as a list rather than a single string.

  * Subject-transform on streams - Downgrading would result in the subject transform not being applied since the server has no awareness of it.

  * Compression on streams - Downgrading when compression is enabled on streams will cause those streams to become unloadable since the older server versions will not understand the compression being used.

## 

[hashtag](#features)

Features

### 

[hashtag](#platforms)

Platforms

  * Experimental support for [IBM z/OS](https://docs.nats.io/running-a-nats-service/introduction/installation#supported-operating-systems-and-architectures) ([local](./../../running-a-nats-service/introduction/installation.md#supported-operating-systems-and-architectures))

  * Experimental support for [NetBSD](https://docs.nats.io/running-a-nats-service/introduction/installation#supported-operating-systems-and-architectures) ([local](./../../running-a-nats-service/introduction/installation.md#supported-operating-systems-and-architectures))

### 

[hashtag](#reload)

Reload

  * A server reload can now be performed by sending a message on [`$SYS.REQ.SERVER.<server-id>.RELOAD`](https://docs.nats.io/running-a-nats-service/configuration#configuration-reloading) ([local](./../../../09_chevron-right/08_configuring-nats-server-chevron-right.md#configuration-reloading)) by a client authenticated in the system account.

### 

[hashtag](#jetstream)

JetStream

  * A new [`sync_interval` server config option](https://docs.nats.io/running-a-nats-service/configuration#jetstream) ([local](./../../../09_chevron-right/08_configuring-nats-server-chevron-right.md#jetstream)) has been added to change the default sync interval of stream data when written to disk, including allowing all writes to be flushed immediately. This option is only relevant if you need to modify durability guarantees.

### 

[hashtag](#subject-mapping)

Subject mapping

  * Subject mappings can now be [cluster-scoped](https://docs.nats.io/nats-concepts/subject_mapping#cluster-scoped-mappings) ([local](./../../../05_chevron-right/10_subject-mapping-and-partitioning.md#cluster-scoped-mappings)) and weighted, enabling the ability to have different mappings or weights on a per cluster basis.

  * The requirement to use all wildcard tokens in subject mapping or transforms has been relaxed. This can be applied to config or account-based subject mapping, stream subject transforms, and stream republishing, but not on subject mappings that are associated with stream and service import/export between accounts.

### 

[hashtag](#streams)

Streams

  * A [`subject_transform` field](https://docs.nats.io/nats-concepts/jetstream/streams#subjecttransforms) ([local](./../../nats-concepts/jetstream/streams.md#subjecttransforms)) has been added enabling per-stream subject transforms. This applies to standard streams, mirrors, and sourced streams.

  * A [`metadata` field](https://docs.nats.io/nats-concepts/jetstream/streams#configuration) ([local](./../../nats-concepts/jetstream/streams.md#configuration)) has been added to stream configuration enabling arbitrary user-defined key-value data. This is to supplant or augment the `description` field.

  * A [`first_seq` field](https://docs.nats.io/nats-concepts/jetstream/streams#configuration) ([local](./../../nats-concepts/jetstream/streams.md#configuration)) has been added to stream configuration enabling explicitly setting the initial sequence on stream creation.

  * A [`compression` field](https://docs.nats.io/nats-concepts/jetstream/streams#configuration) ([local](./../../nats-concepts/jetstream/streams.md#configuration)) has been added to stream configuration enabling on-disk compression for file-based streams.

  * The ability to edit the [`republish` config option](https://docs.nats.io/nats-concepts/jetstream/streams#republish) ([local](./../../nats-concepts/jetstream/streams.md#republish)) on a stream after stream creation was added.

  * A [`Nats-Time-Stamp` header](https://docs.nats.io/nats-concepts/jetstream/headers#republish) ([local](./../../nats-concepts/jetstream/headers.md#republish)) is now included in republished messages containing the original message's timestamp.

  * A `ts` field has been added to stream info responses indicating the server time of the snapshot. This was added to allow for local time calculations relying on the local clock.

  * An array of subject-transforms (subject filter + subject transform destination) can be added to a mirror or source configuration (can not use the single subject filter/subject transform destination fields at the same time as the array).

  * A stream configured with `sources` can source from the same stream multiple times when distinct filter+transform options are used, allowing for some messages of a stream to be sourced more than once.

### 

[hashtag](#consumers)

Consumers

  * A [`filter_subjects` field](https://docs.nats.io/nats-concepts/jetstream/consumers#filtersubjects) ([local](./../../nats-concepts/jetstream/consumers.md#filtersubjects)) has been added which enables applying server-side filtering against multiple disjoint subjects, rather than only one.

  * A [`metadata` field](https://docs.nats.io/nats-concepts/jetstream/consumers#configuration) ([local](./../../nats-concepts/jetstream/consumers.md#configuration)) has been added to consumer configuration enabling arbitrary user-defined key-value data. This is to supplant or augment the `description` field.

  * A `ts` field has been added to consumer info responses indicating the server time of the snapshot. This was added to allow for local time calculations without relying on the local clock.

### 

[hashtag](#key-value)

Key-value

  * A [`metadata` fieldarrow-up-right](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/key-value-store.md#configuration) has been added to key-value configuration enabling arbitrary user-defined key-value data. This is to supplant or augment the `description` field.

  * A bucket configured as a mirror or sourcing from other buckets

### 

[hashtag](#object-store)

Object store

  * A [`metadata` fieldarrow-up-right](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/object-store.md#configuration) has been added to object store configuration enabling arbitrary user-defined key-value data. This is to supplant or augment the `description` field.

### 

[hashtag](#authn-authz)

Authn/Authz

  * A pluggable server extension, referred to as [auth callout](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout) ([local](./../../running-a-nats-service/configuration/securing-nats/auth-callout.md)), has been added. This provides a mechanism for delegating authentication checks against a bring-your-own (BYO) provider and, optionally, dynamically declaring permissions for the authenticated user.

### 

[hashtag](#monitoring)

Monitoring

  * A `unique_tag` field has been added to the [`/varz`](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#general-information) ([local](./../../running-a-nats-service/nats-admin/monitoring.md#general-information)) and [`/jsz`](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#jetstream-information) ([local](./../../running-a-nats-service/nats-admin/monitoring.md#jetstream-information)) HTTP endpoint responses, corresponding to the value of `unique_tag` defined in the server config.

  * A `slow_consumer_stats` field has been added to the [`/varz`](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#general-information) ([local](./../../running-a-nats-service/nats-admin/monitoring.md#general-information)) HTTP endpoint providing a count of slow consumers for clients, routes, gateways, and leafnodes.

  * A `raft=1` query parameter has been added to the [`/jsz`](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#jetstream-information) ([local](./../../running-a-nats-service/nats-admin/monitoring.md#jetstream-information)) HTTP endpoint which adds `stream_raft_group` and `consumer_raft_groups` fields to the response.

  * A `num_subscriptions` field has been added to the [`$SYS.REQ.SERVER.PING.STATZ`](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts#usdsys.req.server.less-than-id-greater-than.statsz-requesting-server-stats-summary) ([local](./../../running-a-nats-service/configuration/sys-accounts/sys-accounts.md#usdsys.req.server.less-than-id-greater-than.statsz-requesting-server-stats-summary)) NATS endpoint responses.

  * A system account responder for [`$SYS.REQ.SERVER.PING.IDZ`](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts#usdsys.req.server.ping.idz-discovering-servers) ([local](./../../running-a-nats-service/configuration/sys-accounts/sys-accounts.md#usdsys.req.server.ping.idz-discovering-servers)) has been added which returns info for the server that the client is connected to.

  * A system account responder for [`$SYS.REQ.SERVER.PING.PROFILEZ`](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts#usdsys.req.server.less-than-id-greater-than.profilez-request-profiling-information) ([local](./../../running-a-nats-service/configuration/sys-accounts/sys-accounts.md#usdsys.req.server.less-than-id-greater-than.profilez-request-profiling-information)) has been added and works even if a profiling port is not enabled in the server configuration.

  * A user account responder for [`$SYS.REQ.USER.INFO`](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts#usdsys.req.user.info-request-connected-user-information) ([local](./../../running-a-nats-service/configuration/sys-accounts/sys-accounts.md#usdsys.req.user.info-request-connected-user-information)) has been added which allows a connected user to query for the account they are in and permissions they have.

### 

[hashtag](#mqtt)

MQTT

  * Support for [QoS2](https://docs.nats.io/running-a-nats-service/configuration/mqtt) ([local](./../../running-a-nats-service/configuration/mqtt.md)) has been added. Check out the new [MQTT implementation detailsarrow-up-right](https://github.com/nats-io/nats-server/blob/main/server/README-MQTT.md) overview.

### 

[hashtag](#clustering)

Clustering

  * When defining routes between servers, a handful of optimizations have been introduced including a pool of TCP connections between servers, optional pinning of accounts to connections, and optional compression of traffic. There is quite a bit to dig into, so check out the [v2 routes](https://docs.nats.io/running-a-nats-service/configuration/clustering/v2_routes) ([local](./../../running-a-nats-service/configuration/clustering/v2-routes.md)) page for details.

### 

[hashtag](#leafnodes)

Leafnodes

  * A [`handshake_first` config option](https://docs.nats.io/running-a-nats-service/configuration/leafnodes#tls-first-handshake) ([local](./../../running-a-nats-service/configuration/leafnodes.md#tls-first-handshake)) has been added enabling TLS-first handshakes for leafnode connections.

### 

[hashtag](#windows)

Windows

  * The [`NATS_STARTUP_DELAY` environment variable](https://docs.nats.io/running-a-nats-service/introduction/windows_srv#nats_startup_delay-environment-variable) ([local](./../../running-a-nats-service/introduction/windows-srv.md#nats_startup_delay-environment-variable)) has been added to allow changing the default startup for the server of 10 seconds

## 

[hashtag](#improvements)

Improvements

### 

[hashtag](#reload-1)

Reload

  * The [`nats-server --signal` command](https://docs.nats.io/running-a-nats-service/nats_admin/signals#multiple-processes) ([local](./../../running-a-nats-service/nats-admin/signals.md#multiple-processes)) now supports a glob expression on the `<pid>` argument which would match a subset of all `nats-server` instances running on the host.

### 

[hashtag](#streams-1)

Streams

  * Prior to 2.10, setting [`republish` configuration](https://docs.nats.io/nats-concepts/jetstream/streams#republish) ([local](./../../nats-concepts/jetstream/streams.md#republish)) on mirrors would result in an error. On sourcing streams, only messages that were actively between stored matching configured `subjects` would be republished. The behavior has been relaxed to allow republishing on mirrors and includes all messages on sourcing streams.

### 

[hashtag](#consumers-1)

Consumers

  * A new header has been added on a fetch response that indicates to clients the fetch has been fulfilled without requiring clients to rely on heartbeats. It avoids some conditions in which the client would issue fetch requests that could go over limits or have more fetch requests pending than required.

### 

[hashtag](#leafnodes-1)

Leafnodes

  * Previously, a leafnode configured with two or more remotes binding to the same hub account would be rejected. This restriction has been relaxed since each remote could be binding to a different local account.

### 

[hashtag](#mqtt-1)

MQTT

  * Previously a dot `.` in an MQTT topic was not supported, however now it is! Check out the [topic-subject conversion table](https://docs.nats.io/running-a-nats-service/configuration/mqtt) ([local](./../../running-a-nats-service/configuration/mqtt.md)) for details.

[PreviousNATS 2.11chevron-left](https://docs.nats.io/release-notes/whats_new/whats_new_211) ([local](./whats-new-211.md))[NextNATS 2.2chevron-right](https://docs.nats.io/release-notes/whats_new/whats_new_22) ([local](./whats-new-22.md))

Last updated 2 years ago

Was this helpful?
