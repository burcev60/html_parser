---
title: Monitoring the Connection
source: https://docs.nats.io/using-nats/developer/connecting/events
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/events/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../connecting.md))

# Monitoring the Connection

Managing the interaction with the server is primarily the job of the client library but most of the libraries also provide some insight into what is happening under the covers.

For example, the client library may provide a mechanism to get the connection's current status:

Go

Java

JavaScript

Python

C#

Ruby

Copy

```

    nc, err := nats.Connect("demo.nats.io", nats.Name("API Example"))
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()
    
    getStatusTxt := func(nc *nats.Conn) string {
        switch nc.Status() {
        case nats.CONNECTED:
            return "Connected"
        case nats.CLOSED:
            return "Closed"
        default:
            return "Other"
        }
    }
    log.Printf("The connection is %v\n", getStatusTxt(nc))
    
    nc.Close()
    
    log.Printf("The connection is %v\n", getStatusTxt(nc))

```

Copy

```

    Connection nc = Nats.connect("nats://demo.nats.io:4222");
    
    System.out.println("The Connection is: " + nc.getStatus()); // CONNECTED
    
    nc.close();
    
    System.out.println("The Connection is: " + nc.getStatus()); // CLOSED

```

Copy

```

      // you can find out where you connected:
    t.log(`connected to a nats server version ${nc.info.version}`);
    
    // or information about the data in/out of the client:
    const stats = nc.stats();
    t.log(`client sent ${stats.outMsgs} messages and received ${stats.inMsgs}`);

```

Copy

```

    nc = NATS()
    
    await nc.connect(
       servers=["nats://demo.nats.io:4222"],
       )
    
    # Do something with the connection.
    
    print("The connection is connected?", nc.is_connected)
    
    while True:
      if nc.is_reconnecting:
        print("Reconnecting to NATS...")
        break
      await asyncio.sleep(1)
    
    await nc.close()
    
    print("The connection is closed?", nc.is_closed)

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    
    await using var client = new NatsClient();
    
    Console.WriteLine($"{client.Connection.ConnectionState}"); // Closed
    
    await client.ConnectAsync();
    
    Console.WriteLine($"{client.Connection.ConnectionState}"); // Open

```

Copy

```

    NATS.start(max_reconnect_attempts: 2) do |nc|
      puts "Connect is connected?: #{nc.connected?}"
    
      timer = EM.add_periodic_timer(1) do
        if nc.closing?
          puts "Connection closed..."
          EM.cancel_timer(timer)
          NATS.stop
        end
    
        if nc.reconnecting?
          puts "Reconnecting to NATS..."
          next
        end
      end
    end

```

[PreviousBuffering Messages During Reconnect Attemptschevron-left](https://docs.nats.io/using-nats/developer/connecting/reconnect/buffer) ([local](./reconnect/buffer.md))[NextListen for Connection Eventschevron-right](https://docs.nats.io/using-nats/developer/connecting/events/events) ([local](./events/events.md))

Last updated 1 year ago

Was this helpful?
