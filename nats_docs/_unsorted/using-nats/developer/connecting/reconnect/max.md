---
title: Set the Number of Reconnect Attempts
source: https://docs.nats.io/using-nats/developer/connecting/reconnect/max
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/reconnect/max.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../../connecting.md))chevron-right
  4. [Automatic Reconnections](https://docs.nats.io/using-nats/developer/connecting/reconnect) ([local](./../reconnect.md))

# Set the Number of Reconnect Attempts

Applications can set the maximum reconnect attempts per server. This includes the server provided to the client's connect call, as well as the server the client discovered through another server. Once reconnect to a server fails the specified amount of times in a row, it will be removed from the connect list. After a successful reconnect to a server, the client will reset that server's failed reconnect attempt count. If a server was removed from the connect list, it can be rediscovered on connect. This effectively resets the connect attempt count as well. If the client runs out of servers to reconnect, it will close the connection and [raise an error](https://docs.nats.io/using-nats/developer/connecting/reconnect/events) ([local](./events.md)).

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    // Set max reconnects attempts
    nc, err := nats.Connect("demo.nats.io", nats.MaxReconnects(10))
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
        .maxReconnects(10) // Set max reconnect attempts
        .build();
    Connection nc = Nats.connect(options);
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

    const nc = await connect({
        maxReconnectAttempts: 10,
        servers: ["demo.nats.io"],
    });

```

Copy

```

    nc = NATS()
    await nc.connect(
       servers=["nats://demo.nats.io:4222"],
       max_reconnect_attempts=10,
       )
    
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
        
        // Set the maximum number of reconnect attempts
        MaxReconnectRetry = 10,
    });

```

Copy

```

    require 'nats/client'
    
    NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"], max_reconnect_attempts: 10) do |nc|
       # Do something with the connection
    
       # Close the connection
       nc.close
    end

```

Copy

```

    natsConnection      *conn    = NULL;
    natsOptions         *opts    = NULL;
    natsStatus          s        = NATS_OK;
    
    s = natsOptions_Create(&opts);
    if (s == NATS_OK)
        s = natsOptions_SetMaxReconnect(opts, 10);
    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);
    
    (...)
    
    // Destroy objects that were created
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

```

[PreviousDisabling Reconnectchevron-left](https://docs.nats.io/using-nats/developer/connecting/reconnect/disable) ([local](./disable.md))[NextAvoiding the Thundering Herdchevron-right](https://docs.nats.io/using-nats/developer/connecting/reconnect/random) ([local](./random.md))

Last updated 1 year ago

Was this helpful?
