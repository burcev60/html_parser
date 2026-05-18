---
title: Connecting
source: https://docs.nats.io/using-nats/developer/connecting
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/connecting/README.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Using NATS](https://docs.nats.io/using-nats) ([local](./../../using-nats.md))chevron-right
  2. [Developing With NATS](https://docs.nats.io/using-nats/developer) ([local](./../../../07_chevron-right/03_developing-with-nats-chevron-right.md))

# Connecting

In order for a NATS client application to connect to the NATS service, and then subscribe or publish messages to subjects, it needs to be able to be configured with the details of how to connect to the NATS service infrastructure and of how to authenticate with it.

## 

[hashtag](#nats-url)

NATS URL

  1. A 'NATS URL' is a string (in a URL format) that specifies the IP address and port where the NATS server(s) can be reached, and what kind of connection to establish:

     * TLS encrypted _only_ TCP connection (i.e. NATS URLs starting with `tls://...`)

     * TLS encrypted if the server is configured for it or plain un-encrypted TCP connection otherwise (i.e. NATS URLs starting with `nats://...`)

     * Websocket connection (i.e. NATS URLs starting with `ws://...`)

### 

[hashtag](#connecting-to-clusters)

Connecting to clusters

Note that when connecting to a NATS service infrastructure with clusters there is more than one URL and the application should allow for more than one URL to be specified in its NATS connect call (typically you pass a comma separated list of URLs as the URL, e.g. `"nats://server1:port1,nats://server2:port2"`).

When connecting to a cluster it is best to provide the complete set of 'seed' URLs for the cluster.

## 

[hashtag](#authentication-details)

Authentication details

  1. If required: authentication details for the application to identify itself with the NATS server(s). NATS supports multiple authentication schemes:

     * [Username/Password credentials](https://docs.nats.io/using-nats/developer/connecting/userpass) ([local](./connecting/userpass.md)) (which can be passed as part of the NATS URL)

     * [Decentralized JWT Authentication/Authorization](https://docs.nats.io/using-nats/developer/connecting/creds) ([local](./connecting/creds.md)) (where the application is configured with the location of 'credentials file' containing the JWT and private Nkey)

     * [Token Authentication](https://docs.nats.io/using-nats/developer/connecting/token#connecting-with-a-token) ([local](./connecting/token.md#connecting-with-a-token)) (where the application is configured with a Token string)

     * [TLS Certificate](https://docs.nats.io/using-nats/developer/connecting/tls#connecting-with-tls-and-verify-client-identity) ([local](./connecting/tls.md#connecting-with-tls-and-verify-client-identity)) (where the client is configured to use a client TLS certificate and the servers are configured to map the TLS client certificates to users defined in the server configuration)

     * [NKEY with Challenge](https://docs.nats.io/using-nats/developer/connecting/nkey) ([local](./connecting/nkey.md)) (where the client is configured with a Seed and User NKeys)

### 

[hashtag](#runtime-configuration)

Runtime configuration

Your application should expose a way to be configured at run time with the NATS URL(s) to use. If you want to use a secure infrastructure, the application must provide for the definition of either the credentials file (.creds) to use, or the means to encode the token, or Nkey, in the URL(s).

## 

[hashtag](#connection-options)

Connection Options

Besides the connectivity and security details, there are numerous options for a NATS connection ranging from [timeouts](https://docs.nats.io/using-nats/developer/connecting/reconnect#connection-timeout-attributes) ([local](./connecting/reconnect.md#connection-timeout-attributes)) to [reconnect settings](https://docs.nats.io/using-nats/developer/connecting/reconnect#reconnection-attributes) ([local](./connecting/reconnect.md#reconnection-attributes)) to setting [asynchronous error and connection event callback handlers](https://docs.nats.io/using-nats/developer/connecting/reconnect#advisories) ([local](./connecting/reconnect.md#advisories)) in your application.

## 

[hashtag](#see-also)

See Also

WebSocket and NATS

WebSocket and NATS | Hello World

NATS WebSockets and React

NATS WebSockets and React

[PreviousAnatomy of a NATS applicationchevron-left](https://docs.nats.io/using-nats/developer/anatomy) ([local](./anatomy.md))[NextConnecting to the Default Serverchevron-right](https://docs.nats.io/using-nats/developer/connecting/default_server) ([local](./connecting/default-server.md))

Last updated 1 year ago

Was this helpful?
