---
title: Manage Data
source: https://qdrant.tech/documentation/manage-data/
---

# Manage Data

Learn how to structure, store, and organize your data in Qdrant. These pages cover the core building blocks — from individual records and the vectors that represent them, to collections, payloads, and the indexing and quantization options that control how data is stored and retrieved.

## Points

[Points](https://qdrant.tech/documentation/manage-data/points/) ([local](./01_manage-data/01_points.md)) are the fundamental unit of data in Qdrant — each point is a record consisting of a vector and an optional payload.

## Vectors

[Vectors](https://qdrant.tech/documentation/manage-data/vectors/) ([local](./01_manage-data/02_vectors.md)) define how data is represented in vector space, including support for dense, sparse, and multivector configurations.

## Payload

A [Payload](https://qdrant.tech/documentation/manage-data/payload/) ([local](./01_manage-data/03_payload.md)) is structured metadata you can attach to a point, enabling filtering and enriched search results.

## Collections

[Collections](https://qdrant.tech/documentation/manage-data/collections/) ([local](./01_manage-data/04_collections.md)) are named groups of points that share the same vector configuration and serve as the top-level organizational unit in Qdrant.

## Storage

[Storage](https://qdrant.tech/documentation/manage-data/storage/) ([local](./01_manage-data/05_storage.md)) describes how Qdrant persists vector and payload data, including segment structure and in-memory vs. on-disk options.

## Indexing

[Indexing](https://qdrant.tech/documentation/manage-data/indexing/) ([local](./01_manage-data/06_indexing.md)) covers the available index types — payload, vector, sparse, and filterable — and how they accelerate search and filtering.

## Quantization

[Quantization](https://qdrant.tech/documentation/manage-data/quantization/) ([local](./01_manage-data/07_quantization.md)) reduces memory usage by compressing vectors, with options for scalar, product, and binary quantization.

## Multitenancy

[Multitenancy](https://qdrant.tech/documentation/manage-data/multitenancy/) ([local](./01_manage-data/08_multitenancy.md)) explains strategies for isolating data across multiple users or tenants within a single Qdrant deployment.
