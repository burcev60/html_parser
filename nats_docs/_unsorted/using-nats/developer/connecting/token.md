---
title: Authenticating with a Token
source: https://docs.nats.io/using-nats/developer/connecting/token
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/connecting/security/token.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../../07_chevron-right/03_developing-with-nats-chevron-right.md))chevron-right
  3. [Connecting](https://docs.nats.io/using-nats/developer/connecting) ([local](./../connecting.md))

# Authenticating with a Token

Tokens are basically random strings, much like a password, and can provide a simple authentication mechanism in some situations. However, tokens are only as safe as they are secret so other authentication schemes can provide more security in large installations. It is highly recommended to use one of the other NATS authentication mechanisms.

For this example, start the server using:

Copy

```

    nats-server --auth mytoken

```

The code uses localhost:4222 so that you can start the server on your machine to try them out.

## 

[hashtag](#connecting-with-a-token)

Connecting with a Token

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    // Set a token
    nc, err := nats.Connect("127.0.0.1", nats.Name("API Token Example"), nats.Token("mytoken"))
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
        .token("mytoken") // Set a token
        .build();
    Connection nc = Nats.connect(options);
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

    const nc = await connect({
      port: ns.port,
      token: "aToK3n",
    });

```

Copy

```

    nc = NATS()
    
    await nc.connect(servers=["nats://demo.nats.io:4222"], token="mytoken")
    
    # Do something with the connection.

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    using NATS.Client.Core;
    
    await using var client = new NatsClient(new NatsOpts
    {
        Url = "127.0.0.1",
        Name = "API Token Example",
        AuthOpts = new NatsAuthOpts
        {
            Token = "mytoken"
        }
    });

```

Copy

```

    NATS.start(token: "mytoken") do |nc|
      puts "Connected using token"
    end

```

Copy

```

    natsConnection      *conn      = NULL;
    natsOptions         *opts      = NULL;
    natsStatus          s          = NATS_OK;
    
    s = natsOptions_Create(&opts);
    if (s == NATS_OK)
        s = natsOptions_SetToken(opts, "mytoken");
    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);
    
    (...)
    
    // Destroy objects that were created
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

```

## 

[hashtag](#connecting-with-a-token-in-the-url)

Connecting with a Token in the URL

Some client libraries will allow you to pass the token as part of the server URL using the form:

> nats://_token_ @server:port

Again, once you construct this URL you can connect as if this was a normal URL.

Go

Java

JavaScript

Python

C#

Ruby

C

Copy

```

    // Token in URL
    nc, err := nats.Connect("mytoken@localhost")
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()
    
    // Do something with the connection

```

Copy

```

    Connection nc = Nats.connect("nats://mytoken@localhost:4222");//Token in URL
    
    // Do something with the connection
    
    nc.close();

```

Copy

```

      // JavaScript doesn't support tokens in urls use the `token` option

```

Copy

```

    nc = NATS()
    
    await nc.connect(servers=["nats://mytoken@demo.nats.io:4222"])
    
    # Do something with the connection.

```

Copy

```

    // dotnet add package NATS.Net
    using NATS.Net;
    using NATS.Client.Core;
    
    await using var client = new NatsClient(new NatsOpts
    {
        // .NET client doesn't support tokens in URLs
        // use Token option instead.
        AuthOpts = new NatsAuthOpts
        {
            Token = "mytoken"
        }
    });

```

Copy

```

    NATS.start("mytoken@127.0.0.1:4222") do |nc|
      puts "Connected using token!"
    end

```

Copy

```

    natsConnection      *conn      = NULL;
    natsOptions         *opts      = NULL;
    natsStatus          s          = NATS_OK;
    
    s = natsOptions_Create(&opts);
    if (s == NATS_OK)
        s = natsOptions_SetURL(opts, "nats://mytoken@127.0.0.1:4222");
    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);
    
    (...)
    
    // Destroy objects that were created
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

```

[PreviousAuthenticating with a User and Passwordchevron-left](https://docs.nats.io/using-nats/developer/connecting/userpass) ([local](./userpass.md))[NextAuthenticating with an NKeychevron-right](https://docs.nats.io/using-nats/developer/connecting/nkey) ([local](./nkey.md))

Last updated 1 year ago

Was this helpful?
