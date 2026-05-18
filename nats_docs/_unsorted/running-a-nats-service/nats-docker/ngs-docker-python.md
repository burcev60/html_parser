---
title: Python and NGS Running in Docker
source: https://docs.nats.io/running-a-nats-service/nats_docker/ngs-docker-python
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/running/nats_docker/ngs-docker-python.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [NATS and Docker](https://docs.nats.io/running-a-nats-service/nats_docker) ([local](./../../../09_chevron-right/04_nats-and-docker-chevron-right.md))

# Python and NGS Running in Docker

Start a lightweight Docker container:

Copy

```

    docker run --entrypoint /bin/bash -it python:3.8-slim-buster

```

Or you can also mount local creds via a volume:

Copy

```

    docker run --entrypoint /bin/bash -v $HOME/.nkeys/creds/synadia/NGS/:/creds -it python:3.8-slim-buster

```

Install nats.py and dependencies to install nkeys:

Copy

```

    apt-get update && apt-get install -y build-essential curl
    pip install asyncio-nats-client[nkeys]

```

Get the Python examples using curl:

Copy

```

    curl -o nats-pub.py -O -L https://raw.githubusercontent.com/nats-io/nats.py/master/examples/nats-pub/__main__.py
    curl -o nats-sub.py -O -L https://raw.githubusercontent.com/nats-io/nats.py/master/examples/nats-sub/__main__.py

```

Create a subscription that lingers:

Copy

```

    python nats-sub.py --creds /creds/NGS.creds  -s tls://connect.ngs.global:4222 hello &

```

Publish a message:

Copy

```

    python nats-pub.py --creds /creds/NGS.creds  -s tls://connect.ngs.global:4222 hello -d world

```

[PreviousDocker Swarmchevron-left](https://docs.nats.io/running-a-nats-service/nats_docker/docker_swarm) ([local](./docker-swarm.md))[NextJetStreamchevron-right](https://docs.nats.io/running-a-nats-service/nats_docker/jetstream_docker) ([local](./jetstream-docker.md))

Last updated 4 years ago

Was this helpful?
