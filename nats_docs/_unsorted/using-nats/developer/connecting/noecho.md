---
title: Turning Off Echo'd Messages
source: https://docs.nats.io/using-nats/developer/connecting/noecho
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/connecting/noecho.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../connecting.md))

# Turning Off Echo'd Messages

By default a NATS connection will echo messages if the connection also has interest in the published subject. This means that if a publisher on a connection sends a message to a subject any subscribers on that same connection will receive the message. Clients can opt to turn off this behavior, such that regardless of interest, the message will not be delivered to subscribers on the same connection.

The NoEcho option can be useful in BUS patterns where all applications subscribe and publish to the same subject. Usually a publish represents a state change that the application already knows about, so in the case where the application publishes an update it does not need to process the update itself.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-5a09f42db59d94cf40b825de3e3c436bc0250eef%252Fnoecho.svg%3Falt%3Dmedia%26token%3D796746d0-f2dc-4112-9eb2-90e6f6086bff&width=768&dpr=3&quality=100&sign=5fbe87d0&sv=2)

Keep in mind that each connection will have to turn off echo, and that it is per connection, not per application. Also, turning echo on and off can result in a major change to your applications communications protocol since messages will flow or stop flowing based on this setting and the subscribing code won't have any indication as to why.

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    // Turn off echo
    nc, err := nats.Connect("demo.nats.io", nats.Name("API NoEcho Example"), nats.NoEcho())
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()
    
    // Do something with the connection

```

Copy

```

    Options options = new Options.Builder()
        .server("nats://demo.nats.io:4222")
        .noEcho() // Turn off echo
        .build();
    Connection nc = Nats.connect(options);
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

    const nc = await connect({
        servers: ["demo.nats.io"],
        noEcho: true,
    });
    
    const sub = nc.subscribe(subj, { callback: (_err, _msg) => {} });
    nc.publish(subj);
    await sub.drain();
    // we won't get our own messages
    t.is(sub.getProcessed(), 0);

```

Copy

```

    ncA = NATS()
    ncB = NATS()
    
    await ncA.connect(no_echo=True)
    await ncB.connect()
    
    async def handler(msg):
       # Messages sent by `ncA' will not be received.
       print("[Received] ", msg)
    
    await ncA.subscribe("greetings", cb=handler)
    await ncA.flush()
    await ncA.publish("greetings", b'Hello World!')
    await ncB.publish("greetings", b'Hello World!')
    
    # Do something with the connection
    
    await asyncio.sleep(1)
    await ncA.drain()
    await ncB.drain()

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    using NATS.Client.Core;
    
    await using var client = new NatsClient(new NatsOpts
    {
        Url = "nats://demo.nats.io:4222",
        
        // Turn off echo
        Echo = false
    });

```

Copy

```

    NATS.start("nats://demo.nats.io:4222", no_echo: true) do |nc|
      # ...
    end

```

Copy

```

    natsConnection      *conn    = NULL;
    natsOptions         *opts    = NULL;
    natsStatus          s        = NATS_OK;
    
    s = natsOptions_Create(&opts);
    if (s == NATS_OK)
        s = natsOptions_SetNoEcho(opts, true);
    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);
    
    (...)
    
    // Destroy objects that were created
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

```

[PreviousPing/Pong Protocolchevron-left](https://docs.nats.io/using-nats/developer/connecting/pingpong) ([local](./pingpong.md))[NextMiscellaneous functionalitieschevron-right](https://docs.nats.io/using-nats/developer/connecting/misc) ([local](./misc.md))

Last updated 1 year ago

Was this helpful?
