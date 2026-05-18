---
title: Object Store Walkthrough
source: https://docs.nats.io/nats-concepts/jetstream/obj_store/obj_walkthrough
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/object-store/obj_walkthrough.md)chevron-down

block-quoteOn this pageblock-quote

  1. [NATS Concepts](https://docs.nats.io/nats-concepts) ([local](./../../../nats-concepts.md))chevron-right
  2. [JetStream](https://docs.nats.io/nats-concepts/jetstream) ([local](./../../../../05_chevron-right/08_jetstream-chevron-right.md))chevron-right
  3. [Object Store](https://docs.nats.io/nats-concepts/jetstream/obj_store) ([local](./../../../../14_hashtag-guided-tour/03_object-store.md))

# Object Store Walkthrough

If you are running a local `nats-server` stop it and restart it with JetStream enabled using `nats-server -js` (if that's not already done)

You can then check that JetStream is enabled by using

Copy

```

    nats account info

```

Which should output something like:

Copy

```

    Connection Information:
    
                   Client ID: 6
                   Client IP: 127.0.0.1
                         RTT: 64.996µs
           Headers Supported: true
             Maximum Payload: 1.0 MiB
               Connected URL: nats://127.0.0.1:4222
           Connected Address: 127.0.0.1:4222
         Connected Server ID: ND2XVDA4Q363JOIFKJTPZW3ZKZCANH7NJI4EJMFSSPTRXDBFG4M4C34K
    
    JetStream Account Information:
    
               Memory: 0 B of Unlimited
              Storage: 0 B of Unlimited
              Streams: 0 of Unlimited
            Consumers: 0 of Unlimited

```

If you see the below instead then JetStream is _not_ enabled

Copy

```

    JetStream Account Information:
    
       JetStream is not supported in this account

```

## 

[hashtag](#creating-an-object-store-bucket)

Creating an Object Store bucket

Just like you need to create streams before you can use them you need to first create an Object Store bucket

Copy

```

    nats object add myobjbucket

```

which outputs

Copy

```

    myobjbucket Object Store Status
    
             Bucket Name: myobjbucket
                Replicas: 1
                     TTL: unlimitd
                  Sealed: false
                    Size: 0 B
      Backing Store Kind: JetStream
        JetStream Stream: OBJ_myobjbucket

```

## 

[hashtag](#putting-a-file-in-the-bucket)

Putting a file in the bucket

Copy

```

    nats object put myobjbucket ~/Movies/NATS-logo.mov

```

Copy

```

    1.5 GiB / 1.5 GiB [====================================================================================]
    
    Object information for myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov
    
                   Size: 1.5 GiB
      Modification Time: 14 Apr 22 00:34 +0000
                 Chunks: 12,656
                 Digest: sha-256 8ee0679dd1462de393d81a3032d71f43d2bc89c0c8a557687cfe2787e926

```

## 

[hashtag](#putting-a-file-in-the-bucket-by-providing-a-name)

Putting a file in the bucket by providing a name

By default the full file path is used as a key. Provide the key explicitly (e.g. a relative path ) with `--name`

Copy

```

    nats object put --name /Movies/NATS-logo.mov myobjbucket ~/Movies/NATS-logo.mov

```

Copy

```

    1.5 GiB / 1.5 GiB [====================================================================================]
    
    Object information for myobjbucket > /Movies/NATS-logo.mov
    
                   Size: 1.5 GiB
      Modification Time: 14 Apr 22 00:34 +0000
                 Chunks: 12,656
                 Digest: sha-256 8ee0679dd1462de393d81a3032d71f43d2bc89c0c8a557687cfe2787e926

```

## 

[hashtag](#listing-the-objects-in-a-bucket)

Listing the objects in a bucket

Copy

```

    nats object ls myobjbucket

```

Copy

```

    ╭───────────────────────────────────────────────────────────────────────────╮
    │                              Bucket Contents                              │
    ├─────────────────────────────────────┬─────────┬───────────────────────────┤
    │ Name                                │ Size    │ Time                      │
    ├─────────────────────────────────────┼─────────┼───────────────────────────┤
    │ /Users/jnmoyne/Movies/NATS-logo.mov │ 1.5 GiB │ 2022-04-13T17:34:55-07:00 │
    │ /Movies/NATS-logo.mov               │ 1.5 GiB │ 2022-04-13T17:35:41-07:00 │
    ╰─────────────────────────────────────┴─────────┴───────────────────────────╯

```

## 

[hashtag](#getting-an-object-from-the-bucket)

Getting an object from the bucket

Copy

```

    nats object get myobjbucket ~/Movies/NATS-logo.mov

```

Copy

```

    1.5 GiB / 1.5 GiB [====================================================================================]
    
    Wrote: 1.5 GiB to /Users/jnmoyne/NATS-logo.mov in 5.68s average 279 MiB/s

```

## 

[hashtag](#getting-an-object-from-the-bucket-with-a-specific-output-path)

Getting an object from the bucket with a specific output path

By default, the file will be stored relative to the local path under its name (not the full path). To specify an output path use `--output`

Copy

```

    nats object get myobjbucket --output /temp/Movies/NATS-logo.mov /Movies/NATS-logo.mov

```

Copy

```

    1.5 GiB / 1.5 GiB [====================================================================================]
    
    Wrote: 1.5 GiB to /temp/Movies/NATS-logo.mov in 5.68s average 279 MiB/s

```

## 

[hashtag](#removing-an-object-from-the-bucket)

Removing an object from the bucket

Copy

```

    nats object rm myobjbucket ~/Movies/NATS-logo.mov

```

Copy

```

    ? Delete 1.5 GiB byte file myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov? Yes
    Removed myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov
    myobjbucket Object Store Status
    
             Bucket Name: myobjbucket
                Replicas: 1
                     TTL: unlimitd
                  Sealed: false
                    Size: 16 MiB
      Backing Store Kind: JetStream
        JetStream Stream: OBJ_myobjbucket

```

## 

[hashtag](#getting-information-about-the-bucket)

Getting information about the bucket

Copy

```

    nats object info myobjbucket

```

Copy

```

    myobjbucket Object Store Status
    
             Bucket Name: myobjbucket
                Replicas: 1
                     TTL: unlimitd
                  Sealed: false
                    Size: 1.6 GiB
      Backing Store Kind: JetStream
        JetStream Stream: OBJ_myobjbucket

```

## 

[hashtag](#watching-for-changes-to-a-bucket)

Watching for changes to a bucket

Copy

```

    nats object watch myobjbucket

```

Copy

```

    [2022-04-13 17:51:28] PUT myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov: 1.5 GiB bytes in 12,656 chunks
    [2022-04-13 17:53:27] DEL myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov

```

### 

[hashtag](#sealing-a-bucket)

Sealing a bucket

You can seal a bucket, meaning that no further changes are allowed on that bucket

Copy

```

    nats object seal myobjbucket

```

Copy

```

    ? Really seal Bucket myobjbucket, sealed buckets can not be unsealed or modified Yes
    myobjbucket has been sealed
    myobjbucket Object Store Status
    
             Bucket Name: myobjbucket
                Replicas: 1
                     TTL: unlimitd
                  Sealed: true
                    Size: 1.6 GiB
      Backing Store Kind: JetStream
        JetStream Stream: OBJ_myobjbucket

```

## 

[hashtag](#deleting-a-bucket)

Deleting a bucket

Using `nats object rm myobjbucket` will delete the bucket and all the files stored in it.

[PreviousObject Storechevron-left](https://docs.nats.io/nats-concepts/jetstream/obj_store) ([local](./../../../../14_hashtag-guided-tour/03_object-store.md))[NextHeaderschevron-right](https://docs.nats.io/nats-concepts/jetstream/headers) ([local](./../headers.md))

Last updated 1 year ago

Was this helpful?
