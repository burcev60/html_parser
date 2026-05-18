---
title: Sending Messages
source: https://docs.nats.io/using-nats/developer/sending
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/sending/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../07_chevron-right/03_developing-with-nats-chevron-right.md))

# Sending Messages

NATS sends and receives messages using a protocol that includes a target subject, an optional reply subject and an array of bytes. Some libraries may provide helpers to convert other data formats to and from bytes, but the NATS server will treat all messages as opaque byte arrays.

All of the NATS clients are designed to make sending a message simple. For example, to send the string “All is Well” to the “updates” subject as a UTF-8 string of bytes you would do:

Go

Java

JavaScript

Python

C#

Ruby

Copy

```

    nc, err := nats.Connect("demo.nats.io", nats.Name("API PublishBytes Example"))
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()
    
    if err := nc.Publish("updates", []byte("All is Well")); err != nil {
        log.Fatal(err)
    }

```

Copy

```

    Connection nc = Nats.connect("nats://demo.nats.io:4222");
    
    nc.publish("updates", "All is Well".getBytes(StandardCharsets.UTF_8));

```

Copy

```

    const sc = StringCodec();
    nc.publish("updates", sc.encode("All is Well"));

```

Copy

```

    nc = NATS()
    
    await nc.connect(servers=["nats://demo.nats.io:4222"])
    
    await nc.publish("updates", b'All is Well')

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    
    await using var client = new NatsClient(url: "demo.nats.io", name: "API Publish String Example");
    
    // The default serializer uses UTF-8 encoding for strings
    await client.PublishAsync<string>(subject: "updates", data: "All is Well");

```

Copy

```

    require 'nats/client'
    
    NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
      nc.publish("updates", "All is Well")
    end

```

[PreviousReceiving Structured Datachevron-left](https://docs.nats.io/using-nats/developer/receiving/structure) ([local](./receiving/structure.md))[NextIncluding a Reply Subjectchevron-right](https://docs.nats.io/using-nats/developer/sending/replyto) ([local](./sending/replyto.md))

Last updated 1 year ago

Was this helpful?
