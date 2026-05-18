---
title: NATS and Kubernetes
source: https://docs.nats.io/running-a-nats-service/nats-kubernetes
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats-on-kubernetes/nats-kubernetes.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../_unsorted/running-a-nats-service.md))

# NATS and Kubernetes

The recommended way to deploy NATS on Kubernetes is using [Helmarrow-up-right](https://helm.sh/) with the official NATS Helm Chart.

## 

[hashtag](#helm-repo)

Helm repo

To register the NATS Helm chart run:

Copy

```

    helm repo add nats https://nats-io.github.io/k8s/helm/charts/

```

## 

[hashtag](#config-values)

Config values

The default configuration values of the chart will deploy a single NATS server as a `StatefulSet` and a single replica [nats-boxarrow-up-right](https://github.com/nats-io/nats-box) `Deployment`.

The [ArtifactHub pagearrow-up-right](https://artifacthub.io/packages/helm/nats/nats) provides the list of Helm configuration values and examples for the current release.

_For tracking the development version, refer to the_[ _source repo_ arrow-up-right](https://github.com/nats-io/k8s/tree/main/helm/charts/nats#nats-server) _._

Once the desired configuration is created, install the chart:

Copy

```

    helm install nats nats/nats

```

## 

[hashtag](#validate-connectivity)

Validate connectivity

Once the pods are up, validate by accessing the `nats-box` container and running a CLI command.

Copy

```

    kubectl exec -it deployment/nats-box -- nats pub test hi

```

The output should indicate a successful publish to NATS.

Copy

```

    16:17:00 Published 2 bytes to "test"

```

## 

[hashtag](#commercial-options)

Commercial Options

Synadia offers [Deploy for Kubernetesarrow-up-right](https://www.synadia.com/deploy-for-kubernetes/), a self-service, bring-your-own Kubernetes deployment option that includes NATS and additional components.

[PreviousNGS Leaf Nodeschevron-left](https://docs.nats.io/running-a-nats-service/nats_docker/ngs-leafnodes-docker) ([local](./../_unsorted/running-a-nats-service/nats-docker/ngs-leafnodes-docker.md))[NextNATS Server Clientschevron-right](https://docs.nats.io/running-a-nats-service/clients) ([local](./07_nats-server-clients.md))

Last updated 10 months ago

Was this helpful?
