---
title: v2 Routes
source: https://docs.nats.io/running-a-nats-service/configuration/clustering/v2_routes
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/clustering/v2_routes.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [Clustering](https://docs.nats.io/running-a-nats-service/configuration/clustering) ([local](./../clustering.md))

# v2 Routes

 _Introduced in NATS v2.10.0_

## 

[ hashtag](#connection-pooling)

Connection pooling

Before the v2.10.0 release, two servers in a cluster had only one connection to transmit all messages for all accounts, which could lead to slow down and increased memory usage when data was not transmitted fast enough.

The v2.10.0 release introduces the ability to have multiple route connections between two servers. By default, without any configuration change, clustering two v2.10.0+ servers together will create 3 route connections. This can of course be configured to a different value by explicitly configuring the pool size.

Copy

```

    cluster {
      pool_size: 3
    }

```

### 

[hashtag](#pool-size-requirements)

Pool size requirements

Each of those connections will handle a specific subset of the accounts, and the assignment of an account to a specific connection index in the pool is the same in any server in the cluster. It is required that each server in the cluster have the same pool size value, otherwise, clustering will fail to be established with an error similar to:

Copy

```

    [ERR] 127.0.0.1:6222 - rid:6 - Mismatch route pool size: 3 vs 4

```

### 

[hashtag](#handling-loss-of-connection)

Handling loss of connection

In the event that a given connection of the pool breaks, automatic reconnection occurs as usual. However, while the disconnection is happening, traffic for accounts handled by that connection is stopped (that is, traffic is not routed through other connections), the same way that it was when there was a single route connection.

### 

[hashtag](#configuration-reload)

Configuration reload

Note that although the cluster's `pool_size` configuration parameter can be changed through a configuration reload, connections between servers will likely break since there will be a mismatch between servers. It is possible though to do a rolling reload by setting the same value on all servers. Client and other connections (including dedicated account routes - see next section) will not be closed.

### 

[hashtag](#monitoring)

Monitoring

When monitoring is enabled, you will see that the `/routez` page now has more connections than before, which is expected.

### 

[hashtag](#disabling-connection-pooling)

Disabling connection pooling

It is possible to disable route connection pooling by setting the `pool_size` configuration parameter to the value `-1`. When that is the case, a server will behave as a server pre-v2.10.0 and create a single route connection between its peers.

Note that in that mode, no `accounts` list can be defined (see "Accounts Pinning" below).

## 

[hashtag](#account-pinning)

Account pinning

In addition to connection pooling, the release v2.10.0 has introduced the ability to configure a list of accounts that will have a dedicated route connection.

Copy

```

    cluster {
      accounts: [acc1, acc2]
    }

```

Note that by default, the server will create a dedicated route for the system account (no specific configuration is needed).

Having a dedicated route improves performance and reduces latency, but another benefit is that since the route is dedicated to an account, the account name does not need to be added to the message route protocols. Since account names can be quite long, this reduces the number of bytes that need to be transmitted in all other cases.

### 

[hashtag](#handling-loss-of-connection-1)

Handling loss of connection

In the event that an account route connection breaks, automatic reconnection occurs as usual. However, while the disconnection is happening, traffic for this account is stopped.

### 

[hashtag](#configuration-reload-1)

Configuration reload

The `accounts` list can be modified and a configuration signal be sent to the server. All servers need to have the same list, however, it is possible to perform a rolling configuration reload.

For instance, adding an account to the list of server `A` and issuing a configuration reload will not produce an error, even though the other server in the cluster does not have that account in the list yet. A dedicated connection will not yet be established, but traffic for this account in the pooled connection currently handling it will stop. When the configuration reload happens on the other server, a dedicated connection will then be established and this account’s traffic will resume.

When removing an account from the list and issuing a configuration reload, the connection for this account will be closed, and traffic for this account will stop. Other server(s) that still have this account configured with a dedicated connection will fail to reconnect. When they are also sent the configuration reload (with updated `accounts` configuration), the account traffic will now be handled by a connection in the pool.

Note that configuration reload of changes in the `accounts` list do not affect existing pool connections, and therefore should not affect traffic for other accounts.

### 

[hashtag](#monitoring-1)

Monitoring

When monitoring is enabled, the route connection's information now has a new field called `account` that displays the name of the account this route is for.

### 

[hashtag](#disabling-connection-pooling-1)

Disabling connection pooling

As indicated in the connection pooling section, if `pool_size` is set to `-1`, the `accounts` list cannot be configured nor would be in use.

### 

[hashtag](#connecting-to-an-older-server)

Connecting to an older server

Although it is recommended that all servers part of the same cluster be at the same version number, a v2.10.0 server will be able to connect to an older server and in that case create a single route to that server. This allows for an easy deployment of a v2.10.0 release into an existing cluster running an older release.

## 

[hashtag](#compression)

Compression

Release v2.10.0 introduces the ability to configure compression between servers having route connections. The current compression algorithm used is [S2, an extension of Snappyarrow-up-right](https://github.com/klauspost/compress/tree/master/s2#s2-compression). By default, routes do not use compression and it needs to be explicitly enabled.

Copy

```

    cluster {
      compression: {
        mode: accept
      }
    }

```

### 

[hashtag](#compression-modes)

Compression Modes

There are several modes of compression and there is no requirement to have the same mode between routed servers.

  * `off` \- Explicitly disables compression for any route between the server and a peer.

  * `accept` (default) - Does not initiate compression, but will accept the compression mode of the peer it connects to.

  * `s2_fast` \- Applies compression, but optimizes for speed over compression ratio.

  * `s2_better` \- Applies compression, providing a balance of speed and compression ratio.

  * `s2_best` \- Applies compression and optimizes for compression ratio over speed.

  * `s2_auto` \- Choose the appropriate `s2_*` mode relative to the round-trip time (RTT) measured between the server and the peer. See `rtt_thresholds` below.

### 

[hashtag](#round-trip-time-thresholds)

Round-trip time thresholds

When `s2_auto` compression is used, it relies on a `rtt_thresholds` option, which is a list of three latency thresholds that dictate increasing or decreasing the compression mode.

Copy

```

    cluster {
      compression: {
        mode: s2_auto
        rtt_thresholds: [10ms, 50ms, 100ms]
      }
    }

```

The default `rtt_thresholds` value is `[10ms, 50ms, 100ms]`. The way to read this is that if the RTT is under 10ms, no compression is applied. Once 10ms is reached, `s2_fast` is applied and so on with the remaining two thresholds for `s2_better` and `s2_best`.

### 

[hashtag](#configuration-reload-2)

Configuration reload

The `compression` configuration can be changed through configuration reload. If the value is changed from `off` to anything else, then connections are closed and recreated, same as if the compression mode was set to something and disabled by setting it to `off`.

For all other compression modes, the mode is changed dynamically without a need to close the route connections.

### 

[hashtag](#monitoring-2)

Monitoring

When monitoring is enabled, the route connection's information now has a new field called `compression` that displays the current compression mode. It can be `off` or any other mode described above. Note that `s2_auto` is not displayed, instead, what will be displayed is the _current mode_ , say `s2_best` or `s2_uncompressed`.

If connected to an older server, the `compression` field will display `not supported`.

### 

[hashtag](#connecting-to-an-older-server-1)

Connecting to an older server

It is possible to have a v2.10.0+ server, with a compression mode configured, connect to an older server that does not support compression. The connection will simply not use compression.

[PreviousClustering Configurationchevron-left](https://docs.nats.io/running-a-nats-service/configuration/clustering/cluster_config) ([local](./cluster-config.md))[NextJetStream Clusteringchevron-right](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering) ([local](./jetstream-clustering.md))

Last updated 2 years ago

Was this helpful?
