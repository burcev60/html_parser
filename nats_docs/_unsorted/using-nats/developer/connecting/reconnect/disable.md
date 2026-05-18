---
title: Disabling Reconnect
source: https://docs.nats.io/using-nats/developer/connecting/reconnect/disable
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/reconnect/disable.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../../connecting.md))chevron-right
  4. [Automatic Reconnections](https://docs.nats.io/using-nats/developer/connecting/reconnect) ([local](./../reconnect.md))

# Disabling Reconnect

You can disable automatic reconnect with connection options:

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    // Disable reconnect attempts
    nc, err := nats.Connect("demo.nats.io", nats.NoReconnect())
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
        .noReconnect() // Disable reconnect attempts
        .build();
    Connection nc = Nats.connect(options);
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

     const nc = await connect({
        reconnect: false,
        servers: ["demo.nats.io"],
    });

```

Copy

```

    nc = NATS()
    await nc.connect(
       servers=[
          "nats://demo.nats.io:1222",
          "nats://demo.nats.io:1223",
          "nats://demo.nats.io:1224"
          ],
       allow_reconnect=False,
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
        
        // .NET client does not support disabling reconnects,
        // but you can set the maximum number of reconnect attempts
        MaxReconnectRetry = 1,
    });

```

Copy

```

    require 'nats/client'
    
    NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"], reconnect: false) do |nc|
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
        s = natsOptions_SetAllowReconnect(opts, false);
    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);
    
    (...)
    
    // Destroy objects that were created
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

```

[PreviousAutomatic Reconnectionschevron-left](https://docs.nats.io/using-nats/developer/connecting/reconnect) ([local](./../reconnect.md))[NextSet the Number of Reconnect Attemptschevron-right](https://docs.nats.io/using-nats/developer/connecting/reconnect/max) ([local](./max.md))

Last updated 1 year ago

Was this helpful?
