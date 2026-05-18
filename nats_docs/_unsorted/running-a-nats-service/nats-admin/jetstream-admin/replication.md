---
title: Data Replication
source: https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/replication
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/jetstream_admin/replication.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../running-a-nats-service.md))chevron-right
  2. [Managing and Monitoring your NATS Server Infrastructure](https://docs.nats.io/running-a-nats-service/nats_admin) ([local](./../../../../09_chevron-right/10_managing-and-monitoring-your-nats-server-infrastructure-chev.md))chevron-right
  3. [Managing JetStream](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin) ([local](./../jetstream-admin.md))

# Data Replication

Replication allows you to move data between streams in either a 1:1 mirror style or by multiplexing multiple source streams into a new stream. In future builds this will allow data to be replicated between accounts as well, ideal for sending data from a Leafnode into a central store.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-866a502a8129bcaeefac6f5cac01071bb22d05e7%252Freplication.png%3Falt%3Dmedia%26token%3D71571c07-72d5-4eba-86aa-42c5dd4dd070&width=768&dpr=3&quality=100&sign=ac8d0434&sv=2)

Here we have 2 main streams - _ORDERS_ and _RETURNS_ \- these streams are clustered across 3 nodes. These Streams have short retention periods and are memory based.

We create a _ARCHIVE_ stream that has 2 _sources_ set, the _ARCHIVE_ will pull data from the sources into itself. This stream has a very long retention period and is file based and replicated across 3 nodes. Additional messages can be added to the ARCHIVE by sending to it directly.

Finally, we create a _REPORT_ stream mirrored from _ARCHIVE_ that is not clustered and retains data for a month. The _REPORT_ Stream does not listen for any incoming messages, it can only consume data from _ARCHIVE_.

## 

