---
title: Connecting to the Default Server
source: https://docs.nats.io/using-nats/developer/connecting/default_server
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/connecting/default_server.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../connecting.md))

# Connecting to the Default Server

Some libraries also provide a special way to connect to a _default_ url, which is generally `nats://localhost:4222`:

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    nc, err := nats.Connect(nats.DefaultURL)
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()
    
    // Do something with the connection

```

Copy

```

    Connection nc = Nats.connect();
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

    const nc = await connect();
    // Do something with the connection
    doSomething();
    // When done close it
    await nc.close();

```

Copy

```

    nc = NATS()
    await nc.connect()
    
    # Do something with the connection
    
    await nc.close()

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    
    await using var client = new NatsClient();
    
    // It's optional to call ConnectAsync()
    // as it will be called when needed automatically
    await client.ConnectAsync();

```

Copy

```

    require 'nats/client'
    
    NATS.start do |nc|
       # Do something with the connection
    
       # Close the connection
       nc.close
    end

```

Copy

```

    natsConnection      *conn = NULL;
    natsStatus          s;
    
    s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
    if (s != NATS_OK)
      // handle error
    
    // Destroy connection, no-op if conn is NULL.
    natsConnection_Destroy(conn);

```

[PreviousConnectingchevron-left](https://docs.nats.io/using-nats/developer/connecting) ([local](./../connecting.md))[NextConnecting to a Specific Serverchevron-right](https://docs.nats.io/using-nats/developer/connecting/specific_server) ([local](./specific-server.md))

Last updated 1 year ago

Was this helpful?
