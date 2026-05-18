---
title: Profiling
source: https://docs.nats.io/running-a-nats-service/nats_admin/profiling
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/profiling.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../running-a-nats-service.md))chevron-right
  2. [Managing and Monitoring your NATS Server Infrastructure](https://docs.nats.io/running-a-nats-service/nats_admin) ([local](./../../../09_chevron-right/10_managing-and-monitoring-your-nats-server-infrastructure-chev.md))

# Profiling

When investigating and debugging a performance issue with the NATS Server (i.e. unexpectedly high CPU or RAM utilisation), it may be necessary for you to collect and provide profiles from your deployment for troublshooting. These profiles are crucial to understand where CPU time and memory are being spent.

Note that profiling is an advanced operation for development purposes only. Server operators should use the [monitoring port](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring) ([local](./monitoring.md)) instead for monitoring day-to-day runtime statistics.

### 

[hashtag](#via-the-nats-cli)

Via the NATS CLI

The NATS CLI can request profiles from the NATS Server **when connected to the system account only**. Profiles will be written out to the current working directory by default as files, which can then either be sent onwards or inspected using [`go tool pprof`arrow-up-right](https://pkg.go.dev/net/http/pprof).

#### 

[hashtag](#memory-profile)

Memory profile

The `--name`, `--tags` and `--cluster` selectors can be used either individually or combined in order to request profiles from specific servers. Memory profiles are returned instantly. Examples include:

Command

Description

`nats server request profile allocs`

Request a memory profile from all servers in the system

`nats server request profile allocs ./profiles`

Request a memory profile from all servers in the system and write to the `profiles` directory

`nats server request profile allocs --name=servername1`

Request a memory profile from `servername1` only

`nats server request profile allocs --tags=aws`

Request a memory profile from all servers tagged as `aws`

`nats server request profile allocs --cluster=aws-useast2`

Request a memory profile from all servers in the cluster named `aws-useast2` only

#### 

[hashtag](#cpu-profile)

CPU profile

The `--name`, `--tags` and `--cluster` selectors can be used either individually or combined in order to request profiles from specific servers. The `--timeout` option can also be provided as a means of specifying how long the CPU profile should run for. The default is 5 seconds. Examples include:

Command

Description

`nats server request profile cpu`

Request a CPU profile from all servers in the system

`nats server request profile cpu ./profiles`

Request a CPU profile from all servers in the system and write to the `profiles` directory

`nats server request profile cpu --timeout=10s`

Request a CPU profile from all servers in the system over a 10 second period

`nats server request profile cpu --name=servername1`

Request a CPU profile from `servername1` only

`nats server request profile cpu --tags=aws`

Request a CPU profile from all servers tagged as `aws`

`nats server request profile cpu --cluster=aws-useast2`

Request a CPU profile from all servers in the cluster named `aws-useast2` only

### 

[hashtag](#via-the-profiling-port)

Via the Profiling Port

circle-exclamation

`nats-server` does not have authentication/authorization for the profiling endpoint. When you plan to open your `nats-server` to the internet make sure to not expose the profiling port as well. By default, profiling binds to every interface `0.0.0.0` so consider setting profiling to `localhost` or have appropriate firewall rules.

The NATS Server can expose a HTTP `pprof` profiling port, although it must be enabled by setting the `prof_port` in your NATS Server configuration file. Note that the profiling port is not authenticated and should not be exposed to clients, to the internet etc. For example, to enable the profiling port on TCP/65432:

Copy

```

    prof_port = 65432

```

Note that this option does not support [configuration-reloading](https://docs.nats.io/running-a-nats-service/configuration#configuration-reloading) ([local](./../../../09_chevron-right/08_configuring-nats-server-chevron-right.md#configuration-reloading)), so the server must be restarted for the config change to take effect.

Once the profiling port has been enabled, you can download profiles as per the following sections. These profiles can be inspected using [`go tool pprof`arrow-up-right](https://pkg.go.dev/net/http/pprof).

To see all available profiles, open <http://localhost:65432/debug/pprof/>[arrow-up-right](http://localhost:65432/debug/pprof/)

#### 

[hashtag](#memory-profile-1)

Memory profile

`http://localhost:65432/debug/pprof/allocs`

This endpoint will return instantly.

For example, to download an allocation profile from NATS running on the same machine:

Copy

```

    curl -o mem.prof http://localhost:65432/debug/pprof/allocs

```

The profile will be saved into `mem.prof`.

#### 

[hashtag](#cpu-profile-1)

CPU profile

`http://localhost:65432/debug/pprof/profile?seconds=30`

This endpoint will block for the specified duration and then return. You can specify a different duration by adjusting `?seconds=` in the URL if you want to sample a shorter or longer period of time.

For example, to download a CPU profile from NATS running on the same machine with a 30 second window:

Copy

```

    curl -o cpu.prof http://localhost:65432/debug/pprof/profile?seconds=30

```

The profile will be saved into `cpu.prof`.

[PreviousLame Duck Modechevron-left](https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode) ([local](./lame-duck-mode.md))[NextFAQchevron-right](https://docs.nats.io/reference/faq) ([local](./../../../11_chevron-right/01_faq.md))

Last updated 1 year ago

Was this helpful?
