---
title: Kubernetes Controller
source: https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/kubernetes_controller
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/jetstream-config/configuration_mgmt/kubernetes_controller.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Configuring JetStream](https://docs.nats.io/running-a-nats-service/configuration/resource_management) ([local](./../../resource-management.md))chevron-right
  4. [Configuration Management](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt) ([local](./../configuration-mgmt.md))

# Kubernetes Controller

The JetStream controllers allow you to manage NATS JetStream Streams and Consumers via K8S CRDs. You can find more info on how to deploy and usage [herearrow-up-right](https://github.com/nats-io/nack#getting-started). Below you can find an example of how to create a stream and a couple of consumers:

Copy

```

    ---
    apiVersion: jetstream.nats.io/v1beta1
    kind: Stream
    metadata:
      name: mystream
    spec:
      name: mystream
      subjects: ["orders.*"]
      storage: memory
      maxAge: 1h
    ---
    apiVersion: jetstream.nats.io/v1beta1
    kind: Consumer
    metadata:
      name: my-push-consumer
    spec:
      streamName: mystream
      durableName: my-push-consumer
      deliverSubject: my-push-consumer.orders
      deliverPolicy: last
      ackPolicy: none
      replayPolicy: instant
    ---
    apiVersion: jetstream.nats.io/v1beta1
    kind: Consumer
    metadata:
      name: my-pull-consumer
    spec:
      streamName: mystream
      durableName: my-pull-consumer
      deliverPolicy: all
      filterSubject: orders.received
      maxDeliver: 20
      ackPolicy: explicit

```

Once the CRDs are installed you can use `kubectl` to manage the streams and consumers as follows:

Copy

```

    $ kubectl get streams
    NAME       STATE     STREAM NAME   SUBJECTS
    mystream   Created   mystream      [orders.*]
    
    $ kubectl get consumers
    NAME               STATE     STREAM     CONSUMER           ACK POLICY
    my-pull-consumer   Created   mystream   my-pull-consumer   explicit
    my-push-consumer   Created   mystream   my-push-consumer   none
    
    # If you end up in an Errored state, run kubectl describe for more info.
    #     kubectl describe streams mystream
    #     kubectl describe consumers my-pull-consumer

```

[PreviousGitHub Actionschevron-left](https://docs.nats.io/running-a-nats-service/configuration/resource_management/configuration_mgmt/github_actions) ([local](./github-actions.md))[NextClusteringchevron-right](https://docs.nats.io/running-a-nats-service/configuration/clustering) ([local](./../../clustering.md))

Last updated 4 years ago

Was this helpful?
