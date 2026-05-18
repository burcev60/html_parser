---
title: WebSocket
source: https://docs.nats.io/running-a-nats-service/configuration/websocket
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/websocket/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))

# WebSocket

 _Supported since NATS Server version 2.2_

WebSocket support can be enabled in the server and may be used alongside the traditional TCP socket connections. TLS, compression and Origin Header checking are supported.

**Important**

  * NATS Supports only WebSocket data frames in Binary, not Text format (<https://tools.ietf.org/html/rfc6455#section-5.6>[arrow-up-right](https://tools.ietf.org/html/rfc6455#section-5.6)). The server will always send in Binary and your clients MUST send in Binary too.

  * For writers of client libraries: a WebSocket frame is not guaranteed to contain a full NATS protocol (actually will generally not). Any data from a frame must be going through a parser that can handle partial protocols. See the protocol description [here](https://docs.nats.io/reference/reference-protocols/nats-protocol) ([local](./../../reference/reference-protocols/nats-protocol.md)).

[PreviousSystem Events & Decentralized JWT Tutorialchevron-left](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts) ([local](./sys-accounts/sys-accounts.md))[NextConfigurationchevron-right](https://docs.nats.io/running-a-nats-service/configuration/websocket/websocket_conf) ([local](./websocket/websocket-conf.md))

Last updated 4 years ago

Was this helpful?
