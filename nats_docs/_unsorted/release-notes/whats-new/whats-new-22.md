---
title: NATS 2.2
source: https://docs.nats.io/release-notes/whats_new/whats_new_22
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/release_notes/whats_new_22.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Release Notes](https://docs.nats.io/release-notes) ([local](./../../release-notes.md))chevron-right
  2. [What's New!](https://docs.nats.io/release-notes/whats_new) ([local](./../../../03_chevron-right/01_what-s-new-chevron-right.md))

# NATS 2.2

NATS 2.2 is the largest feature release since version 2.0. The 2.2 release provides highly scalable, highly performant, secure and easy-to-use next generation streaming in the form of JetStream, allows remote access via websockets, has simplified NATS account management, native MQTT support, and further enables NATS toward our goal of securely democratizing streams and services for the hyperconnected world we live in.

## 

[hashtag](#next-generation-streaming)

Next Generation Streaming

JetStream is the next generation streaming platform for NATS, highly resilient, highly available, and easy to use. We’ve spent a long time listening to our community, learning from our experiences, looking at the needs of today, and thinking deeply about the needs of tomorrow. We built JetStream to address these needs.

JetStream:

  * is easy to deploy and manage, built into the NATS server

  * simplifies and accelerates development

  * supports wildcard subjects

  * supports at least once delivery and exactly once within a window

  * is horizontally scalable at runtime with no interruptions

  * persists data via streams and delivers or replays via consumers

  * supports multiple patterns to consume data on the same stream

  * supports push and pull modes when consuming messages

  * is account aware

  * allows for detailed granularity of security, by stream, by consumer, by function

Get started with [JetStream](https://docs.nats.io/nats-concepts/jetstream) ([local](./../../../05_chevron-right/08_jetstream-chevron-right.md)).

## 

[hashtag](#security-and-simplified-account-management)

Security and Simplified Account Management

Account management just became much easier. This version of NATS has a built-in account management system, eliminating the need to set up an account manager when not using the memory account resolver. With automated default system account generation, and the ability to preload accounts, simply enable a set of servers in your deployment to be account resolvers or account resolver caches, and they will handle public account information provided to the NATS system through the NATS nsc tooling. Have enterprise-scale account management up and running in minutes.

### 

[hashtag](#cidr-block-account-restrictions)

CIDR Block Account Restrictions

By specifying a CIDR block restriction for a user, policy can be applied to limit connections from clients within a certain range or set of IP addresses. Use this as another layer of security atop user credentials to better secure your distributed system. Ensure your applications can only connect from within a specific cloud, enterprise, geographic location, virtual or physical network.

### 

[hashtag](#time-based-account-restrictions)

Time-Based Account Restrictions

Scoped to the user, you can now [specify a specific block of time](https://docs.nats.io/using-nats/nats-tools/nsc/basics#user-authorization) ([local](./../../using-nats/nats-tools/nsc/basics.md#user-authorization)) during the day when applications can connect. For example, permit certain users or applications to access the system during specified business hours, or protect business operations during the busiest parts of the day from batch driven back-office applications that could adversely impact the system when run at the wrong time.

### 

[hashtag](#default-user-permissions)

Default User Permissions

Now you can specify [default user permissions](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization#examples) ([local](./../../running-a-nats-service/configuration/securing-nats/authorization.md#examples)) within an account. This significantly reduces efforts around policy, reduces chances for error in permissioning, and simplifies the provisioning of user credentials.

## 

[hashtag](#websockets)

WebSockets

Connect mobile and web applications to any NATS server using [WebSockets](https://docs.nats.io/running-a-nats-service/configuration/websocket) ([local](./../../running-a-nats-service/configuration/websocket.md)). Built to more easily traverse firewalls and load balancers, NATS WebSocket support provides even more flexibility to NATS deployments and makes it easier to communicate to the edge and endpoints. This is currently supported in NATS server leaf nodes, nats.ts, nats.deno, and the nats.js clients.

## 

[hashtag](#native-mqtt-support)

Native MQTT Support

With the [Adaptive Edge architecturearrow-up-right](https://nats.io/blog/synadia-adaptive-edge/) and the ease with which NATS can extend a cloud deployment to the edge, it makes perfect sense to leverage existing investments in IoT deployments. It’s expensive to update devices and large edge deployments. Our goal is to enable the hyperconnected world, so we added first-class support for [MQTT 3.1.1](https://docs.nats.io/running-a-nats-service/configuration/mqtt) ([local](./../../running-a-nats-service/configuration/mqtt.md)) directly into the NATS Server.

Seamlessly integrate existing IoT deployments using MQTT 3.1.1 with a cloud-native NATS deployment. Add a leaf node that is MQTT enabled and instantly send and receive messages to your MQTT applications and devices from a NATS deployment whether it be edge, single-cloud, multi-cloud, on-premise, or any combination thereof.

## 

[hashtag](#build-better-systems)

Build Better Systems

We’ve added a variety of features to allow you to build a more resilient, secure, and simply better system at scale.

### 

[hashtag](#message-headers)

Message Headers

We’ve added the ability to optionally use headers, following the HTTP semantics familiar to developers. Headers naturally apply overhead, which was why we resisted adding them for so long. By creating new internal protocol messages transparent to developers, we maintain the extremely fast processing of simple NATS messages that we have always had while supporting headers for those who would like to leverage them. Adding headers to messages allows you to provide application-specific metadata, such as compression or encryption-related information, without touching the payload. We also provide some NATS specific headers for use in JetStream and other features.

### 

[hashtag](#seamless-maintenance-with-lame-duck-notifications)

Seamless Maintenance with Lame Duck Notifications

When taking down a server for maintenance, servers can be signaled to enter [Lame Duck Mode](https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode) ([local](./../../running-a-nats-service/nats-admin/lame-duck-mode.md)) where they do not accept new connections and evict existing connections over a period of time. Maintainer supported clients will notify applications that a server has entered this state and will be shutting down, allowing a client to smoothly transition to another server or cluster and better maintain business continuity during scheduled maintenance periods.

### 

[hashtag](#react-quicker-with-no-responder-notifications)

React Quicker with No-Responder Notifications

Why wait for timeouts when services aren’t available? When a request is made to a service (request-reply) and the NATS Server knows there are no services available the server will short circuit the request. A “no-responders” protocol message will be sent back to the requesting client which will break from blocking API calls. This allows applications to immediately react which further enables building a highly responsive system at scale, even in the face of application failures and network partitions.

### 

[hashtag](#subject-mapping-and-traffic-shaping)

Subject Mapping and Traffic Shaping

Reduce risk when onboarding new services. Canary deployments, A/B testing, and transparent teeing of data streams are now fully supported in NATS. The NATS Server allows accounts to form subject mappings from one subject to another for both client inbound and service import invocations and allows weighted sets for the destinations. Map any percentage - 1 to 100 percent of your traffic - to other subjects, and change this at runtime with a server configuration reload. You can even artificially drop a percentage of traffic to introduce chaos testing into your system. See [Configuring Subject Mapping and Traffic Shaping](https://docs.nats.io/running-a-nats-service/configuration/configuring_subject_mapping) ([local](./../../running-a-nats-service/configuration/configuring-subject-mapping.md)) in NATS Server configuration for more details.

### 

[hashtag](#account-monitoring-more-meaningful-metrics)

Account Monitoring - More Meaningful Metrics

NATS now allows for [fine-grained monitoring](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#monitoring-nats) ([local](./../../running-a-nats-service/nats-admin/monitoring.md#monitoring-nats)) to identify usage metrics tied to a particular account. Inspect messages and bytes sent or received and various connection statistics for a particular account. Accounts can represent anything - a group of applications, a team or organization, a geographic location, or even roles. If NATS is enabling your SaaS solution you could use NATS account scoped metrics to bill users.

[PreviousNATS 2.10chevron-left](https://docs.nats.io/release-notes/whats_new/whats_new_210) ([local](./whats-new-210.md))[NextNATS 2.0chevron-right](https://docs.nats.io/release-notes/whats_new/whats_new_20) ([local](./whats-new-20.md))

Last updated 2 years ago

Was this helpful?
