---
title: Protocol Demo
source: https://docs.nats.io/reference/reference-protocols/nats-protocol-demo
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/reference/nats-protocol/nats-protocol-demo.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Reference](https://docs.nats.io/reference) ([local](./../../reference.md))chevron-right
  2. [NATS Protocols](https://docs.nats.io/reference/reference-protocols) ([local](./../../../11_chevron-right/02_nats-protocols-chevron-right.md))

# Protocol Demo

The virtues of the NATS protocol manifest quickly when you experience how easy it is to use NATS. Because the NATS protocol is text-based, you can use NATS across virtually any platform or language.

In the following demo we use [Telnetarrow-up-right](https://en.wikipedia.org/wiki/Telnet). On the wire you can publish and subscribe using a simple [set of protocol commands](https://docs.nats.io/reference/reference-protocols/nats-protocol) ([local](./nats-protocol.md)).

## 

[hashtag](#initiate-a-connection)

Initiate a connection

Open a terminal and initiate a connection to the NATS demo instance.

Copy

```

    telnet demo.nats.io 4222

```

The expected result will roughly look like this. Note the IP address, and `INFO` payload may have different values.

Copy

```

    Trying 107.170.221.32...
    Connected to demo.nats.io.
    Escape character is '^]'.
    INFO {"server_id":"NCXMJZYQEWUDJFLYLSTTE745I2WUNCVG3LJJ3NRKSFJXEG6RGK7753DJ","version":"2.0.0","proto":1,"go":"go1.11.10","host":"0.0.0.0","port":4222,"max_payload":1048576,"client_id":5089}

```

## 

[hashtag](#confirm-the-connection)

Confirm the connection

Any client establishing a connection with the server must send `CONNECT` message to confirm the connection. There are several options that can be specified to indicate the client supported features, but for the purpose of this example, we can send an empty payload.

Copy

```

    CONNECT {}

```

You will see a `+OK` message in response.

## 

[hashtag](#observe-the-ping-pong-interval)

Observe the ping/pong interval

Not long after the `CONNECT` you will see a `PING` message. There is a bi-directional behavior between the client and server to check for liveness. In the case of the server, after some period of time without a `PONG`, the server will shutdown the client connection. If the client does not hear back a `PONG`, it will attempt to reconnect to a different server in a clustered setup, if available.

You can respond to the server, but simply typing `PONG` followed by a return.

Copy

```

    PONG

```

## 

[hashtag](#bind-a-subscription)

Bind a subscription

Subscribe to the wildcard subject `foo.*` with subscription ID of `90`.

Copy

```

    SUB foo.* 90

```

An `+OK` message will follow, indicating a successful subscription.

## 

[hashtag](#publish-a-message)

Publish a message

NATS connection are bi-directional, so we can not only subscribe to subjects, but we can publish to them as well.

We can send the `PUB` command followed by the subject, and the length of the message payload that will be followed on the second line. In this case, `hello` is the payload. Once that is typed, hit return which will send the message.

Copy

```

    PUB foo.bar 5
    hello

```

An `+OK` message will follow, indicating a successful publish.

Immediately following, a `MSG` message will appear which indicates the subscription received the message that was just published.

Copy

```

    MSG foo.bar 90 5
    hello

```

## 

[hashtag](#unsubscribe-from-the-subject)

Unsubscribe from the subject

You can use the `UNSUB` command to unsubscribe from a message.

Run the subscriber to unsubscribe:

Copy

```

    UNSUB 90

```

## 

[hashtag](#try-to-publish-again)

Try to publish again

Now that we unsubscribed, if we attempt to publish again, we will receive the `+OK`, but will not receive a `MSG`.

Copy

```

    PUB foo.bar 7
    goodbye

```

## 

[hashtag](#close-the-connection)

Close the connection

Use `ctrl+c` to close the connection, however, as noted above, if this is not done, after some period of inactivity the server will automatically close the connection.

[PreviousNATS Protocolschevron-left](https://docs.nats.io/reference/reference-protocols) ([local](./../../../11_chevron-right/02_nats-protocols-chevron-right.md))[NextClient Protocolchevron-right](https://docs.nats.io/reference/reference-protocols/nats-protocol) ([local](./nats-protocol.md))

Last updated 3 years ago

Was this helpful?
