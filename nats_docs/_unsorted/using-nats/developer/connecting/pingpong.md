---
title: Ping/Pong Protocol
source: https://docs.nats.io/using-nats/developer/connecting/pingpong
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/connecting/pingpong.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../connecting.md))

# Ping/Pong Protocol

NATS client applications use a PING/PONG protocol to check that there is a working connection to the NATS service. Periodically the client will send PING messages to the server, which responds with a PONG. This period is configured by specifying a ping interval on the client connection settings.

![](https://docs.nats.io/~gitbook/image?url=https%3A%2F%2F1487470910-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LqMYcZML1bsXrN3Ezg0%252Fuploads%252Fgit-blob-06ebb703571bae3f457bcb328f9f7d55ea14b971%252Fpingpong.svg%3Falt%3Dmedia%26token%3D981a213b-c37e-4370-93bd-4e709e3b0d58&width=768&dpr=3&quality=100&sign=3a602822&sv=2)

The connection will be closed as stale when the client reaches a number of pings which recieved no pong in response, which is configured by specifying the maximum pings outstanding on the client connection settings.

The ping interval and the maximum pings outstanding work together to specify how quickly the client connection will be notified of a problem. This will also help when there is a remote network partition where the operating system does not detect a socket error. Upon connection close, the client will attempt to reconnect. When it knows about other servers, these will be tried next.

In the presence of traffic, such as messages or client side pings, the server will not initiate the PING/PONG interaction.

On connections with significant traffic, the client will often figure out there is a problem between PINGS, and as a result the default ping interval is typically on the order of minutes. To close an unresponsive connection after 100s, set the ping interval to 20s and the maximum pings outstanding to 5:

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    // Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
    nc, err := nats.Connect("demo.nats.io", nats.Name("API Ping Example"), nats.PingInterval(20*time.Second), nats.MaxPingsOutstanding(5))
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()
    
    // Do something with the connection

```

Copy

```

    Options options = new Options.Builder()
        .server("nats://demo.nats.io")
        .pingInterval(Duration.ofSeconds(20)) // Set Ping Interval
        .maxPingsOut(5) // Set max pings in flight
        .build();
    
    // Connection is AutoCloseable
    try (Connection nc = Nats.connect(options)) {
        // Do something with the connection
    }

```

Copy

```

    // Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
    const nc = await connect({
        pingInterval: 20 * 1000,
        maxPingOut: 5,
        servers: ["demo.nats.io:4222"],
    });

```

Copy

```

    nc = NATS()
    
    await nc.connect(
       servers=["nats://demo.nats.io:4222"],
       # Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
       ping_interval=20,
       max_outstanding_pings=5,
       )
    
    # Do something with the connection.

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    using NATS.Client.Core;
    
    await using var client = new NatsClient(new NatsOpts
    {
        Url = "nats://demo.nats.io:4222",
        
        // Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
        PingInterval = TimeSpan.FromSeconds(20),
        MaxPingOut = 5,
    });

```

Copy

```

    require 'nats/client'
    # Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
    NATS.start(ping_interval: 20, max_outstanding_pings: 5) do |nc|
       nc.on_reconnect do
        puts "Got reconnected to #{nc.connected_server}"
      end
    
      nc.on_disconnect do |reason|
        puts "Got disconnected! #{reason}"
      end
    
      # Do something with the connection
    end

```

Copy

```

    natsConnection      *conn    = NULL;
    natsOptions         *opts    = NULL;
    natsStatus          s        = NATS_OK;
    
    s = natsOptions_Create(&opts);
    if (s == NATS_OK)
        // Set Ping interval to 20 seconds (20,000 milliseconds)
        s = natsOptions_SetPingInterval(opts, 20000);
    if (s == NATS_OK)
        // Set the limit to 5
        s = natsOptions_SetMaxPingsOut(opts, 5);
    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);
    
    (...)
    
    // Destroy objects that were created
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

```

[PreviousSetting a Connect Timeoutchevron-left](https://docs.nats.io/using-nats/developer/connecting/connect_timeout) ([local](./connect-timeout.md))[NextTurning Off Echo'd Messageschevron-right](https://docs.nats.io/using-nats/developer/connecting/noecho) ([local](./noecho.md))

Last updated 1 year ago

Was this helpful?
