---
title: Object Store
source: https://docs.nats.io/nats-concepts/jetstream/obj_store
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/object-store/obj_store.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../_unsorted/nats-concepts.md))chevron-right
  2. [JetStream](https://docs.nats.io/nats-concepts/jetstream) ([local](./../05_chevron-right/08_jetstream-chevron-right.md))

# Object Store

JetStream, the persistence layer of NATS, not only allows for the higher qualities of service and features associated with 'streaming', but it also enables some functionalities not found in messaging systems.

One such feature is the Object store functionality, which allows client applications to create `buckets` (corresponding to streams) that can store a set of files. Files are stored and transmitted in chunks, allowing files of arbitrary size to be transferred safely over the NATS infrastructure.

**Note:** Object store is not a distributed storage system. All files in a bucket will need to fit on the target file system.

  * [Walkthrough](https://docs.nats.io/nats-concepts/jetstream/obj_store/obj_walkthrough) ([local](./../_unsorted/nats-concepts/jetstream/obj-store/obj-walkthrough.md))

  * [Details](https://docs.nats.io/using-nats/developer/develop_jetstream/object) ([local](./../_unsorted/using-nats/developer/develop-jetstream/object.md))

## 

[hashtag](#basic-capabilities)

Basic Capabilities

The Object Store implements a chunking mechanism, allowing you to for example store and retrieve files (i.e. the object) of any size by associating them with a path or file name as the key.

  * `add` a `bucket` to hold the files.

  * `put` Add a file to the bucket

  * `get` Retrieve the file and store it to a designated location

  * `del` Delete a file

## 

[hashtag](#advanced-capabilities)

Advanced Capabilities

  * `watch` Subscribe to changes in the bucket. Will receive notifications on successful `put` and `del` operations.

[PreviousKey/Value Store Walkthroughchevron-left](https://docs.nats.io/nats-concepts/jetstream/key-value-store/kv_walkthrough) ([local](./../_unsorted/nats-concepts/jetstream/key-value-store/kv-walkthrough.md))[NextObject Store Walkthroughchevron-right](https://docs.nats.io/nats-concepts/jetstream/obj_store/obj_walkthrough) ([local](./../_unsorted/nats-concepts/jetstream/obj-store/obj-walkthrough.md))

Last updated 1 year ago

Was this helpful?
