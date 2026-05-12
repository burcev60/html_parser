---
title: Configure, Scale & Update Qdrant Hybrid Cloud Clusters
source: https://qdrant.tech/documentation/hybrid-cloud/configure-scale-upgrade/
---

# Configure, Scale & Update Qdrant Hybrid Cloud Clusters

## Configure Clusters

Alongside Hybrid Cloud specific scheduling options, you can also adjust various other advanced configuration options for your clusters. See [Configure Clusters](https://qdrant.tech/documentation/cloud/configure-cluster/) ([local](./../cloud/configure-cluster.md)) for more details.

## Scale Clusters

Hybrid cloud clusters can be scaled up and down, horizontally and vertically, at any time. For more details see [Scale Clusters](https://qdrant.tech/documentation/cloud/cluster-scaling/) ([local](./../cloud/cluster-scaling.md)).

### Automatic Shard Rebalancing

Qdrant Cloud supports automatic shard rebalancing when scaling your cluster horizontally. This ensures that data is evenly distributed across the nodes, optimizing performance and resource utilization. For more details see [Shard Rebalancing](https://qdrant.tech/documentation/cloud/configure-cluster/#shard-rebalancing) ([local](./../cloud/configure-cluster.md#shard-rebalancing)).

### Resharding

In Qdrant Cloud, you can change the number of shards in your existing collections without having to recreate the collection from scratch. This feature is called resharding and allows you to scale your collections up or down as needed. For more details see [Resharding](https://qdrant.tech/documentation/cloud/cluster-scaling/#resharding) ([local](./../cloud/cluster-scaling.md#resharding)).

## Update Clusters

You can update the version of your cluster at any time. For more details see [Update Clusters](https://qdrant.tech/documentation/cloud/cluster-upgrades/) ([local](./../cloud/cluster-upgrades.md)).
