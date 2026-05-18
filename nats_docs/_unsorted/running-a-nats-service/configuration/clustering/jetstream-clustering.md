---
title: JetStream Clustering
source: https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/clustering/jetstream_clustering/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Clustering](https://docs.nats.io/running-a-nats-service/configuration/clustering) ([local](./../clustering.md))

# JetStream Clustering

Clustering in JetStream is required for a highly available and scalable system. Behind clustering is RAFT. There's no need to understand RAFT in depth to use clustering, but knowing a little explains some of the requirements behind setting up JetStream clusters.

## 

[hashtag](#raft)

RAFT

JetStream uses a NATS optimized RAFT algorithm for clustering. Typically RAFT generates a lot of traffic, but the NATS server optimizes this by combining the data plane for replicating messages with the messages RAFT would normally use to ensure consensus. Each server participating requires an unique `server_name` (only applies within the same domain).

### 

[hashtag](#raft-groups)

RAFT Groups

The RAFT groups include API handlers, streams, consumers, and an internal algorithm designates which servers handle which streams and consumers.

The RAFT algorithm has a few requirements:

  * A log to persist state

  * A quorum for consensus

### 

[hashtag](#the-quorum)

The Quorum

In order to ensure data consistency across complete restarts, a quorum of servers is required. A quorum is ½ cluster size + 1. This is the minimum number of nodes to ensure at least one node has the most recent data and state after a catastrophic failure. So for a cluster size of 3, you’ll need at least two JetStream enabled NATS servers available to store new messages. For a cluster size of 5, you’ll need at least 3 NATS servers, and so forth.

### 

[hashtag](#raft-groups-1)

RAFT Groups

**Meta Group** \- all servers join the Meta Group and the JetStream API is managed by this group. A leader is elected and this owns the API and takes care of server placement.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-1e802be26efb0851026ee1112c9d2ee17c73bf89%252Fmeta-group.png%3Falt%3Dmedia%26token%3D89ceb459-4388-4c63-b8a5-171f761756ae&width=768&dpr=3&quality=100&sign=99a8d810&sv=2)

Meta Group

**Stream Group** \- each Stream creates a RAFT group, this group synchronizes state and data between its members. The elected leader handles ACKs and so forth, if there is no leader the stream will not accept messages.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-88e131ba49cdc826a2f0aef966180fee5b3bcdbf%252Fstream-groups.png%3Falt%3Dmedia%26token%3D2e191ff8-c1ab-4d56-a26f-ade28c759272&width=768&dpr=3&quality=100&sign=ab2d2a0&sv=2)

Stream Groups

**Consumer Group** \- each Consumer creates a RAFT group, this group synchronizes consumer state between its members. The group will live on the machines where the Stream Group is and handle consumption ACKs etc. Each Consumer will have their own group.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-d3691663bd3ce8e4173c5649e95b2f11f7543cea%252Fconsumer-groups.png%3Falt%3Dmedia%26token%3D348c7312-206f-410e-bd9d-f605cae53aeb&width=768&dpr=3&quality=100&sign=6e0417d9&sv=2)

Consumer Groups

### 

[hashtag](#cluster-size)

Cluster Size

Generally, we recommend 3 or 5 JetStream enabled servers in a NATS cluster. This balances scalability with a tolerance for failure. For example, if 5 servers are JetStream enabled you would want two servers in one “zone”, two servers in another, and the remaining server in a third. This means you can lose any one “zone” at any time and continue operating.

### 

[hashtag](#mixing-jetstream-enabled-servers-with-standard-nats-servers)

Mixing JetStream enabled servers with standard NATS servers

This is possible and even recommended in some cases. By mixing server types you can dedicate certain machines optimized for storage for Jetstream and others optimized solely for compute for standard NATS servers, reducing operational expense. With the right configuration, the standard servers would handle non-persistent NATS traffic and the JetStream enabled servers would handle JetStream traffic.

## 

[hashtag](#configuration)

Configuration

To configure JetStream clusters, just configure clusters as you normally would by specifying a cluster block in the configuration. Any JetStream enabled servers in the list of clusters will automatically chatter and set themselves up. Unlike core NATS clustering though, each JetStream node **must specify** a server name and cluster name.

Below are explicitly listed server configuration for a three-node cluster across three machines, `n1-c1`, `n2-c1`, and `n3-c1`.

### 

[hashtag](#server-password-configuration)

Server password configuration

A user and password under the [system account ($SYS)](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts#system-account) ([local](./../sys-accounts.md#system-account)) should be configured. The following configuration uses a [bcrypted password](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) ([local](./../securing-nats/auth-intro/username-password.md)): `a very long s3cr3t! password`.

### 

[hashtag](#server-1-host_a)

Server 1 (host_a)

Copy

```

    server_name=n1-c1
    listen=4222
    
    accounts {
      $SYS {
        users = [
          { user: "admin",
            pass: "$2a$11$DRh4C0KNbNnD8K/hb/buWe1zPxEHrLEiDmuq1Mi0rRJiH/W25Qidm"
          }
        ]
      }
    }
    
    jetstream {
       store_dir=/nats/storage
    }
    
    cluster {
      name: C1
      listen: 0.0.0.0:6222
      routes: [
        nats://host_b:6222
        nats://host_c:6222
      ]
    }

```

### 

[hashtag](#server-2-host_b)

Server 2 (host_b)

Copy

```

    server_name=n2-c1
    listen=4222
    
    accounts {
      $SYS {
        users = [
          { user: "admin",
            pass: "$2a$11$DRh4C0KNbNnD8K/hb/buWe1zPxEHrLEiDmuq1Mi0rRJiH/W25Qidm"
          }
        ]
      }
    }
    
    jetstream {
       store_dir=/nats/storage
    }
    
    cluster {
      name: C1
      listen: 0.0.0.0:6222
      routes: [
        nats://host_a:6222
        nats://host_c:6222
      ]
    }

```

### 

[hashtag](#server-3-host_c)

Server 3 (host_c)

Copy

```

    server_name=n3-c1
    listen=4222
    
    accounts {
      $SYS {
        users = [
          { user: "admin",
            pass: "$2a$11$DRh4C0KNbNnD8K/hb/buWe1zPxEHrLEiDmuq1Mi0rRJiH/W25Qidm"
          }
        ]
      }
    }
    
    jetstream {
       store_dir=/nats/storage
    }
    
    cluster {
      name: C1
      listen: 0.0.0.0:6222
      routes: [
        nats://host_a:6222
        nats://host_b:6222
      ]
    }

```

Add nodes as necessary. Choose a data directory that makes sense for your environment, ideally a fast SSD, and launch each server. After two servers are running you'll be ready to use JetStream.

[Previousv2 Routeschevron-left](https://docs.nats.io/running-a-nats-service/configuration/clustering/v2_routes) ([local](./v2-routes.md))[NextAdministrationchevron-right](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/administration) ([local](./jetstream-clustering/administration.md))

Last updated 1 year ago

Was this helpful?
