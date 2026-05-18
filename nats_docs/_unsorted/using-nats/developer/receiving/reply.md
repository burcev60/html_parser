---
title: Replying to a Message
source: https://docs.nats.io/using-nats/developer/receiving/reply
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/receiving/reply.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Receiving Messages](https://docs.nats.io/using-nats/developer/receiving) ([local](./../receiving.md))

# Replying to a Message

Incoming messages have an optional reply-to field. If that field is set, it will contain a subject to which a reply is expected.

For example, the following code will listen for that request and respond with the time.

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
    sub, err := nc.SubscribeSync("time")
    if err != nil {
        log.Fatal(err)
    }
    
    // Read a message
    msg, err := sub.NextMsg(10 * time.Second)
    if err != nil {
        log.Fatal(err)
    }
    
    // Get the time
    timeAsBytes := []byte(time.Now().String())
    
    // Send the time as the response.
    msg.Respond(timeAsBytes)

```

Copy

```

    Connection nc = Nats.connect("nats://demo.nats.io:4222");
    
    // Subscribe to the "time" subject and reply with the current time
    Subscription sub = nc.subscribe("time");
    
    // Read a message
    Message msg = sub.nextMessage(Duration.ZERO);
    
    // Get the time
    Calendar cal = Calendar.getInstance();
    SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
    byte[] timeAsBytes = sdf.format(cal.getTime()).getBytes(StandardCharsets.UTF_8);
    
    // Send the time to the reply to subject
    nc.publish(msg.getReplyTo(), timeAsBytes);
    
    // Flush and close the connection
    nc.flush(Duration.ZERO);
    nc.close();

```

Copy

```

    const sc = StringCodec();
    // set up a subscription to process a request
    const sub = nc.subscribe("time");
    for await (const m of sub) {
      m.respond(sc.encode(new Date().toLocaleDateString()));
    }

```

Copy

```

    nc = NATS()
    
    await nc.connect(servers=["nats://demo.nats.io:4222"])
    
    future = asyncio.Future()
    
    async def cb(msg):
      nonlocal future
      future.set_result(msg)
    
    await nc.subscribe("time", cb=cb)
    
    await nc.publish_request("time", new_inbox(), b'What is the time?')
    await nc.flush()
    
    # Read the message
    msg = await asyncio.wait_for(future, 1)
    
    # Send the time
    time_as_bytes = "{}".format(datetime.now()).encode()
    await nc.publish(msg.reply, time_as_bytes)

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    
    await using var client = new NatsClient();
    
    // Subscribe to the "time" subject and reply with the current time
    await foreach (var msg in client.SubscribeAsync<string>("time"))
    {
        await msg.ReplyAsync(DateTime.Now);
    }

```

Copy

```

    require 'nats/client'
    require 'fiber'
    
    NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
      Fiber.new do
        f = Fiber.current
    
        nc.subscribe("time") do |msg, reply|
          f.resume Time.now
        end
    
        nc.publish("time", 'What is the time?', NATS.create_inbox)
    
        # Use the response
        msg = Fiber.yield
        puts "Reply: #{msg}"
    
      end.resume
    end

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
        s = natsConnection_SubscribeSync(&sub, conn, "time");
    
    // Wait for messages
    if (s == NATS_OK)
        s = natsSubscription_NextMsg(&msg, sub, 10000);
    
    if (s == NATS_OK)
    {
        char buf[64];
    
        snprintf(buf, sizeof(buf), "%lld", nats_Now());
    
        // Send the time as a response
        s = natsConnection_Publish(conn, natsMsg_GetReply(msg), buf, (int) strlen(buf));
    
        // Destroy message that was received
        natsMsg_Destroy(msg);
    }
    
    (...)
    
    // Destroy objects that were created
    natsSubscription_Destroy(sub);
    natsConnection_Destroy(conn);

```

[PreviousUnsubscribing After N Messageschevron-left](https://docs.nats.io/using-nats/developer/receiving/unsub_after) ([local](./unsub-after.md))[NextWildcard Subscriptionschevron-right](https://docs.nats.io/using-nats/developer/receiving/wildcards) ([local](./wildcards.md))

Last updated 1 year ago

Was this helpful?
