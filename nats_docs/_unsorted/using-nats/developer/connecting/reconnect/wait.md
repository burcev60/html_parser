---
title: Pausing Between Reconnect Attempts
source: https://docs.nats.io/using-nats/developer/connecting/reconnect/wait
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/reconnect/wait.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../../connecting.md))chevron-right
  4. [Automatic Reconnections](https://docs.nats.io/using-nats/developer/connecting/reconnect) ([local](./../reconnect.md))

# Pausing Between Reconnect Attempts

It doesn’t make much sense to try to connect to the same server over and over. To prevent this sort of thrashing, and wasted reconnect attempts, especially when using TLS, libraries provide a wait setting. Generally clients make sure that between two reconnect attempts to the **same** server at least a certain amount of time has passed. The concrete implementation depends on the library used.

This setting not only prevents wasting client resources, it also alleviates a [_thundering herd_](https://docs.nats.io/using-nats/developer/connecting/reconnect/random) ([local](./random.md)) situation when additional servers are not available.

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    // Set reconnect interval to 10 seconds
    nc, err := nats.Connect("demo.nats.io", nats.ReconnectWait(10*time.Second))
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
        .reconnectWait(Duration.ofSeconds(10))  // Set Reconnect Wait
        .build();
    Connection nc = Nats.connect(options);
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

    const nc = await connect({
        reconnectTimeWait: 10 * 1000, // 10s
        servers: ["demo.nats.io"],
    });

```

Copy

```

    nc = NATS()
    await nc.connect(
       servers=["nats://demo.nats.io:4222"],
       reconnect_time_wait=10,
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
        Url = "nats://127.0.0.1:1222,nats://127.0.0.1:1223,nats://127.0.0.1:1224",
        
        // Set reconnect interval to between 5-10 seconds
        ReconnectWaitMin = TimeSpan.FromSeconds(5),
        ReconnectWaitMax = TimeSpan.FromSeconds(10),
    });

```

Copy

```

    require 'nats/client'
    
    NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"], reconnect_time_wait: 10) do |nc|
       # Do something with the connection
    
       # Close the connection
       nc.close
    end

```

Copy

```

    natsConnection      *conn      = NULL;
    natsOptions         *opts      = NULL;
    natsStatus          s          = NATS_OK;
    
    s = natsOptions_Create(&opts);
    if (s == NATS_OK)
        // Set reconnect interval to 10 seconds (10,000 milliseconds)
        s = natsOptions_SetReconnectWait(opts, 10000);
    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);
    
    (...)
    
    // Destroy objects that were created
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

```

[PreviousAvoiding the Thundering Herdchevron-left](https://docs.nats.io/using-nats/developer/connecting/reconnect/random) ([local](./random.md))[NextListening for Reconnect Eventschevron-right](https://docs.nats.io/using-nats/developer/connecting/reconnect/events) ([local](./events.md))

Last updated 1 year ago

Was this helpful?
