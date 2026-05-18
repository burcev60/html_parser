---
title: Account Information
source: https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/account
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/jetstream_admin/account.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../running-a-nats-service.md))chevron-right
  2. [Managing and Monitoring your NATS Server Infrastructure](https://docs.nats.io/running-a-nats-service/nats_admin) ([local](./../../../../09_chevron-right/10_managing-and-monitoring-your-nats-server-infrastructure-chev.md))chevron-right
  3. [Managing JetStream](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin) ([local](./../jetstream-admin.md))

# Account Information

## 

[hashtag](#account-information)

Account Information

JetStream is multi-tenant so you will need to check that your account is enabled for JetStream and is not limited. You can view your limits as follows:

Copy

```

    nats account info

```

Copy

```

    Connection Information:
                   Client ID: 8
                   Client IP: 127.0.0.1
                         RTT: 178.545µs
           Headers Supported: true
             Maximum Payload: 1.0 MiB
               Connected URL: nats://localhost:4222
           Connected Address: 127.0.0.1:4222
         Connected Server ID: NCCOHA6ONXJOGAEZP4WPU4UJ3IQP2VVXEPRKTQCGBCW4IL4YYW4V4KKL
    JetStream Account Information:
               Memory: 0 B of 5.7 GiB
              Storage: 0 B of 11 GiB
              Streams: 0 of Unlimited
       Max Consumers: unlimited

```

[PreviousManaging JetStreamchevron-left](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin) ([local](./../jetstream-admin.md))[NextNaming Streams, Consumers, and Accountschevron-right](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/naming) ([local](./naming.md))

Last updated 4 years ago

Was this helpful?
