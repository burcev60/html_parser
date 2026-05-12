---
title: Things to Check Before Taking Qdrant into Production
source: https://qdrant.tech/documentation/production-checklist/
---

# Things to Check Before Taking Qdrant into Production

A practical checklist to ensure Qdrant is optimized, stable, and ready to handle real-world load.

* * *

## 1\. Distributed Deployment & Sharding

Architect for scale from day one. Retrofitting these patterns onto an existing deployment is costly.

  * **Ensure you have enough shards to scale.** Qdrant [scales horizontally](https://qdrant.tech/documentation/distributed_deployment/) ([local](./distributed-deployment.md)) through [sharding](https://qdrant.tech/documentation/distributed_deployment/#sharding) ([local](./distributed-deployment.md#sharding)). Plan for enough shards to evenly distribute your data and load across the nodes in your cluster. At a minimum, you need one shard or replica per node.

  * **Ensure you don’t have too many shards.** While sharding is essential for scale, having too many shards can lead to performance degradation. Each collection has its own shards, so if you have many collections, you may end up with an excessive number of shards.

  * **Partition by payload instead of creating separate collections per user.** A common cause of too many shards is creating a separate collection for each user. Consider [partitioning by payload](https://qdrant.tech/documentation/manage-data/multitenancy/) ([local](./../04_user-manual/01_manage-data/08_multitenancy.md)) to logically isolate data for different users or groups within the same collection instead.

  * **Set up load balancing across nodes.** Distribute incoming requests evenly across cluster nodes to ensure consistent performance. Without load balancing, a single overloaded node can cause timeouts across your entire application. Qdrant Cloud includes a load balancer, but self-managed deployments need to configure one separately.

* * *

## 2\. Quantization

Compress vectors to reduce memory footprint. [Quantization](https://qdrant.tech/documentation/manage-data/quantization/) ([local](./../04_user-manual/01_manage-data/07_quantization.md)) is one of the most impactful changes you can make before going to production.

  * **Quantization** reduces the memory footprint of vectors, by compressing them to fewer bits. This enables you to store more vectors in memory and on disk, which can improve query performance and reduce costs. Qdrant supports multiple quantization methods, each with different trade-offs between recall, speed, and compression. [Choose the right method](https://qdrant.tech/documentation/manage-data/quantization/#how-to-choose-the-right-quantization-method) ([local](./../04_user-manual/01_manage-data/07_quantization.md#how-to-choose-the-right-quantization-method)) based on your requirements for recall, compression, and distance metrics.

  * **Benchmark retrieval quality after applying quantization.** Some models produce embeddings that can’t be quantized efficiently. [Verify](https://qdrant.tech/documentation/manage-data/quantization/#accuracy-tuning) ([local](./../04_user-manual/01_manage-data/07_quantization.md#accuracy-tuning)) that error rates stay within your acceptable threshold for your specific dataset and query patterns. Rescoring adds latency. [Tune](https://qdrant.tech/documentation/manage-data/quantization/#memory-and-speed-tuning) ([local](./../04_user-manual/01_manage-data/07_quantization.md#memory-and-speed-tuning)) quantization settings to ensure it meets your performance targets.

* * *

## 3\. Storage and Hardware

Right-size your RAM, disk type, and storage mode. These decisions are difficult to change once you’re in production.

  * **Choose between in-memory and on-disk/memmap storage.** In-memory gives maximum speed, but RAM becomes a bottleneck at scale. [On-disk/memmap](https://qdrant.tech/documentation/manage-data/storage/#configuring-memmap-storage) ([local](./../04_user-manual/01_manage-data/05_storage.md#configuring-memmap-storage)) maps data to disk-backed virtual address space, which is slightly slower but handles datasets larger than physical RAM.

  * **Estimate your RAM requirements before provisioning.** [Calculate](https://qdrant.tech/documentation/capacity-planning/) ([local](./capacity-planning.md)) your full dataset size and add headroom for vector and payload index overhead.

  * **Use SSDs for disk-backed storage, not HDDs.** SSDs are strongly recommended for workloads involving random reads and writes. HDDs introduce significant latency that can degrade query response times at scale.

  * **Keep frequently accessed data in memory.** [Keep hot collections in RAM](https://qdrant.tech/documentation/ops-optimization/optimize/) ([local](./ops-optimization/optimize.md)) to minimize disk I/O and speed up query execution. Identify your most-queried collections and prioritize them for in-memory storage.

  * **Enable inline storage.** When storing vectors and the HNSW index on disk, improve search performance by [enabling inline storage](https://qdrant.tech/documentation/ops-optimization/optimize/#inline-storage-in-hnsw-index) ([local](./ops-optimization/optimize.md#inline-storage-in-hnsw-index)). It makes searches faster by reducing the number of I/O operations, at the cost of increased storage usage.

* * *

## 4\. Query Optimization

Ensure your search is fast, accurate, and efficient under production load.

  * **Create[payload indexes](https://qdrant.tech/documentation/manage-data/indexing/#payload-index) ([local](./../04_user-manual/01_manage-data/06_indexing.md#payload-index)) on fields used for filtering.** Payload indexes speed up filtering and reduce load on the system. Identify which fields are commonly used in filters and create indexes on them. Create payload indexes before ingesting data. HNSW graphs are only [optimized for payload filtering](https://qdrant.tech/documentation/manage-data/indexing/#filterable-hnsw-index) ([local](./../04_user-manual/01_manage-data/06_indexing.md#filterable-hnsw-index)) when they are generated after payload index creation.

  * **Apply payload filters to narrow the search space.** Searching every data point is inefficient at scale. [Filtering](https://qdrant.tech/documentation/search/filtering/) ([local](./../04_user-manual/03_search/02_filtering.md)) on specific payload fields can reduce computational load and focus queries on relevant data subsets.

  * **[Query indexed data only](https://qdrant.tech/documentation/search/low-latency-search/#query-indexed-data-only) ([local](./../04_user-manual/03_search/07_low-latency-search.md#query-indexed-data-only)).** Under heavy write loads, large amounts of data may not be indexed immediately, which can slow down searches. To maintain consistent performance, only query indexed data.

  * **Evaluate whether[hybrid search](https://qdrant.tech/documentation/search/hybrid-queries/) ([local](./../04_user-manual/03_search/03_hybrid-queries.md)) fits your use case.** Hybrid search casts a wide retrieval net, maximizing recall by using multiple retrieval methods, such as combining dense vector search (semantic similarity) with sparse vector search (keyword matching). Evaluate its effectiveness for your specific dataset and queries.

  * **Rerank for maximum search relevance.** After initial hybrid retrieval, [rerank](https://qdrant.tech/documentation/search/hybrid-queries/#multi-stage-queries) ([local](./../04_user-manual/03_search/03_hybrid-queries.md#multi-stage-queries)) the results using late interaction embeddings. Reranking can be computationally expensive, so aim for a balance between relevance and speed. To save memory, disable the HNSW index for vectors used only for rescoring and factor the rescoring vector into your capacity planning (disk and RAM).

  * **Implement batch processing for inserts and queries.** [Group vector inserts into larger batches](https://qdrant.tech/documentation/manage-data/points/?q=batch#upload-points) ([local](./manage-data/points/q-batch.md#upload-points)) rather than individual transactions to reduce write overhead. [Batch multiple queries together](https://qdrant.tech/documentation/search/search/#batch-search-api) ([local](./../04_user-manual/03_search/01_search.md#batch-search-api)) to cut round trips to the database.

  * **Reduce tail latency with[delayed fan-outs](https://qdrant.tech/documentation/search/low-latency-search/#use-delayed-fan-outs) ([local](./../04_user-manual/03_search/07_low-latency-search.md#use-delayed-fan-outs)).** For collections with a replication factor higher than one, use delayed fan-outs to automatically query a second replica if the first one doesn’t respond within the desired latency threshold.