[hashtag](#mirrors)

Mirrors

A _mirror_ copies data from 1 other stream, as far as possible IDs and ordering will match exactly the source. A _mirror_ does not listen on a subject for any data to be added. A _mirror_ can filter by subject and the Start Sequence and Start Time can be set. A stream can only have 1 _mirror_ and if it is a mirror it cannot also have any _source_.

## 

[hashtag](#sources)

Sources

A _source_ is a stream where data is copied from, one stream can have multiple sources and will read data in from them all. The stream will also listen for messages on it's own subject. We can therefore not maintain absolute ordering, but data from 1 single source will be in the correct order but mixed in with other streams. You might also find the timestamps of streams can be older and newer mixed in together as a result.

A Stream with sources may also listen on subjects, but could have no listening subject. When using the `nats` CLI to create sourced streams use `--subjects` to supply subjects to listen on.

A source can have Start Time or Start Sequence and can filter by a subject.

## 

[hashtag](#configuration)

Configuration

The ORDERS and RETURNS streams as normal, I will not show how to create them.

Copy

```

    nats s report

```

Copy

```

    Obtaining Stream stats
    
    +---------+---------+-----------+----------+-------+------+---------+----------------------+
    | Stream  | Storage | Consumers | Messages | Bytes | Lost | Deleted | Cluster              |
    +---------+---------+-----------+----------+-------+------+---------+----------------------+
    | ORDERS  | Memory  | 0         | 0        | 0 B   | 0    | 0       | n1-c2, n2-c2*, n3-c2 |
    | RETURNS | Memory  | 0         | 0        | 0 B   | 0    | 0       | n1-c2*, n2-c2, n3-c2 |
    +---------+---------+-----------+----------+-------+------+---------+----------------------+

```

We now add the ARCHIVE:

Copy

```

    nats s add ARCHIVE --source ORDERS --source RETURNS

```

Copy

```

    ? Storage backend file
    ? Retention Policy Limits
    ? Discard Policy Old
    ? Stream Messages Limit -1
    ? Message size limit -1
    ? Maximum message age limit -1
    ? Maximum individual message size -1
    ? Duplicate tracking time window 2m0s
    ? Allow message Roll-ups No
    ? Allow message deletion Yes
    ? Allow purging subjects or the entire stream Yes
    ? Replicas 1
    ? Adjust source "ORDERS" start Yes
    ? ORDERS Source Start Sequence 0
    ? ORDERS Source UTC Time Stamp (YYYY:MM:DD HH:MM:SS)
    ? ORDERS Source Filter source by subject
    ? Import "ORDERS" from a different JetStream domain No
    ? Import "ORDERS" from a different account No
    ? Adjust source "RETURNS" start No
    ? Import "RETURNS" from a different JetStream domain No
    ? Import "RETURNS" from a different account No
    Stream ARCHIVE was created
    
    Information for Stream ARCHIVE created 2022-01-21T11:49:52-08:00
    
    Configuration:
    
         Acknowledgements: true
                Retention: File - Limits
                 Replicas: 1
           Discard Policy: Old
         Duplicate Window: 2m0s
        Allows Msg Delete: true
             Allows Purge: true
           Allows Rollups: false
         Maximum Messages: unlimited
            Maximum Bytes: unlimited
              Maximum Age: unlimited
     Maximum Message Size: unlimited
        Maximum Consumers: unlimited
                  Sources: ORDERS
                           RETURNS
    
    
    State:
    
                 Messages: 0
                    Bytes: 0 B
                 FirstSeq: 0
                  LastSeq: 0
         Active Consumers: 0

```

And we add the REPORT:

Copy

```

    nats s add REPORT --mirror ARCHIVE

```

Copy

```

    ? Storage backend file
    ? Retention Policy Limits
    ? Discard Policy Old
    ? Stream Messages Limit -1
    ? Message size limit -1
    ? Maximum message age limit -1
    ? Maximum individual message size -1
    ? Allow message Roll-ups No
    ? Allow message deletion Yes
    ? Allow purging subjects or the entire stream Yes
    ? Replicas 1
    ? Adjust mirror start No
    ? Import mirror from a different JetStream domain No
    ? Import mirror from a different account No
    Stream REPORT was created
    
    Information for Stream REPORT created 2022-01-21T11:50:55-08:00
    
    Configuration:
    
         Acknowledgements: true
                Retention: File - Limits
                 Replicas: 1
           Discard Policy: Old
         Duplicate Window: 2m0s
        Allows Msg Delete: true
             Allows Purge: true
           Allows Rollups: false
         Maximum Messages: unlimited
            Maximum Bytes: unlimited
              Maximum Age: unlimited
     Maximum Message Size: unlimited
        Maximum Consumers: unlimited
                   Mirror: ARCHIVE
    
    
    State:
    
                 Messages: 0
                    Bytes: 0 B
                 FirstSeq: 0
                  LastSeq: 0
         Active Consumers: 0

```

When configured we'll see some additional information in a `nats stream info` output:

Copy

```

    nats stream info ARCHIVE

```

Output extract

Copy

```

    ...
    Source Information:
    
              Stream Name: ORDERS
                      Lag: 0
                Last Seen: 2m23s
    
              Stream Name: RETURNS
                      Lag: 0
                Last Seen: 2m15s
    ...
    
    $ nats stream info REPORT
    ...
    Mirror Information:
    
              Stream Name: ARCHIVE
                      Lag: 0
                Last Seen: 2m35s
    ...

```

Here the `Lag` is how far behind we were reported as being last time we saw a message.

We can confirm all our setup using a `nats stream report`:

Copy

```

    nats s report

```

Copy

```

    +--------------------------------------------------------------------------------------------------------+
    |                                            Stream Report                                               |
    +---------+---------+-------------+-----------+----------+-------+------+---------+----------------------+
    | Stream  | Storage | Replication | Consumers | Messages | Bytes | Lost | Deleted | Cluster              |
    +---------+---------+-------------+-----------+----------+-------+------+---------+----------------------+
    | ARCHIVE | File    | Sourced     | 1         | 0        | 0 B   | 0    | 0       | n1-c2*, n2-c2, n3-c2 |
    | ORDERS  | Memory  |             | 1         | 0        | 0 B   | 0    | 0       | n1-c2, n2-c2*, n3-c2 |
    | REPORT  | File    | Mirror      | 0         | 0        | 0 B   | 0    | 0       | n1-c2*               |
    | RETURNS | Memory  |             | 1         | 0        | 0 B   | 0    | 0       | n1-c2, n2-c2, n3-c2* |
    +---------+---------+-------------+-----------+----------+-------+------+---------+----------------------+
    
    +---------------------------------------------------------+
    |                   Replication Report                    |
    +---------+--------+---------------+--------+-----+-------+
    | Stream  | Kind   | Source Stream | Active | Lag | Error |
    +---------+--------+---------------+--------+-----+-------+
    | ARCHIVE | Source | ORDERS        | never  | 0   |       |
    | ARCHIVE | Source | RETURNS       | never  | 0   |       |
    | REPORT  | Mirror | ARCHIVE       | never  | 0   |       |
    +---------+--------+---------------+--------+-----+-------+

```

We then create some data in both ORDERS and RETURNS:

Copy

```

    nats req ORDERS.new "ORDER {{Count}}" --count 100
    nats req RETURNS.new "RETURN {{Count}}" --count 100

```

We can now see from a Stream Report that the data has been replicated:

Copy

```

    nats s report --dot replication.dot

```

Copy

```

    Obtaining Stream stats
    
    +---------+---------+-----------+----------+---------+------+---------+----------------------+
    | Stream  | Storage | Consumers | Messages | Bytes   | Lost | Deleted | Cluster              |
    +---------+---------+-----------+----------+---------+------+---------+----------------------+
    | ORDERS  | Memory  | 1         | 100      | 3.3 KiB | 0    | 0       | n1-c2, n2-c2*, n3-c2 |
    | RETURNS | Memory  | 1         | 100      | 3.5 KiB | 0    | 0       | n1-c2*, n2-c2, n3-c2 |
    | ARCHIVE | File    | 1         | 200      | 27 KiB  | 0    | 0       | n1-c2, n2-c2, n3-c2* |
    | REPORT  | File    | 0         | 200      | 27 KiB  | 0    | 0       | n1-c2*               |
    +---------+---------+-----------+----------+---------+------+---------+----------------------+
    
    +---------------------------------------------------------+
    |                   Replication Report                    |
    +---------+--------+---------------+--------+-----+-------+
    | Stream  | Kind   | Source Stream | Active | Lag | Error |
    +---------+--------+---------------+--------+-----+-------+
    | ARCHIVE | Source | ORDERS        | 14.48s | 0   |       |
    | ARCHIVE | Source | RETURNS       | 9.83s  | 0   |       |
    | REPORT  | Mirror | ARCHIVE       | 9.82s  | 0   |       |
    +---------+--------+---------------+--------+-----+-------+

```

Here we also pass the `--dot replication.dot` argument that writes a GraphViz format map of the replication setup.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-7d14c7d0e31828d5f2e59d0b6f98b18e32d9851b%252Freplication-setup.png%3Falt%3Dmedia%26token%3D72f9676c-5c53-4155-8d17-25652f543470&width=768&dpr=3&quality=100&sign=9ce996b9&sv=2)

[PreviousConsumerschevron-left](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/consumers) ([local](./consumers.md))[NextDisaster Recoverychevron-right](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/disaster_recovery) ([local](./disaster-recovery.md))

Last updated 3 years ago

Was this helpful?
