---
title: ToolJet
source: https://qdrant.tech/documentation/platforms/tooljet/
---

# ToolJet

[ToolJet](https://www.tooljet.com) is a low-code platform for building business applications. Connect to databases, cloud storages, GraphQL, API endpoints, Airtable, Google sheets, OpenAI, etc and build apps using drag and drop application builder.

## Prerequisites

  1. A Qdrant instance to connect to. You can get a free cloud instance at [cloud.qdrant.io](https://cloud.qdrant.io/).
  2. A [ToolJet instance](https://www.tooljet.com) to develop your workflows.

## Setting Up

  * Search for the Qdrant plugin in the Tooljet [plugins marketplace](https://docs.tooljet.ai/docs/marketplace/plugins/marketplace-plugin-qdrant/).

  * Set up the connection to Qdrant using your instance credentials.

![Qdrant Connection](https://qdrant.tech/documentation/platforms/tooljet/tooljet-connection.png)

You can interface with the Qdrant instance using the following Tooljet operations.

  * List Collections - Get the names of all the available collections in the Qdrant instance.

![Qdrant List Collections](https://qdrant.tech/documentation/platforms/tooljet/tooljet-list-collections.png)

  * Collection Info - Get the configuration of a specific collection.

![Qdrant Collection Info](https://qdrant.tech/documentation/platforms/tooljet/tooljet-collection-info.png)

  * Upsert Points - Add points to a collection.

![Qdrant Upsert Points](https://qdrant.tech/documentation/platforms/tooljet/tooljet-upsert-points.png)

  * Get Points - Get points from a collection by IDs or [filters](https://qdrant.tech/documentation/search/filtering/) ([local](./../../04_user-manual/03_search/02_filtering.md)).

![Qdrant Get Points](https://qdrant.tech/documentation/platforms/tooljet/tooljet-get-points.png)

  * Delete Points - Delete points from a collection by [filters](https://qdrant.tech/documentation/search/filtering/) ([local](./../../04_user-manual/03_search/02_filtering.md)).

![Qdrant Delete Points](https://qdrant.tech/documentation/platforms/tooljet/tooljet-delete-points.png)

  * Query Points - [Search](https://qdrant.tech/documentation/search/search/) ([local](./../../04_user-manual/03_search/01_search.md)) for points in a collection.

![Qdrant Query Points](https://qdrant.tech/documentation/platforms/tooljet/tooljet-query-points.png)

## Further Reading

  * [ToolJet Documentation](https://docs.tooljet.com/docs/).
  * [ToolJet Qdrant Plugin](https://docs.tooljet.ai/docs/marketplace/plugins/marketplace-plugin-qdrant/).
