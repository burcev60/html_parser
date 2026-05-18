---
title: System Events & Decentralized JWT Tutorial
source: https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/configuration/sys_accounts/sys_accounts.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../running-a-nats-service.md))chevron-right
  2. [Configuring NATS Server](https://docs.nats.io/running-a-nats-service/configuration) ([local](./../../../../09_chevron-right/08_configuring-nats-server-chevron-right.md))chevron-right
  3. [System Events](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts) ([local](./../sys-accounts.md))

# System Events & Decentralized JWT Tutorial

## 

[hashtag](#enabling-system-events-with-decentralized-authentication-authorization)

Enabling System Events with Decentralized Authentication/Authorization

To enable and access system events, you'll have to:

  * Create an Operator, Account and User

  * Run a NATS Account Server (or Memory Resolver)

### 

[hashtag](#create-an-operator-account-user)

Create an Operator, Account, User

Let's create an operator, system account and system account user:

Copy

```

    nsc add operator -n SAOP

```

Copy

```

    Generated operator key - private key stored "~/.nkeys/SAOP/SAOP.nk"
    Success! - added operator "SAOP"

```

Add the system account

Copy

```

    nsc add account -n SYS

```

Copy

```

    Generated account key - private key stored "~/.nkeys/SAOP/accounts/SYS/SYS.nk"
    Success! - added account "SYS"

```

Add a system account user

Copy

```

    nsc add user -n SYSU

```

Copy

```

    Generated user key - private key stored "~/.nkeys/SAOP/accounts/SYS/users/SYSU.nk"
    Generated user creds file "~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds"
    Success! - added user "SYSU" to "SYS"

```

By default, the operator JWT can be found in `~/.nsc/nats/<operator_name>/<operator.name>.jwt`.

### 

[hashtag](#nats-account-server)

NATS-Account-Server

To vend the credentials to the nats-server, we'll use a [nats-account-serverarrow-up-right](https://github.com/nats-io/nats.docs/blob/master/legacy/nas/README.md). Let's start a nats-account-server to serve the JWT credentials:

Copy

```

    nats-account-server -nsc ~/.nsc/nats/SAOP

```

The server will by default vend JWT configurations on the an endpoint at: `http(s)://<server_url>/jwt/v1/accounts/`.

### 

[hashtag](#nats-server-configuration)

NATS Server Configuration

The server configuration will need:

  * The operator JWT - (`~/.nsc/nats/<operator_name>/<operator.name>.jwt`)

  * The URL where the server can resolve accounts (`http://localhost:9090/jwt/v1/accounts/`)

  * The public key of the `system_account`

The only thing we don't have handy is the public key for the system account. We can get it easy enough:

Copy

```

    nsc list accounts

```

Copy

```

    ╭─────────────────────────────────────────────────────────────────╮
    │                            Accounts                             │
    ├──────┬──────────────────────────────────────────────────────────┤
    │ Name │ Public Key                                               │
    ├──────┼──────────────────────────────────────────────────────────┤
    │ SYS  │ ADWJVSUSEVC2GHL5GRATN2LOEOQOY2E6Z2VXNU3JEIK6BDGPWNIW3AXF │
    ╰──────┴──────────────────────────────────────────────────────────╯

```

Because the server has additional resolver implementations, you need to enclose the server url like: `URL(<url>)`.

Let's create server config with the following contents and save it to `server.conf`:

Copy

```

    operator: /Users/synadia/.nsc/nats/SAOP/SAOP.jwt
    system_account: ADWJVSUSEVC2GHL5GRATN2LOEOQOY2E6Z2VXNU3JEIK6BDGPWNIW3AXF
    resolver: URL(http://localhost:9090/jwt/v1/accounts/)

```

Let's start the nats-server:

Copy

```

    nats-server -c server.conf

```

## 

[hashtag](#inspecting-server-events)

Inspecting Server Events

Let's add a subscriber for all the events published by the system account:

Copy

```

    nats sub --creds ~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds ">"

```

Very quickly we'll start seeing messages from the server as they are published by the NATS server. As should be expected, the messages are just JSON, so they can easily be inspected even if just using a simple `nats sub` to read them.

To see an account update:

Copy

```

    nats pub --creds ~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds foo bar

```

The subscriber will print the connect and disconnect:

Copy

```

    {
      "server": {
        "host": "0.0.0.0",
        "id": "NBTGVY3OKDKEAJPUXRHZLKBCRH3LWCKZ6ZXTAJRS2RMYN3PMDRMUZWPR",
        "ver": "2.0.0-RC5",
        "seq": 32,
        "time": "2019-05-03T14:53:15.455266-05:00"
      },
      "acc": "ADWJVSUSEVC2GHL5GRATN2LOEOQOY2E6Z2VXNU3JEIK6BDGPWNIW3AXF",
      "conns": 1,
      "total_conns": 1
    }
    {
      "server": {
        "host": "0.0.0.0",
        "id": "NBTGVY3OKDKEAJPUXRHZLKBCRH3LWCKZ6ZXTAJRS2RMYN3PMDRMUZWPR",
        "ver": "2.0.0-RC5",
        "seq": 33,
        "time": "2019-05-03T14:53:15.455304-05:00"
      },
      "client": {
        "start": "2019-05-03T14:53:15.453824-05:00",
        "host": "127.0.0.1",
        "id": 6,
        "acc": "ADWJVSUSEVC2GHL5GRATN2LOEOQOY2E6Z2VXNU3JEIK6BDGPWNIW3AXF",
        "user": "UACPEXCAZEYWZK4O52MEGWGK4BH3OSGYM3P3C3F3LF2NGNZUS24IVG36",
        "name": "NATS Sample Publisher",
        "lang": "go",
        "ver": "1.7.0",
        "stop": "2019-05-03T14:53:15.45526-05:00"
      },
      "sent": {
        "msgs": 1,
        "bytes": 3
      },
      "received": {
        "msgs": 0,
        "bytes": 0
      },
      "reason": "Client Closed"
    }

```

## 

[hashtag](#user-services)

User Services

### 

[hashtag](#usdsys.req.user.info-request-connected-user-information)

`$SYS.REQ.USER.INFO` \- Request Connected User Information

For the active connection, get basic user information including the account name, permissions, and expiry, if applicable. Note, this works with any connected user, not just a system account user.

Copy

```

    nats request --creds ~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds \$SYS.REQ.USER.INFO ""

```

Copy

```

    Published [$SYS.REQ.USER.INFO] : ''
    Received  [_INBOX.DQD44ugVt0O4Ur3pWIOOD1.WQOBevoq] : '{
      "user": "UACPEXCAZEYWZK4O52MEGWGK4BH3OSGYM3P3C3F3LF2NGNZUS24IVG36",
      "account": "ADWJVSUSEVC2GHL5GRATN2LOEOQOY2E6Z2VXNU3JEIK6BDGPWNIW3AXF"
    }'

```

## 

[hashtag](#system-services)

System Services

### 

[hashtag](#usdsys.req.server.ping.idz-discovering-servers)

`$SYS.REQ.SERVER.PING.IDZ` \- Discovering Servers

To discover servers in the cluster to get their ID and name, publish a request to `$SYS.REQ.SERVER.PING.IDZ`.

Copy

```

    nats request --creds ~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds \$SYS.REQ.SERVER.PING.IDZ ""

```

Copy

```

    Published [$SYS.REQ.SERVER.PING.IDZ] : ''
    Received  [_INBOX.DQD44ugVt0O4Ur3pWIOOD1.WQOBevoq] : '{
      "host": "0.0.0.0",
      "id": "NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL",
      "name": "n1"
    }'

```

### 

[hashtag](#usdsys.req.server.ping-discovering-servers--stats)

`$SYS.REQ.SERVER.PING` \- Discovering Servers + Stats

To discover servers in the cluster, and get a small health summary, publish a request to `$SYS.REQ.SERVER.PING`. Note that while the example below uses `nats-req`, only the first answer for the request will be printed. You can easily modify the example to wait until no additional responses are received for a specific amount of time, thus allowing for all responses to be collected.

Copy

```

    nats request --creds ~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds \$SYS.REQ.SERVER.PING ""

```

Copy

```

    Published [$SYS.REQ.SERVER.PING] : ''
    Received  [_INBOX.G5mbsf0k7l7nb4eWHa7GTT.omklmvnm] : '{
      "server": {
        "host": "0.0.0.0",
        "id": "NCZQDUX77OSSTGN2ESEOCP4X7GISMARX3H4DBGZBY34VLAI4TQEPK6P6",
        "ver": "2.0.0-RC9",
        "seq": 47,
        "time": "2019-05-02T14:02:46.402166-05:00"
      },
      "statsz": {
        "start": "2019-05-02T13:41:01.113179-05:00",
        "mem": 12922880,
        "cores": 20,
        "cpu": 0,
        "connections": 2,
        "total_connections": 2,
        "active_accounts": 1,
        "subscriptions": 10,
        "sent": {
          "msgs": 7,
          "bytes": 2761
        },
        "received": {
          "msgs": 0,
          "bytes": 0
        },
        "slow_consumers": 0
      }
    }'

```

### 

[hashtag](#usdsys.req.server.less-than-id-greater-than.statsz-requesting-server-stats-summary)

`$SYS.REQ.SERVER.<id>.STATSZ` \- Requesting Server Stats Summary

If you know the server id for a particular server (such as from a response to `$SYS.REQ.SERVER.PING`), you can query the specific server for its health information:

Copy

```

    nats request --creds ~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds \$SYS.REQ.SERVER.NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL.STATSZ ""

```

Copy

```

    Published [$SYS.REQ.SERVER.NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL.STATSZ] : ''
    Received  [_INBOX.DQD44ugVt0O4Ur3pWIOOD1.WQOBevoq] : '{
      "server": {
        "host": "0.0.0.0",
        "id": "NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL",
        "ver": "2.0.0-RC5",
        "seq": 25,
        "time": "2019-05-03T14:34:02.066077-05:00"
      },
      "statsz": {
        "start": "2019-05-03T14:32:19.969037-05:00",
        "mem": 11874304,
        "cores": 20,
        "cpu": 0,
        "connections": 2,
        "total_connections": 4,
        "active_accounts": 1,
        "subscriptions": 10,
        "sent": {
          "msgs": 26,
          "bytes": 9096
        },
        "received": {
          "msgs": 2,
          "bytes": 0
        },
        "slow_consumers": 0
      }
    }'

```

### 

[hashtag](#usdsys.req.server.less-than-id-greater-than.profilez-request-profiling-information)

`$SYS.REQ.SERVER.<id>.PROFILEZ` \- Request Profiling Information

If profiling is enabled for a server, this service enables requesting it from the server. The request payload must specify the name of the profile being requested with an optional debug level, including:

  * `allocs` \- 0, 1

  * `block` \- 0

  * `goroutine` \- 0, 1, 2

  * `heap` \- 0, 1

  * `mutex` \- 0

  * `threadcount` \- 0

Copy

```

    nats request --creds ~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds \$SYS.REQ.SERVER.NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL.PROFILEZ '{"name": "heap", "debug": 1}'

```

Copy

```

    Published [$SYS.REQ.SERVER.NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL.PROFILEZ] : '{
      "name": "heap",
      "debug": 1
    }'
    Received  [_INBOX.DQD44ugVt0O4Ur3pWIOOD1.WQOBevoq] : '{
      "profile": "<base64-encoded profile output>"
    }'

```

### 

[hashtag](#usdsys.req.server.less-than-id-greater-than.reload-hot-reload-configuration)

`$SYS.REQ.SERVER.<id>.RELOAD` \- Hot Reload Configuration

Sending a request to this service will attempt to hot reload the server configuration, akin to `nats-server --signal reload`. If there are errors with the new configuration, they will be returned in an `error` field in the response.

Copy

```

    nats request --creds ~/.nkeys/SAOP/accounts/SYS/users/SYSU.creds \$SYS.REQ.SERVER.NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL.RELOAD ''

```

Copy

```

    Published [$SYS.REQ.SERVER.NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL.RELOAD] : ''
    Received  [_INBOX.DQD44ugVt0O4Ur3pWIOOD1.WQOBevoq] : '{
      "server": {
        "host": "0.0.0.0",
        "id": "NC7AKPQRC6CIZGWRJOTVFIGVSL7VW7WXTQCTUJFNG7HTCMCKQTGE5PUL",
        "ver": "2.10.0-RC5",
        "seq": 25,
        "time": "2023-09-19T14:34:02.066077-04:00"
      }
    }'

```

[PreviousSystem Eventschevron-left](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts) ([local](./../sys-accounts.md))[NextWebSocketchevron-right](https://docs.nats.io/running-a-nats-service/configuration/websocket) ([local](./../websocket.md))

Last updated 2 years ago

Was this helpful?
