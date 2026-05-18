---
title: Managing JetStream
source: https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/jetstream_admin/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Managing and Monitoring your NATS Server Infrastructure](https://docs.nats.io/running-a-nats-service/nats_admin) ([local](./../../../09_chevron-right/10_managing-and-monitoring-your-nats-server-infrastructure-chev.md))

# Managing JetStream

Once the server is running it's time to use the management tool. Please refer to the [installation section in the readmearrow-up-right](https://github.com/nats-io/natscli?tab=readme-ov-file#installation).

Copy

```

    nats --help
    nats cheat

```

We'll walk through the above scenario and introduce features of the CLI and of JetStream as we recreate the setup above.

Throughout this example, we'll show other commands like `nats pub` and `nats sub` to interact with the system. These are normal existing core NATS commands and JetStream is fully usable by only using core NATS.

We'll touch on some additional features but please review the section on the design model to understand all possible permutations.

[PreviousMonitoring JetStreamchevron-left](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring/monitoring_jetstream) ([local](./monitoring/monitoring-jetstream.md))[NextAccount Informationchevron-right](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/account) ([local](./jetstream-admin/account.md))

Last updated 1 year ago

Was this helpful?
