---
title: JetStream
source: https://docs.nats.io/running-a-nats-service/nats_docker/jetstream_docker
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/running/nats_docker/jetstream_docker.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [NATS and Docker](https://docs.nats.io/running-a-nats-service/nats_docker) ([local](./../../../09_chevron-right/04_nats-and-docker-chevron-right.md))

# JetStream

This mini-tutorial shows how to run a NATS server with JetStream enabled in a local Docker container. This enables quick and consequence-free experimentation with the many features of JetStream.

Using the official `nats` image, start a server. The `-js` option is passed to the server to enable JetStream. The `-p` option forwards your local 4222 port to the server inside the container, 4222 is the default client connection port.

Copy

```

    docker run -p 4222:4222 nats -js

```

To persist JetStream data to a volume, you can use the `-v` option in combination with `-sd`:

Copy

```

    docker run -p 4222:4222 -v nats:/data nats -js -sd /data

```

With the server running, use `nats bench` to create a stream and publish some messages to it.

Copy

```

    nats bench -s localhost:4222 benchsubject --js --pub 1 --msgs=100000

```

JetStream persists the messages (on disk by default). Now consume them with:

Copy

```

    nats bench -s localhost:4222 benchsubject --js --sub 3 --msgs=100000

```

You can use `nats` to inspect various aspects of the stream, for example:

Copy

```

    nats -s localhost:4222 stream list
    ╭────────────────────────────────────────────────────────────────────────────────────╮
    │                                       Streams                                      │
    ├─────────────┬─────────────┬─────────────────────┬──────────┬────────┬──────────────┤
    │ Name        │ Description │ Created             │ Messages │ Size   │ Last Message │
    ├─────────────┼─────────────┼─────────────────────┼──────────┼────────┼──────────────┤
    │ benchstream │             │ 2024-06-07 20:26:38 │ 100,000  │ 16 MiB │ 35s          │
    ╰─────────────┴─────────────┴─────────────────────┴──────────┴────────┴──────────────╯

```

### 

[hashtag](#related-and-useful)

Related and useful:

  * Official [Docker image for the NATS server on GitHubarrow-up-right](https://github.com/nats-io/nats-docker) and [issuesarrow-up-right](https://github.com/nats-io/nats-docker/issues)

  * [`nats` images on DockerHubarrow-up-right](https://hub.docker.com/_/nats)

  * [`nats` CLI tool](https://docs.nats.io/using-nats/nats-tools/nats_cli) ([local](./../../using-nats/nats-tools/nats-cli.md)) and [`nats bench`arrow-up-right](https://github.com/nats-io/nats.docs/blob/master/using-nats/nats-tools/nats_cli/natsbench/README.md)

  * [`Administer JetStream`arrow-up-right](https://github.com/nats-io/nats.docs/blob/master/nats_admin/jetstream_admin/README.md)

[PreviousPython and NGS Running in Dockerchevron-left](https://docs.nats.io/running-a-nats-service/nats_docker/ngs-docker-python) ([local](./ngs-docker-python.md))[NextNGS Leaf Nodeschevron-right](https://docs.nats.io/running-a-nats-service/nats_docker/ngs-leafnodes-docker) ([local](./ngs-leafnodes-docker.md))

Last updated 1 year ago

Was this helpful?
