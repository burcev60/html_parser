---
title: Example
source: https://docs.nats.io/nats-concepts/jetstream/source_and_mirror/source_and_mirror_example
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/source_and_mirror_example.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../../nats-concepts.md))chevron-right
  2. [JetStream](https://docs.nats.io/nats-concepts/jetstream) ([local](./../../../../05_chevron-right/08_jetstream-chevron-right.md))chevron-right
  3. [Source and Mirror Streams](https://docs.nats.io/nats-concepts/jetstream/source_and_mirror) ([local](./../source-and-mirror.md))

# Example

Streams with source and mirror configurations are best managed through a client API. If you intend to create such a configuration from command line with NATS CLI you should use a JSON configuration.

Copy

```

    nats stream add --config stream_with_sources.json

```

## 

[hashtag](#example-stream-configuration-with-two-sources)

Example stream configuration with two sources

**Minimal example**

Copy

```

    {
      "name": "SOURCE_TARGET",
      "subjects": [
        "foo1.ext.*",
        "foo2.ext.*"
      ],
      "discard": "old",
      "duplicate_window": 120000000000,
      "sources": [
        {
          "name": "SOURCE1_ORIGIN"
        }
      ],
      "deny_delete": false,
      "sealed": false,
      "max_msg_size": -1,
      "allow_rollup_hdrs": false,
      "max_bytes": -1,
      "storage": "file",
      "allow_direct": false,
      "max_age": 0,
      "max_consumers": -1,
      "max_msgs_per_subject": -1,
      "num_replicas": 1,
      "name": "SOURCE_TARGET",
      "deny_purge": false,
      "compression": "none",
      "max_msgs": -1,
      "retention": "limits",
      "mirror_direct": false
    }

```

**With additional options**

Copy

```

    {
      "name": "SOURCE_TARGET",
      "subjects": [
        "foo1.ext.*",
        "foo2.ext.*"
      ],
      "discard": "old",
      "duplicate_window": 120000000000,
      "sources": [
        {
          "name": "SOURCE1_ORIGIN",
          "filter_subject": "foo1.bar",
          "opt_start_seq": 42,
          "external": {
            "deliver": "",
            "api": "$JS.domainA.API"
          }
        },
        {
          "name": "SOURCE2_ORIGIN",
          "filter_subject": "foo2.bar"
        }
      ],
      "consumer_limits": {
        
      },
      "deny_delete": false,
      "sealed": false,
      "max_msg_size": -1,
      "allow_rollup_hdrs": false,
      "max_bytes": -1,
      "storage": "file",
      "allow_direct": false,
      "max_age": 0,
      "max_consumers": -1,
      "max_msgs_per_subject": -1,
      "num_replicas": 1,
      "name": "SOURCE_TARGET",
      "deny_purge": false,
      "compression": "none",
      "max_msgs": -1,
      "retention": "limits",
      "mirror_direct": false
    }

```

## 

[hashtag](#example-stream-configuration-with-mirror)

Example stream configuration with mirror

**Minimal example**

Copy

```

    {
      "name": "MIRROR_TARGET"
      "discard": "old",
      "mirror": {
        "name": "MIRROR_ORIGIN"
      },
      "deny_delete": false,
      "sealed": false,
      "max_msg_size": -1,
      "allow_rollup_hdrs": false,
      "max_bytes": -1,
      "storage": "file",
      "allow_direct": false,
      "max_age": 0,
      "max_consumers": -1,
      "max_msgs_per_subject": -1,
      "num_replicas": 1,
      "name": "MIRROR_TARGET",
      "deny_purge": false,
      "compression": "none",
      "max_msgs": -1,
      "retention": "limits",
      "mirror_direct": false
    }

```

**With additional options**

Copy

```

    {
      "name": "MIRROR_TARGET"
      "discard": "old",
      "mirror": {
        "opt_start_time": "2024-07-11T08:57:20.4441646Z",
        "external": {
          "deliver": "",
          "api": "$JS.domainB.API"
        },
        "name": "MIRROR_ORIGIN"
      },
      "consumer_limits": {
        
      },
      "deny_delete": false,
      "sealed": false,
      "max_msg_size": -1,
      "allow_rollup_hdrs": false,
      "max_bytes": -1,
      "storage": "file",
      "allow_direct": false,
      "max_age": 0,
      "max_consumers": -1,
      "max_msgs_per_subject": -1,
      "num_replicas": 1,
      "name": "MIRROR_TARGET",
      "deny_purge": false,
      "compression": "none",
      "max_msgs": -1,
      "retention": "limits",
      "mirror_direct": false
    }

```

[PreviousSource and Mirror Streamschevron-left](https://docs.nats.io/nats-concepts/jetstream/source_and_mirror) ([local](./../source-and-mirror.md))[NextConsumerschevron-right](https://docs.nats.io/nats-concepts/jetstream/consumers) ([local](./../consumers.md))

Last updated 4 days ago

Was this helpful?
