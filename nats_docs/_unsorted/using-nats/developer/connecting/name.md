---
title: Connection Name
source: https://docs.nats.io/using-nats/developer/connecting/name
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/connecting/name.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../connecting.md))

# Connection Name

Connections can be assigned a name which will appear in some of the server monitoring data. This name is not required, but is **highly recommended** as a friendly connection name will help in monitoring, error reporting, debugging, and testing.

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    nc, err := nats.Connect("demo.nats.io", nats.Name("API Name Option Example"))
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
        .connectionName("API Name Option Example") // Set Name
        .build();
    Connection nc = Nats.connect(options);
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

     const nc = await connect({
        name: "my-connection",
        servers: ["demo.nats.io:4222"],
    });

```

Copy

```

    nc = NATS()
    await nc.connect(
        servers=["nats://demo.nats.io:4222"], 
        name="API Name Option Example")
    
    # Do something with the connection
    
    await nc.close()

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    
    await using var client = new NatsClient(name: "API Name Option Example", url: "nats://demo.nats.io:4222");
    
    // It's optional to call ConnectAsync()
    // as it will be called when needed automatically
    await client.ConnectAsync();

```

Copy

```

    require 'nats/client'
    
    NATS.start(servers: ["nats://demo.nats.io:4222"], name: "API Name Option Example") do |nc|
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
        s = natsOptions_SetName(opts, "API Name Option Example");
    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);
    
    (...)
    
    // Destroy objects that were created
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

```

[PreviousConnecting to a Clusterchevron-left](https://docs.nats.io/using-nats/developer/connecting/cluster) ([local](./cluster.md))[NextAuthenticating with a User and Passwordchevron-right](https://docs.nats.io/using-nats/developer/connecting/userpass) ([local](./userpass.md))

Last updated 1 year ago

Was this helpful?
