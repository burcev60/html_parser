---
title: Signals
source: https://docs.nats.io/running-a-nats-service/nats_admin/signals
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/signals.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Managing and Monitoring your NATS Server Infrastructure](https://docs.nats.io/running-a-nats-service/nats_admin) ([local](./../../../09_chevron-right/10_managing-and-monitoring-your-nats-server-infrastructure-chev.md))

# Signals

## 

[hashtag](#command-line)

Command Line

On Unix systems, the NATS server responds to the following signals. You can send these using the standard Unix `kill` command, or use the `nats-server --signal` command for convenience.

nats-server command

Unix Signal

Description

`--signal ldm`

`SIGUSR2`

Graceful shutdown (evicts clients gradually) ([lame duck mode](https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode) ([local](./lame-duck-mode.md)))

`--signal quit`

`SIGINT`

Stops the server gracefully

`--signal term`

`SIGTERM`

Stops the server gracefully

`--signal stop`

`SIGKILL`

Kills the process immediately

`--signal reload`

`SIGHUP`

Reloads server configuration file

`--signal reopen`

`SIGUSR1`

Reopens the log file for log rotation

 _(kill only)_

`SIGQUIT`

Kills the process immediately and performs a [stack dumparrow-up-right](https://pkg.go.dev/os/signal#hdr-Default_behavior_of_signals_in_Go_programs)

### 

[hashtag](#usage)

Usage

To send a signal to a running nats-server:

Copy

```

    nats-server --signal <command>

```

For example, to gracefully stop the server with lame duck mode:

Copy

```

    nats-server --signal ldm

```

### 

[hashtag](#multiple-processes)

Multiple processes

If there are multiple `nats-server` processes running, or if `pgrep` isn't available, you must either specify a PID or the absolute path to a PID file:

Copy

```

    nats-server --signal stop=<pid>

```

Copy

```

    nats-server --signal stop=/path/to/pidfile

```

As of NATS v2.10.0, a glob expression can be used to match one or more process IDs, such as:

Copy

```

    nats-server --signal ldm=12*

```

## 

[hashtag](#windows)

Windows

See the [Windows Service](https://docs.nats.io/running-a-nats-service/introduction/windows_srv) ([local](./../introduction/windows-srv.md)) section for information on signaling the NATS server on Windows.

[PreviousSlow Consumerschevron-left](https://docs.nats.io/running-a-nats-service/nats_admin/slow_consumers) ([local](./slow-consumers.md))[NextLame Duck Modechevron-right](https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode) ([local](./lame-duck-mode.md))

Last updated 5 months ago

Was this helpful?
