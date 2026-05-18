---
title: Naming Streams, Consumers, and Accounts
source: https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/naming
---

[githubEdit](https://github.com/nats-io/nats.docs/blob/master/running-a-nats-service/nats_admin/jetstream_admin/naming.md)chevron-down

block-quoteOn this pageblock-quote

  1. [Running a NATS service](https://docs.nats.io/running-a-nats-service) ([local](./../../../running-a-nats-service.md))chevron-right
  2. [Managing and Monitoring your NATS Server Infrastructure](https://docs.nats.io/running-a-nats-service/nats_admin) ([local](./../../../../09_chevron-right/10_managing-and-monitoring-your-nats-server-infrastructure-chev.md))chevron-right
  3. [Managing JetStream](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin) ([local](./../jetstream-admin.md))

# Naming Streams, Consumers, and Accounts

Stream, Consumer (durable name), and Account names are used in both the subject namespace used by JetStream and the filesystem backing JetStream persistence. This means that when naming streams, consumers, and accounts, names must adhere to subject naming rules as well as being friendly to the file system.

We recommend the following guideline for stream, consumer, and account names:

  * Alphanumeric values are recommended.

  * Spaces, tabs, period (`.`), greater than (`>`) or asterisk (`*`) are prohibited.

  * Path separators (i.e. forward slash and backward slash) are prohibited.

  * Limit name length: The JetStream storage directories will include the account, stream name, and consumer name, so a generally safe approach would be to keep names **under 32 characters.**

  * Do not use reserved file names like NUL, LPT1, etc.

  * Be aware that some file systems are case insensitive so do not use stream or account names that would collide in a file system. For example, `Foo` and `foo` would collide on a Windows or Mac OSx System.

We plan to address these limitations in a future release.

[PreviousAccount Informationchevron-left](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/account) ([local](./account.md))[NextStreamschevron-right](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/streams) ([local](./streams.md))

Last updated 3 years ago

Was this helpful?
