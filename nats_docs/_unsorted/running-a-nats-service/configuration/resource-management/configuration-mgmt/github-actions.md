---
title: GitHub Actions
source: https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/github_actions
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/jetstream-config/configuration_mgmt/github_actions.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Configuring JetStream](https://docs.nats.io/running-a-nats-service/configuration/resource_management) ([local](./../../resource-management.md))chevron-right
  4. [Configuration Management](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt) ([local](./../configuration-mgmt.md))

# GitHub Actions

We have a pack of GitHub Actions that let you manage an already running JetStream Server, useful for managing releases or standing up test infrastructure.

Full details and examples are in the [jetstream-gh-actionsarrow-up-right](https://github.com/nats-io/jetstream-gh-action) repository, here's an example.

Copy

```

    on: push
    name: orders
    jobs:
    
      # First we delete the ORDERS stream and consumer if they already exist
      clean_orders:
        runs-on: ubuntu-latest
        steps:
          - name: orders_stream
            uses: nats-io/jetstream-gh-action/delete/stream@master
            with:
              missing_ok: 1
              stream: ORDERS
              server: js.example.net
    
      # Now we create the Stream and Consumers using the same configuration files the 
      # nats CLI utility would use as shown above
      create_orders:
        runs-on: ubuntu-latest
        needs: clean_orders
        steps:
          - uses: actions/checkout@master
          - name: orders_stream
            uses: nats-io/jetstream-gh-action/create/stream@master
            with:
              config: ORDERS.json
              server: js.example.net
          - name: orders_new_consumer
            uses: nats-io/jetstream-gh-action/create/consumer@master
            with:
              config: ORDERS_NEW.json
              stream: ORDERS
              server: js.example.net
    
      # We publish a message to a specific Subject, perhaps some consumer is 
      # waiting there for it to kick off tests
      publish_message:
        runs-on: ubuntu-latest
        needs: create_orders
        steps:
          - uses: actions/checkout@master
          - name: orders_new_consumer
            uses: nats-io/jetstream-gh-action@master
            with:
              subject: ORDERS.deployment
              message: Published new deployment via "${{ github.event_name }}" in "${{ github.repository }}"
              server: js.example.net

```

[PreviousTerraformchevron-left](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/terraform) ([local](./terraform.md))[NextKubernetes Controllerchevron-right](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/kubernetes_controller) ([local](./kubernetes-controller.md))

Last updated 4 years ago

Was this helpful?
