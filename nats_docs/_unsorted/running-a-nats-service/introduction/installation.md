---
title: Installing a NATS Server
source: https://docs.nats.io/running-a-nats-service/introduction/installation
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/installation.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Installing, running and deploying a NATS Server](https://docs.nats.io/running-a-nats-service/introduction) ([local](./../../../09_chevron-right/01_installing-running-and-deploying-a-nats-server-chevron-right.md))

# Installing a NATS Server

NATS philosophy is simplicity. Installation is just decompressing a zip file and copying the binary to an appropriate directory; you can also use your favorite package manager. Here's a list of different ways you can install or run NATS:

  * [Command Line](#getting-the-binary-from-the-command-line)

  * [Docker](#installing-via-docker)

  * [Kubernetes](https://docs.nats.io/running-a-nats-service/nats-kubernetes) ([local](./../../../09_chevron-right/06_nats-and-kubernetes.md))

  * [Package Manager](#installing-via-a-package-manager)

  * [Release Zip](#downloading-a-release-build)

  * [Development Build](#installing-from-the-source)

See also [installing the NATS client](https://docs.nats.io/running-a-nats-service/clients#installing-the-nats-cli-tool) ([local](./../../../09_chevron-right/07_nats-server-clients.md#installing-the-nats-cli-tool))

## 

[hashtag](#supported-operating-systems-and-architectures)

Supported operating systems and architectures

The following table indicates the current supported NATS server build combinations for operating systems and architectures.

Operating System

Architectures

Status

Darwin (macOS)

amd64, arm64

Stable

Linux

amd64, 386, arm6, arm7, arm64, mips64le, s390x

Stable

Windows

amd64, 386, arm6, arm7, arm64

Stable

FreeBSD

amd64

Stable

NetBSD

-

Experimental

IBM z/OS

-

Experimental

 _Note, not all installation methods below have distributions for all OS and architecture combinations._

## 

[ hashtag](#hardware-requirements)

Hardware requirements

The NATS server itself has minimal hardware requirements to support small edge devices, but can take advantage of more resources if available.

CPU should be considered in accepting TLS connections. After a network partition, every disconnected client will attempt to connect to a NATS server in the cluster simultaneously, so CPU on those servers will momentarily spike. When there are many clients this can be mitigated with reconnect jitter settings, and errors can be reduced with longer TLS timeouts, and scaling up cluster sizes.

We highly recommend testing to see if smaller, cheaper machines suffice for your workload - often they do! We suggest starting here and adjusting resources after load testing specific to your environment. When using cloud provider instance types make sure the node has a sufficient NIC to support the required bandwidth for the application needs.

For high throughput use cases, the network interface card (NIC) or the available bandwidth are often the bottleneck, so ensure the hardware or cloud provider instance types are sufficient for your needs.

### 

[hashtag](#core-nats)

Core NATS

The tables below outline the **minimum number of cores and memory** for stable cluster performance with different combinations of publishers, subscribers, and message rates. Stability is defined as the system avoiding slowdowns or running out of memory. These tests were conducted inside containers with `GOMEMLIMIT` set to 90% of the memory allocation, utilizing a 2021-era CPU and SSD for JetStream storage. Note that these are **minimum configurations** , and actual production environments may require additional resources.

Cluster Size

CPU cores

Memory

Subscribers

Publishers

Publish Rate msg/s

Total Message Rate msg/s

1

1

32 MiB

1

100

1000

100,000

1

1

64 MiB

1

1000

100

100,000

3

1

32 MiB

1

1000

100

100,000

3

1

64 MiB

1

1000

100

100,000

### 

[hashtag](#with-jetstream)

With JetStream

This table follows the same pattern, with published messages received by a stream using file storage. For a cluster size of three, the stream uses three replicas. Subscribers rely on a "pull consumer" for fetching messages.

Cluster Size

CPU cores

Memory

Subscribers

Publishers

Publish Rate msg/s

Total Message Rate msg/s

1

1

32 MiB

1

10

100

1,000

1

1

32 MiB

1

100

10

1,000

1

1

64 MiB

1

100

100

10,000

1

1

64 MiB

1

1000

10

10,000

3

1

32 MiB

1

100

10

1,000

3

1

64 MiB

1

100

100

10,000

3

1

64 MiB

1

1000

10

10,000

3

1

256 MiB

1

1000

100

100,000

For **production deployment** of JetStream, we recommend starting with **at least 4 CPU cores and 8 GiB of memory** to reduce the risk of resource-related issues.

For recommendations on configuring limits in Kubernetes, see: https://github.com/nats-io/k8s/tree/main/helm/charts/nats#nats-container-resources

## 

[hashtag](#getting-the-binary-from-the-command-line)

Getting the binary from the command line

The simplest way to get the `nats-server` binary for your machine is to use the following shell command.

For example, to get the binary for version 2.11.6:

Copy

```

    curl -fsSL https://binaries.nats.dev/nats-io/nats-server/v2@v2.11.6 | sh

```

To get the latest released version, use `@latest`. You can also use `@main` to get the tip, or use a tag, specific branch, or commit hash after the `@`.

## 

[hashtag](#installing-via-docker)

Installing via Docker

With Docker, you can install the server easily without scattering binaries and other artifacts on your system. The only pre-requisite is to [install dockerarrow-up-right](https://docs.docker.com/install).

Copy

```

    docker pull nats:latest

```

To run NATS on Docker:

Copy

```

    docker run -p 4222:4222 -ti nats:latest

```

Copy

```

    [1] 2019/05/24 15:42:58.228063 [INF] Starting nats-server version #.#.#
    [1] 2019/05/24 15:42:58.228115 [INF] Git commit [#######]
    [1] 2019/05/24 15:42:58.228201 [INF] Starting http monitor on 0.0.0.0:8222
    [1] 2019/05/24 15:42:58.228740 [INF] Listening for client connections on 0.0.0.0:4222
    [1] 2019/05/24 15:42:58.228765 [INF] Server is ready

```

More information on [containerized NATS is available here](https://docs.nats.io/running-a-nats-service/nats_docker) ([local](./../../../09_chevron-right/04_nats-and-docker-chevron-right.md)).

## 

[hashtag](#installing-via-a-package-manager)

Installing via a Package Manager

On Windows, using [scoop.sharrow-up-right](https://scoop.sh):

Copy

```

    scoop install main/nats-server

```

On Mac OS:

Copy

```

    brew install nats-server

```

Arch Linux:

For Arch users, there is an [AUR packagearrow-up-right](https://aur.archlinux.org/packages/nats-server) that you can install with:

Copy

```

    yay -S nats-server

```

To test your installation (provided the executable is visible to your shell):

Typing `nats-server` should output something like

Copy

```

    [41634] 2019/05/13 09:42:11.745919 [INF] Starting nats-server version 2.*.*
    [41634] 2019/05/13 09:42:11.746240 [INF] Listening for client connections on 0.0.0.0:4222
    ...
    [41634] 2019/05/13 09:42:11.746249 [INF] Server id is NBNYNR4ZNTH4N2UQKSAAKBAFLDV3PZO4OUYONSUIQASTQT7BT4ZF6WX7
    [41634] 2019/05/13 09:42:11.746252 [INF] Server is ready

```

## 

[hashtag](#downloading-a-release-build)

Downloading a Release Build

You can find the latest release of nats-server on [the nats-io/nats-server GitHub releases pagearrow-up-right](https://github.com/nats-io/nats-server/releases/).

From the releases page, copy the link to the release archive file of your choice and download it using `curl -L`.

For example, assuming version X.Y.Z of the server and a Linux AMD64:

Copy

```

    curl -L https://github.com/nats-io/nats-server/releases/download/vX.Y.Z/nats-server-vX.Y.Z-linux-amd64.tar.gz -o nats-server.tar.gz

```

Copy

```

    tar -xvzf nats-server.tar.gz

```

Copy

```

    Archive:  nats-server.zip
       creating: nats-server-vX.Y.Z-linux-amd64/
    ...

```

and finally:

Copy

```

    sudo cp nats-server-vX.Y.Z-linux-amd64/nats-server /usr/bin

```

## 

[hashtag](#installing-from-the-source)

Installing From the Source

If you have [Go installedarrow-up-right](https://go.dev/doc/install), installing the binary is easy:

Copy

```

    go install github.com/nats-io/nats-server/v2@main

```

This mechanism will install a build of the [mainarrow-up-right](https://github.com/nats-io/nats-server) branch, which almost certainly will not be a released version. If you are a developer and want to play with the latest, this is the easiest way.

To test your installation (provided $GOPATH/bin is in your path) by typing `nats-server` which should output something like

Copy

```

    [2397474] 2023/09/27 10:32:02.709019 [INF] Starting nats-server
    [2397474] 2023/09/27 10:32:02.709165 [INF]   Version:  2.11.0-dev
    [2397474] 2023/09/27 10:32:02.709182 [INF]   Git:      [not set]
    [2397474] 2023/09/27 10:32:02.709185 [INF]   Name:     NDQU7SGA4ECW4PHL4KNBY42AFQEZDAPMMQZVSQDKGTARZI5JHJV6KO2N
    [2397474] 2023/09/27 10:32:02.709187 [INF]   ID:       NDQU7SGA4ECW4PHL4KNBY42AFQEZDAPMMQZVSQDKGTARZI5JHJV6KO2N
    [2397474] 2023/09/27 10:32:02.709795 [INF] Listening for client connections on 0.0.0.0:4222
    [2397474] 2023/09/27 10:32:02.710173 [INF] Server is ready

```

## 

[hashtag](#building-from-the-source)

Building From the Source

We use goreleaser to build assets published on [GitHub releasesarrow-up-right](https://github.com/nats-io/nats-server/releases). Our builds are fully reproducible, so with Go installed, one can execute the following commands to build from source:

Copy

```

    go install github.com/goreleaser/goreleaser/v2@latest
    
    git clone git@github.com:nats-io/nats-server.git
    cd nats-server
    git checkout v2.12.0 
    [[ `git status --porcelain` ]] && echo "Must have repo in clean state before building"
    
    goreleaser release --skip=announce,publish,validate --clean -f .goreleaser.yml

```

And to verify SHASUMs against our release:

Copy

```

    wget https://github.com/nats-io/nats-server/releases/download/v2.12.0/SHA256SUMS
    diff --color --minimal --context=0 SHA256SUMS dist/SHA256SUMS

```

[PreviousInstalling, running and deploying a NATS Serverchevron-left](https://docs.nats.io/running-a-nats-service/introduction) ([local](./../../../09_chevron-right/01_installing-running-and-deploying-a-nats-server-chevron-right.md))[NextRunning and deploying a NATS Serverchevron-right](https://docs.nats.io/running-a-nats-service/introduction/running) ([local](./running.md))

Last updated 7 months ago

Was this helpful?
