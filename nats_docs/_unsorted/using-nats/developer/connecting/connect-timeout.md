---
title: Setting a Connect Timeout
source: https://docs.nats.io/using-nats/developer/connecting/connect_timeout
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/connecting/connect_timeout.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../connecting.md))

# Setting a Connect Timeout

Each library has its own, language preferred way, to pass connection options. One of the most common options is a connect timeout. It limits how long it can take to establish a connection to a server. Should multiple URLs be provided, this timeout applies to each cluster member individually. To set the maximum time to connect to a server to 10 seconds:

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    nc, err := nats.Connect("demo.nats.io", nats.Name("API Options Example"), nats.Timeout(10*time.Second))
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
        .connectionTimeout(Duration.ofSeconds(10)) // Set timeout
        .build();
    Connection nc = Nats.connect(options);
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

    const nc = await connect({
        timeout: 10 * 1000, // 10s
        servers: ["demo.nats.io"],
    });

```

Copy

```

    nc = NATS()
    await nc.connect(
      servers=["nats://demo.nats.io:4222"],
      connect_timeout=10)
    
    # Do something with the connection
    
    await nc.close()

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    using NATS.Client.Core;
    
    await using var client = new NatsClient(new NatsOpts
    {
        Url = "nats://demo.nats.io:4222",
        ConnectTimeout = TimeSpan.FromSeconds(10)
    });
    
    // You don't have to call ConnectAsync() explicitly,
    // first operation will make the connection otherwise.
    await client.ConnectAsync();

```

Copy

```

    # There is currently no connect timeout as part of the Ruby NATS client API, but you can use a timer to mimic it.
    require 'nats/client'
    
    timer = EM.add_timer(10) do
      NATS.connect do |nc|
        # Do something with the connection
    
        # Close the connection
        nc.close
      end
    end
    EM.cancel_timer(timer)

```

Copy

```

    nnatsConnection      *conn    = NULL;
     natsOptions         *opts    = NULL;
     natsStatus          s        = NATS_OK;
    
     s = natsOptions_Create(&opts);
     if (s == NATS_OK)
         // Set the timeout to 10 seconds (10,000 milliseconds)
         s = natsOptions_SetTimeout(opts, 10000);
     if (s == NATS_OK)
         s = natsConnection_Connect(&conn, opts);
    
     (...)
    
     // Destroy objects that were created
     natsConnection_Destroy(conn);
     natsOptions_Destroy(opts);

```

[PreviousEncrypting Connections with TLSchevron-left](https://docs.nats.io/using-nats/developer/connecting/tls) ([local](./tls.md))[NextPing/Pong Protocolchevron-right](https://docs.nats.io/using-nats/developer/connecting/pingpong) ([local](./pingpong.md))

Last updated 5 days ago

Was this helpful?
