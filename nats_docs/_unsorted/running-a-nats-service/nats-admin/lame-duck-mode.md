---
title: Lame Duck Mode
source: https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/lame_duck_mode.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Managing and Monitoring your NATS Server Infrastructure](https://docs.nats.io/running-a-nats-service/nats_admin) ([local](./../../../09_chevron-right/10_managing-and-monitoring-your-nats-server-infrastructure-chev.md))

# Lame Duck Mode

In production we recommend that a server is shut down with ​lame duck mode​ as a graceful way to slowly evict clients. With large deployments this mitigates the "thundering herd" situation that will place CPU pressure on servers as TLS enabled clients reconnect.

## 

[hashtag](#server)

Server

Lame duck mode is initiated by [signaling](https://docs.nats.io/running-a-nats-service/nats_admin/signals) ([local](./signals.md)) the server:

Copy

```

    nats-server --signal ldm

```

After entering lame duck mode, the server will stop accepting new connections, wait for a 10 second grace period, then begin to evict clients over a period of time configurable by the [lame_duck_durationarrow-up-right](https://docs.nats.io/nats-server/configuration#runtime-configuration) ([local](./../../nats-server/configuration.md#runtime-configuration)) configuration option. This period defaults to 2 minutes.

## 

[hashtag](#clients)

Clients

When entering lame duck mode, the server will send a message to clients. Some maintainer supported clients will invoke an optional callback indicating that a server is entering lame duck mode. This is used for cases where an application can benefit from preparing for the short outage between the time it is evicted and automatically reconnected to another server.

[PreviousSignalschevron-left](https://docs.nats.io/running-a-nats-service/nats_admin/signals) ([local](./signals.md))[NextProfilingchevron-right](https://docs.nats.io/running-a-nats-service/nats_admin/profiling) ([local](./profiling.md))

Last updated 5 months ago

Was this helpful?
