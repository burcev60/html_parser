---
title: Enabling Monitoring
source: https://docs.nats.io/running-a-nats-service/configuration/monitoring
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/monitoring.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))

# Enabling Monitoring

## 

[hashtag](#nats-server-monitoring)

NATS Server Monitoring

To monitor the NATS messaging system, `nats-server` provides a lightweight HTTP server on a dedicated monitoring port. The monitoring server provides several endpoints, providing statistics and other information.

The [NATS monitoring endpoints](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring) ([local](./../nats-admin/monitoring.md)) support [JSONParrow-up-right](https://en.wikipedia.org/wiki/JSONP) and [CORSarrow-up-right](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing#How_CORS_works), making it easy to create single page monitoring web applications.

> Warning: `nats-server` does not have authentication/authorization for the monitoring endpoint. When you plan to open your `nats-server` to the internet make sure to not expose the monitoring port as well. By default monitoring binds to every interface `0.0.0.0` so consider setting monitoring to `localhost` or have appropriate firewall rules.

### 

[hashtag](#enabling-monitoring-from-the-command-line)

Enabling monitoring from the command line

To enable the monitoring server, start the NATS server with the monitoring flag `-m` and the monitoring port, or turn it on in the [configuration file](#enable-monitoring-from-the-configuration-file).

Copy

```

    -m, --http_port PORT             HTTP PORT for monitoring
    -ms,--https_port PORT            Use HTTPS PORT for monitoring

```

Example:

Copy

```

    nats-server -m 8222

```

Copy

```

    [4528] 2019/06/01 20:09:58.572939 [INF] Starting nats-server version 2.0.0
    [4528] 2019/06/01 20:09:58.573007 [INF] Starting http monitor on port 8222
    [4528] 2019/06/01 20:09:58.573071 [INF] Listening for client connections on 0.0.0.0:4222
    [4528] 2019/06/01 20:09:58.573090 [INF] nats-server is ready

```

To test, run `nats-server -m 8222`, then go to <http://localhost:8222/>[arrow-up-right](http://localhost:8222/)

### 

[hashtag](#enable-monitoring-from-the-configuration-file)

Enable monitoring from the configuration file

You can also enable monitoring using the configuration file as follows:

Copy

```

    http_port: 8222

```

Binding to `localhost` as well:

Copy

```

    http: localhost:8222

```

For example, to monitor this server locally, the endpoint would be <http://localhost:8222/varz>[arrow-up-right](http://localhost:8222/varz). It reports various general statistics.

## 

[hashtag](#monitoring-tools)

Monitoring Tools

In addition to writing custom monitoring tools, you can monitor nats-server in Prometheus. The [Prometheus NATS Exporterarrow-up-right](https://github.com/nats-io/prometheus-nats-exporter) allows you to configure the metrics you want to observe and store in Prometheus. There's a sample [Grafanaarrow-up-right](https://grafana.com) dashboard that you can use to visualize the server metrics.

[PreviousLoggingchevron-left](https://docs.nats.io/running-a-nats-service/configuration/logging) ([local](./logging.md))[NextMQTTchevron-right](https://docs.nats.io/running-a-nats-service/configuration/mqtt) ([local](./mqtt.md))

Last updated 6 months ago

Was this helpful?
