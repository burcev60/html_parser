---
title: Queue Subscriptions
source: https://docs.nats.io/using-nats/developer/receiving/queues
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/receiving/queues.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Receiving Messages](https://docs.nats.io/using-nats/developer/receiving) ([local](./../receiving.md))

# Queue Subscriptions

Subscribing to a [queue group](https://docs.nats.io/nats-concepts/core-nats/queue) ([local](./../../../nats-concepts/core-nats/queue.md)) is only slightly different than subscribing to a subject alone. The application simply includes a queue name with the subscription. The server will load balance between all members of the queue group. In a cluster setup, every member has the same chance of receiving a particular message.

Keep in mind that queue groups in NATS are dynamic and do not require any server configuration.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-e4f2a6428a4be494475b4c811af461ff0908ec2a%252Fqueues.svg%3Falt%3Dmedia%26token%3Db34513af-ce5b-47c2-99cc-1287ae802d6d&width=768&dpr=3&quality=100&sign=559f7c40&sv=2)

As an example, to subscribe to the queue `workers` with the subject `updates`:

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
    
    // Use a WaitGroup to wait for 10 messages to arrive
    wg := sync.WaitGroup{}
    wg.Add(10)
    
    // Create a queue subscription on "updates" with queue name "workers"
    if _, err := nc.QueueSubscribe("updates", "workers", func(m *nats.Msg) {
        wg.Done()
    }); err != nil {
        log.Fatal(err)
    }
    
    // Wait for messages to come in
    wg.Wait()

```

Copy

```

    Connection nc = Nats.connect("nats://demo.nats.io:4222");
    
    // Use a latch to wait for 10 messages to arrive
    CountDownLatch latch = new CountDownLatch(10);
    
    // Create a dispatcher and inline message handler
    Dispatcher d = nc.createDispatcher((msg) -> {
        String str = new String(msg.getData(), StandardCharsets.UTF_8);
        System.out.println(str);
        latch.countDown();
    });
    
    // Subscribe to the "updates" subject with a queue group named "workers"
    d.subscribe("updates", "workers");
    
    // Wait for a message to come in
    latch.await(); 
    
    // Close the connection
    nc.close();

```

Copy

```

    nc.subscribe(subj, {
        queue: "workers",
        callback: (_err, _msg) => {
          t.log("worker1 got message");
        },
    });
    
    nc.subscribe(subj, {
        queue: "workers",
        callback: (_err, _msg) => {
          t.log("worker2 got message");
        },
    });

```

Copy

```

    nc = NATS()
    
    await nc.connect(servers=["nats://demo.nats.io:4222"])
    
    future = asyncio.Future()
    
    async def cb(msg):
      nonlocal future
      future.set_result(msg)
    
    await nc.subscribe("updates", queue="workers", cb=cb)
    await nc.publish("updates", b'All is Well')
    
    msg = await asyncio.wait_for(future, 1)
    print("Msg", msg)

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    
    await using var client = new NatsClient();
    
    var count = 0;
    
    // Subscribe to the "updates" subject with a queue group named "workers"
    await foreach (var msg in client.SubscribeAsync<string>(subject: "updates", queueGroup: "workers"))
    {
        Console.WriteLine($"Received {++count}: {msg.Subject}: {msg.Data}");
        
        // Break after 10 messages
        if (count == 10)
        {
            break;
        }
    }
    
    Console.WriteLine("Done");

```

Copy

```

    require 'nats/client'
    require 'fiber'
    
    NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
      Fiber.new do
        f = Fiber.current
    
        nc.subscribe("updates", queue: "worker") do |msg, reply|
          f.resume Time.now
        end
    
        nc.publish("updates", "A")
    
        # Use the response
        msg = Fiber.yield
        puts "Msg: #{msg}"
      end.resume
    end

```

Copy

```

    static void
    onMsg(natsConnection *conn, natsSubscription *sub, natsMsg *msg, void *closure)
    {
        printf("Received msg: %s - %.*s\n",
               natsMsg_GetSubject(msg),
               natsMsg_GetDataLength(msg),
               natsMsg_GetData(msg));
    
        // Need to destroy the message!
        natsMsg_Destroy(msg);
    }
    
    
    (...)
    
    natsConnection      *conn = NULL;
    natsSubscription    *sub  = NULL;
    natsStatus          s;
    
    s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
    
    // Create a queue subscription on "updates" with queue name "workers"
    if (s == NATS_OK)
        s = natsConnection_QueueSubscribe(&sub, conn, "updates", "workers", onMsg, NULL);
    
    (...)
    
    
    // Destroy objects that were created
    natsSubscription_Destroy(sub);
    natsConnection_Destroy(conn);

```

If you run this example with the publish examples that send to `updates`, you will see that one of the instances gets a message while the others you run won't. But the instance that receives the message will change.

[PreviousWildcard Subscriptionschevron-left](https://docs.nats.io/using-nats/developer/receiving/wildcards) ([local](./wildcards.md))[NextDraining Messages Before Disconnectchevron-right](https://docs.nats.io/using-nats/developer/receiving/drain) ([local](./drain.md))

Last updated 1 year ago

Was this helpful?
