---
title: Terraform
source: https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/terraform
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/jetstream-config/configuration_mgmt/terraform.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Configuring JetStream](https://docs.nats.io/running-a-nats-service/configuration/resource_management) ([local](./../../resource-management.md))chevron-right
  4. [Configuration Management](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt) ([local](./../configuration-mgmt.md))

# Terraform

[Terraformarrow-up-right](https://www.terraform.io/) is a Cloud configuration tool from Hashicorp. We maintain a Provider for Terraform called [terraform-provider-jetstreamarrow-up-right](https://github.com/nats-io/terraform-provider-jetstream/) that can maintain JetStream using Terraform.

Find it in the [Terraform registryarrow-up-right](https://registry.terraform.io/providers/nats-io/jetstream/latest/docs).

## 

[hashtag](#setup)

Setup

In your project you can configure the Provider like this:

Copy

```

    provider "jetstream" {
      servers = "connect.ngs.global"
      credentials = "ngs_jetstream_admin.creds"
    }

```

Sample code below that creates the `ORDERS` example. Review the [Project READMEarrow-up-right](https://github.com/nats-io/terraform-provider-jetstream#readme) for full details.

Copy

```

    resource "jetstream_stream" "ORDERS" {
      name     = "ORDERS"
      subjects = ["ORDERS.*"]
      storage  = "file"
      max_age  = 60 * 60 * 24 * 365
    }
    
    resource "jetstream_consumer" "ORDERS_NEW" {
      stream_id      = jetstream_stream.ORDERS.id
      durable_name   = "NEW"
      deliver_all    = true
      filter_subject = "ORDERS.received"
      sample_freq    = 100
    }
    
    resource "jetstream_consumer" "ORDERS_DISPATCH" {
      stream_id      = jetstream_stream.ORDERS.id
      durable_name   = "DISPATCH"
      deliver_all    = true
      filter_subject = "ORDERS.processed"
      sample_freq    = 100
    }
    
    resource "jetstream_consumer" "ORDERS_MONITOR" {
      stream_id        = jetstream_stream.ORDERS.id
      durable_name     = "MONITOR"
      deliver_last     = true
      ack_policy       = "none"
      delivery_subject = "monitor.ORDERS"
    }
    
    output "ORDERS_SUBJECTS" {
      value = jetstream_stream.ORDERS.subjects
    }

```

[PreviousNATS Admin CLIchevron-left](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/nats-admin-cli) ([local](./nats-admin-cli.md))[NextGitHub Actionschevron-right](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/github_actions) ([local](./github-actions.md))

Last updated 4 years ago

Was this helpful?
