---
title: Getting Started with Qdrant Managed Cloud
source: https://qdrant.tech/documentation/cloud-getting-started/
---

# Getting Started with Qdrant Managed Cloud

Welcome to Qdrant Managed Cloud! This document contains all the information you need to get started.

## Prerequisites

Before creating a cluster, make sure you have a Qdrant Cloud account. Detailed instructions for signing up can be found in the [Qdrant Cloud Setup](https://qdrant.tech/documentation/cloud-account-setup/) ([local](./cloud-account-setup.md)) guide. Qdrant Cloud supports granular [role-based access control](https://qdrant.tech/documentation/cloud-rbac/) ([local](./cloud-rbac.md)).

You also need to provide [payment details](https://qdrant.tech/documentation/cloud-pricing-payments/) ([local](./cloud-pricing-payments.md)). If you have a custom payment agreement, first create your account, then [contact our Support Team](https://support.qdrant.io/) to finalize the setup.

Premium Plan subscribers can enable single sign-on (SSO) for their organizations. To activate SSO, please reach out to the Support Team at <https://support.qdrant.io/> for guidance.

## Cluster Sizing

Before deploying any cluster, consider the resources needed for your specific workload. Our [Capacity Planning guide](https://qdrant.tech/documentation/capacity-planning/) ([local](./capacity-planning.md)) describes how to assess the required CPU, memory, and storage. Additionally, the [Pricing Calculator](https://cloud.qdrant.io/calculator) helps you estimate associated costs based on your projected usage.

## Creating and Managing Clusters

After setting up your account, you can create a Qdrant Cluster by following the steps in [Create a Cluster](https://qdrant.tech/documentation/cloud/create-cluster/) ([local](./cloud/create-cluster.md)).

## Preparing for Production

For a production-ready environment, consider deploying a multi-node Qdrant cluster (at least three nodes) with replication enabled. More details are available in the [Distributed Deployment](https://qdrant.tech/documentation/distributed_deployment/) ([local](./distributed-deployment.md)) guide. For more information on how to create a production-ready cluster, see our [Vector Search in Production](https://qdrant.tech/articles/vector-search-production/) article.

If you are looking to optimize costs, you can reduce memory usage through [Quantization](https://qdrant.tech/documentation/manage-data/quantization/) ([local](./../04_user-manual/01_manage-data/07_quantization.md)) or by [offloading vectors to disk](https://qdrant.tech/documentation/manage-data/storage/#configuring-memmap-storage) ([local](./../04_user-manual/01_manage-data/05_storage.md#configuring-memmap-storage)).

## Infrastructure as Code Automation

Qdrant Cloud can be fully automated using the [Qdrant Cloud API](https://qdrant.tech/documentation/cloud-api/) ([local](./cloud-api.md)). This allows you to create, manage, and scale clusters programmatically. You can also use our [Terraform Provider](https://registry.terraform.io/providers/qdrant/qdrant-cloud) to automate your Qdrant Cloud infrastructure.
