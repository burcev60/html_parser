---
title: Tutorial
source: https://docs.nats.io/using-nats/nats-tools/nats_top/nats-top-tutorial
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/nats-tools/nats_top/nats-top-tutorial.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [NATS Tools](https://docs.nats.io/using-nats/nats-tools) ([local](./../../../../07_chevron-right/01_nats-tools-chevron-right.md))chevron-right
  3. [nats-top](https://docs.nats.io/using-nats/nats-tools/nats_top) ([local](./../nats-top.md))

# Tutorial

You can use [nats-toparrow-up-right](https://github.com/nats-io/nats-top) to monitor in realtime NATS server connections and message statistics.

## 

[hashtag](#prerequisites)

Prerequisites

  * [Set up your Go environmentarrow-up-right](https://golang.org/doc/install)

  * [Install the NATS server](https://docs.nats.io/running-a-nats-service/introduction/installation) ([local](./../../../running-a-nats-service/introduction/installation.md))

## 

[hashtag](#id-1.-install-nats-top)

1\. Install nats-top

Copy

```

    go install github.com/nats-io/nats-top@latest

```

You may need to run the following instead:

Copy

```

    sudo -E go install github.com/nats-io/nats-top

```

## 

[hashtag](#id-2.-start-the-nats-server-with-monitoring-enabled)

2\. Start the NATS server with monitoring enabled

Copy

```

    nats-server -m 8222

```

## 

[hashtag](#id-3.-start-nats-top)

3\. Start nats-top

Copy

```

    nats-top

```

Result:

Copy

```

    nats-server version 0.6.6 (uptime: 2m2s)
    Server:
      Load: CPU:  0.0%  Memory: 6.3M  Slow Consumers: 0
      In:   Msgs: 0  Bytes: 0  Msgs/Sec: 0.0  Bytes/Sec: 0
      Out:  Msgs: 0  Bytes: 0  Msgs/Sec: 0.0  Bytes/Sec: 0
    
    Connections: 0
      HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION

```

## 

[hashtag](#id-4.-run-nats-client-programs)

4\. Run NATS client programs

Run some NATS client programs and exchange messages.

For the best experience, you will want to run multiple subscribers, at least 2 or 3. Refer to the [example pub-sub clients](https://docs.nats.io/running-a-nats-service/clients) ([local](./../../../../09_chevron-right/07_nats-server-clients.md)).

## 

[hashtag](#id-5.-check-nats-top-for-statistics)

5\. Check nats-top for statistics

Copy

```

    nats-server version 0.6.6 (uptime: 30m51s)
    Server:
      Load: CPU:  0.0%  Memory: 10.3M  Slow Consumers: 0
      In:   Msgs: 56  Bytes: 302  Msgs/Sec: 0.0  Bytes/Sec: 0
      Out:  Msgs: 98  Bytes: 512  Msgs/Sec: 0.0  Bytes/Sec: 0
    
    Connections: 3
      HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION
      ::1:58651            6        1       0           52          0           260         0           go       1.1.0
      ::1:58922            38       1       0           21          0           105         0           go       1.1.0
      ::1:58953            39       1       0           21          0           105         0           go       1.1.0

```

## 

[hashtag](#id-6.-sort-nats-top-statistics)

6\. Sort nats-top statistics

In nats-top, enter the command `o` followed by the option, such as `bytes_to`. You see that nats-top sorts the BYTES_TO column in ascending order.

Copy

```

    nats-server version 0.6.6 (uptime: 45m40s)
    Server:
      Load: CPU:  0.0%  Memory: 10.4M  Slow Consumers: 0
      In:   Msgs: 81  Bytes: 427  Msgs/Sec: 0.0  Bytes/Sec: 0
      Out:  Msgs: 154  Bytes: 792  Msgs/Sec: 0.0  Bytes/Sec: 0
    sort by [bytes_to]:
    Connections: 3
      HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION
      ::1:59259            83       1       0           4           0           20          0           go       1.1.0
      ::1:59349            91       1       0           2           0           10          0           go       1.1.0
      ::1:59342            90       1       0           0           0           0           0           go       1.1.0

```

## 

[hashtag](#id-7.-use-different-sort-options)

7\. Use different sort options

Use some different sort options to explore nats-top, such as:

`cid`, `subs`, `pending`, `msgs_to`, `msgs_from`, `bytes_to`, `bytes_from`, `lang`, `version`

You can also set the sort option on the command line using the `-sort` flag. For example: `nats-top -sort bytes_to`.

## 

[hashtag](#id-8.-display-the-registered-subscriptions)

8\. Display the registered subscriptions.

In nats-top, enter the command `s` to toggle displaying connection subscriptions. When enabled, you see the subscription subject in nats-top table:

Copy

```

    nats-server version 0.6.6 (uptime: 1h2m23s)
    Server:
      Load: CPU:  0.0%  Memory: 10.4M  Slow Consumers: 0
      In:   Msgs: 108  Bytes: 643  Msgs/Sec: 0.0  Bytes/Sec: 0
      Out:  Msgs: 185  Bytes: 1.0K  Msgs/Sec: 0.0  Bytes/Sec: 0
    
    Connections: 3
      HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION SUBSCRIPTIONS
      ::1:59708            115      1       0           6           0           48          0           go       1.1.0   foo.bar
      ::1:59758            122      1       0           1           0           8           0           go       1.1.0   foo
      ::1:59817            124      1       0           0           0           0           0           go       1.1.0   foo

```

## 

[hashtag](#id-9.-quit-nats-top)

9\. Quit nats-top

Use the `q` command to quit nats-top.

## 

[hashtag](#id-10.-restart-nats-top-with-a-specified-query)

10\. Restart nats-top with a specified query

For example, to query for the connection with largest number of subscriptions:

Copy

```

    nats-top -n 1 -sort subs

```

Result: nats-top displays only the client connection with the largest number of subscriptions:

Copy

```

    nats-server version 0.6.6 (uptime: 1h7m0s)
    Server:
      Load: CPU:  0.0%  Memory: 10.4M  Slow Consumers: 0
      In:   Msgs: 109  Bytes: 651  Msgs/Sec: 0.0  Bytes/Sec: 0
      Out:  Msgs: 187  Bytes: 1.0K  Msgs/Sec: 0.0  Bytes/Sec: 0
    
    Connections: 3
      HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION
      ::1:59708            115      1       0           6           0           48          0           go       1.1.0

```

[Previousnats-topchevron-left](https://docs.nats.io/using-nats/nats-tools/nats_top) ([local](./../nats-top.md))[NextDeveloping With NATSchevron-right](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))

Last updated 1 year ago

Was this helpful?
