---
title: NATS Admin CLI
source: https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/nats-admin-cli
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/jetstream-config/configuration_mgmt/nats-admin-cli.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Configuring JetStream](https://docs.nats.io/running-a-nats-service/configuration/resource_management) ([local](./../../resource-management.md))chevron-right
  4. [Configuration Management](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt) ([local](./../configuration-mgmt.md))

# NATS Admin CLI

## 

[hashtag](#nats-admin-cli)

nats Admin CLI

The [`nats` CLIarrow-up-right](https://github.com/nats-io/natscli?tab=readme-ov-file#installation) can be used to manage Streams and Consumers easily using it's `--config` flag, for example:

## 

[hashtag](#add-a-new-stream)

Add a new Stream

This creates a new Stream based on `orders.json`. The `orders.json` file can be extracted from an existing stream using `nats stream info ORDERS -j | jq .config`

Copy

```

    nats str add ORDERS --config orders.json

```

## 

[hashtag](#edit-an-existing-stream)

Edit an existing Stream

This edits an existing stream ensuring it complies with the configuration in `orders.json`

Copy

```

    nats str edit ORDERS --config orders.json

```

## 

[hashtag](#add-a-new-consumer)

Add a New Consumer

This creates a new Consumer based on `orders_new.json`. The `orders_new.json` file can be extracted from an existing stream using `nats con info ORDERS NEW -j | jq .config`

Copy

```

    nats con add ORDERS NEW --config orders_new.json

```

[PreviousConfiguration Managementchevron-left](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt) ([local](./../configuration-mgmt.md))[NextTerraformchevron-right](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/terraform) ([local](./terraform.md))

Last updated 1 year ago

Was this helpful?
