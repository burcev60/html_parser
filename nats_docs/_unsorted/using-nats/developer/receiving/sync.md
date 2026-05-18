---
title: Synchronous Subscriptions
source: https://docs.nats.io/using-nats/developer/receiving/sync
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/receiving/sync.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Receiving Messages](https://docs.nats.io/using-nats/developer/receiving) ([local](./../receiving.md))

# Synchronous Subscriptions

Synchronous subscriptions require the application to wait for messages. This type of subscription is easy to set-up and use, but requires the application to deal with looping if multiple messages are expected. For situations where a single message is expected, synchronous subscriptions are sometimes easier to manage, depending on the language.

For example, to subscribe to the subject `updates` and receive a single message you could do:

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    nc, err := nats.Connect("demo.nats.io")
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()
    
    // Subscribe
    sub, err := nc.SubscribeSync("updates")
    if err != nil {
        log.Fatal(err)
    }
    
    // Wait for a message
    msg, err := sub.NextMsg(10 * time.Second)
    if err != nil {
        log.Fatal(err)
    }
    
    // Use the response
    log.Printf("Reply: %s", msg.Data)

```

Copy

```

    Connection nc = Nats.connect("nats://demo.nats.io:4222");
    
    // Subscribe
    Subscription sub = nc.subscribe("updates");
    
    // Read a message
    Message msg = sub.nextMessage(Duration.ZERO);
    
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(str);
    
    // Close the connection
    nc.close();

```

Copy

```

    // node-nats subscriptions are always async.

```

Copy

```

    # Asyncio NATS client currently does not have a sync subscribe API

```

Copy

```

    // NATS .NET subscriptions are always async.

```

Copy

```

    # The Ruby NATS client subscriptions are all async.

```

Copy

```

    natsConnection      *conn      = NULL;
    natsSubscription    *sub       = NULL;
    natsMsg             *msg       = NULL;
    natsStatus          s          = NATS_OK;
    
    s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
    
    // Subscribe
    if (s == NATS_OK)
        s = natsConnection_SubscribeSync(&sub, conn, "updates");
    
    // Wait for messages
    if (s == NATS_OK)
        s = natsSubscription_NextMsg(&msg, sub, 10000);
    
    if (s == NATS_OK)
    {
        printf("Received msg: %s - %.*s\n",
                natsMsg_GetSubject(msg),
                natsMsg_GetDataLength(msg),
                natsMsg_GetData(msg));
    
        // Destroy message that was received
        natsMsg_Destroy(msg);
    }
    
    (...)
    
    // Destroy objects that were created
    natsSubscription_Destroy(sub);
    natsConnection_Destroy(conn);

```

[PreviousReceiving Messageschevron-left](https://docs.nats.io/using-nats/developer/receiving) ([local](./../receiving.md))[NextAsynchronous Subscriptionschevron-right](https://docs.nats.io/using-nats/developer/receiving/async) ([local](./async.md))

Last updated 1 year ago

Was this helpful?
