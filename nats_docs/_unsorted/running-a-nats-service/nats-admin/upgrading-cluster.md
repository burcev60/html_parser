---
title: Upgrading a Cluster
source: https://docs.nats.io/running-a-nats-service/nats_admin/upgrading_cluster
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/upgrading_cluster.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Managing and Monitoring your NATS Server Infrastructure](https://docs.nats.io/running-a-nats-service/nats_admin) ([local](./../../../09_chevron-right/10_managing-and-monitoring-your-nats-server-infrastructure-chev.md))

# Upgrading a Cluster

Repeat this procedure for all nodes of the cluster, one at a time:

  1. Stop the server by putting it into [Lame Duck Modearrow-up-right](https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode) ([local](./lame-duck-mode.md))

  2. Replace the binary or Docker image with the new version.

  3. Restart the server.

  4. Wait until the `/healthz` endpoint returns `HTTP 200 OK` before moving on to the next cluster node.

### 

[hashtag](#downgrading)

Downgrading

Although the NATS server goes through rigorous testing for each release, there may be a need to revert to the previous version if you observe a performance regression for your workload. The support policy for the server is the current release as well as one patch version release prior. For example, if the latest is 2.8.4, a downgrade to 2.8.3 is supported. Downgrades to earlier versions may work, but is not recommended.

Fortunately, the downgrade path is the same as the upgrade path as noted above. Swap the binary and do a rolling restart.

[PreviousIn Depth JWT Guidechevron-left](https://docs.nats.io/running-a-nats-service/nats_admin/security/jwt) ([local](./security/jwt.md))[NextSlow Consumerschevron-right](https://docs.nats.io/running-a-nats-service/nats_admin/slow_consumers) ([local](./slow-consumers.md))

Last updated 10 months ago

Was this helpful?
