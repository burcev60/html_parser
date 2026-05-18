---
title: Logging
source: https://docs.nats.io/running-a-nats-service/configuration/logging
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/logging.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))

# Logging

## 

[hashtag](#configuring-logging)

Configuring Logging

The NATS server provides various logging options that you can set via the command line or the configuration file.

### 

[hashtag](#command-line-options)

Command Line Options

The following logging operations are supported:

Copy

```

    -l, --log FILE                   File to redirect log output.
    -T, --logtime                    Timestamp log entries (default is true).
    -s, --syslog                     Enable syslog as log method.
    -r, --remote_syslog              Syslog server address.
    -D, --debug                      Enable debugging output.
    -V, --trace                      Trace the raw protocol.
    -VV                              Verbose trace (traces system account as well)
    -DV                              Debug and Trace.
    -DVV                             Debug and verbose trace (traces system account as well)

```

#### 

[hashtag](#debug-and-trace)

Debug and trace

The `-DV` flag enables trace and debug for the server.

Copy

```

    nats-server -DV -m 8222 -user foo -pass bar

```

#### 

[hashtag](#log-file-redirect)

Log file redirect

Copy

```

    nats-server -DV -m 8222 -l nats.log

```

#### 

[hashtag](#timestamp)

Timestamp

If `-T false` then log entries are not timestamped. Default is true.

#### 

[hashtag](#syslog)

Syslog

You can configure syslog with `UDP`:

Copy

```

    nats-server -r udp://localhost:514

```

or `syslog:`

Copy

```

    nats-server -r syslog://<hostname>:<port>

```

For example:

Copy

```

    syslog://logs.papertrailapp.com:26900

```

### 

[hashtag](#using-the-configuration-file)

Using the Configuration File

All of these settings are available in the configuration file as well.

Copy

```

    debug:   false
    trace:   true
    logtime: false
    logfile_size_limit: 1GB
    logfile_max_num: 100
    log_file: "/tmp/nats-server.log"

```

### 

[hashtag](#log-rotation)

Log Rotation

Introduced in NATS Server v2.1.4, NATS allows for auto-rotation of log files when the size is greater than the configured limit set in `logfile_size_limit`. The backup files will have the same name as the original log file with the suffix .yyyy.mm.dd.hh.mm.ss.micros.

You can also use NATS-included mechanisms with [logrotatearrow-up-right](https://github.com/logrotate/logrotate), a simple standard Linux utility to rotate logs available on most distributions like Debian, Ubuntu, RedHat (CentOS), etc., to make log rotation simple.

For example, you could configure `logrotate` with:

Copy

```

    /path/to/nats-server.log {
        daily
        rotate 30
        compress
        missingok
        notifempty
        postrotate
            kill -SIGUSR1 `cat /var/run/nats-server.pid`
        endscript
    }

```

The first line specifies the location that the subsequent lines will apply to.

The rest of the file specifies that the logs will rotate daily ("daily" option) and that 30 older copies will be preserved ("rotate" option). Other options are described in [logrorate documentationarrow-up-right](https://linux.die.net/man/8/logrotate).

The "postrotate" section tells NATS server to reload the log files once the rotation is complete. The command ``kill -SIGUSR1`cat /var/run/nats-server.pid``` does not kill the NATS server process, but instead sends it a signal causing it to reload its log files. This will cause new requests to be logged to the refreshed log file.

The `/var/run/nats-server.pid` file is where NATS server stores the master process's pid.

## 

[hashtag](#some-logging-notes)

Some Logging Notes

  * The NATS server, in verbose mode, will log the receipt of `UNSUB` messages, but this does not indicate the subscription is gone, only that the message was received. The `DELSUB` message in the log can be used to determine when the actual subscription removal has taken place.

[PreviousAuth Calloutchevron-left](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout) ([local](./securing-nats/auth-callout.md))[NextEnabling Monitoringchevron-right](https://docs.nats.io/running-a-nats-service/configuration/monitoring) ([local](./monitoring.md))

Last updated 1 year ago

Was this helpful?
