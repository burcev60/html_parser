---
title: Qdrant Tutorial Repository
source: https://qdrant.tech/documentation/tutorials-lp-overview/
---

# Qdrant Tutorial Repository

### Basic Tutorials

 _Get up and running with Qdrant in minutes._

Tutorial| Objective| Stack| Time| Level  
---|---|---|---|---  
[Qdrant Local Quickstart](https://qdrant.tech/documentation/quickstart/) ([local](./02_local-quickstart.md))| Basic CRUD operations and local deployment.| Python| 10m| Beginner  
[Semantic Search 101](https://qdrant.tech/documentation/tutorials-basics/search-beginners/) ([local](./09_tutorials/01_basics/01_semantic-search-101.md))| Build a search engine for science fiction books.| Python| 5m| Beginner  
  
* * *

### Search Engineering Tutorials

 _Master vector search modalities, reranking, and retrieval quality._

Tutorial| Objective| Stack| Time| Level  
---|---|---|---|---  
[Semantic Search Intro](https://qdrant.tech/documentation/tutorials-search-engineering/neural-search/) ([local](./09_tutorials/03_search-engineering/04_semantic-search-basics.md))| Deploy a search service for company descriptions.| FastAPI| 30m| Beginner  
[Hybrid Search with FastEmbed](https://qdrant.tech/documentation/tutorials-search-engineering/hybrid-search-fastembed/) ([local](./09_tutorials/03_search-engineering/07_hybrid-search-with-fastembed.md))| Combine dense and sparse search.| FastAPI| 20m| Beginner  
[Relevance Feedback](https://qdrant.tech/documentation/tutorials-search-engineering/using-relevance-feedback/) ([local](./09_tutorials/03_search-engineering/03_relevance-feedback-retrieval-in-qdrant.md))| Relevance Feedback Retrieval in Qdrant| Python| 30m| Intermediate  
[Collaborative Filtering](https://qdrant.tech/documentation/tutorials-search-engineering/collaborative-filtering/) ([local](./09_tutorials/03_search-engineering/06_collaborative-filtering.md))| Collaborative filtering using sparse embeddings.| Python| 45m| Intermediate  
[Multivector Document Retrieval](https://qdrant.tech/documentation/tutorials-search-engineering/pdf-retrieval-at-scale/) ([local](./09_tutorials/03_search-engineering/08_multivector-document-retrieval.md))| PDF RAG using ColPali and embedding pooling.| Python| 30m| Intermediate  
[Measuring ANN Recall](https://qdrant.tech/documentation/tutorials-search-engineering/ann-recall/) ([local](./09_tutorials/03_search-engineering/09_measuring-ann-recall.md))| Measure ANN recall with the Web UI and tune HNSW parameters.| Web UI| 15m| Beginner  
[Hybrid Search with Reranking](https://qdrant.tech/documentation/tutorials-search-engineering/reranking-hybrid-search/) ([local](./09_tutorials/03_search-engineering/01_hybrid-search-with-reranking.md))| Implement late interaction and sparse reranking.| Python| 40m| Intermediate  
[Semantic Search for Code](https://qdrant.tech/documentation/tutorials-search-engineering/code-search/) ([local](./09_tutorials/03_search-engineering/05_semantic-search-for-code.md))| Navigate codebases using vector similarity.| Python| 45m| Intermediate  
[Multivectors and Late Interaction](https://qdrant.tech/documentation/tutorials-search-engineering/using-multivector-representations/) ([local](./09_tutorials/03_search-engineering/02_multivectors-and-late-interaction.md))| Effective use of multivector representations.| Python| 30m| Intermediate  
[Static Embeddings](https://qdrant.tech/documentation/tutorials-search-engineering/static-embeddings/) ([local](./09_tutorials/03_search-engineering/10_static-embeddings.md))| Evaluate the utility of static embeddings.| Python| 20m| Intermediate  
  
* * *

### Operations & Scale

 _Production-grade management, monitoring, and high-volume optimization._

Tutorial| Objective| Stack| Time| Level  
---|---|---|---|---  
[Snapshots](https://qdrant.tech/documentation/tutorials-operations/create-snapshot/) ([local](./09_tutorials/05_operations-scale/01_snapshots.md))| Create and restore collection snapshots.| Python| 20m| Beginner  
[Data Migration](https://qdrant.tech/documentation/tutorials-operations/migration/) ([local](./09_tutorials/05_operations-scale/02_data-migration.md))| Move embeddings to Qdrant.| CLI| 30m| Intermediate  
[Embedding Model Migration](https://qdrant.tech/documentation/tutorials-operations/embedding-model-migration/) ([local](./09_tutorials/05_operations-scale/03_migrate-to-a-new-embedding-model.md))| Use your new model with zero downtime.| None| 40m| Intermediate  
[Time-Based Sharding](https://qdrant.tech/documentation/tutorials-operations/time-based-sharding/) ([local](./09_tutorials/05_operations-scale/04_time-based-sharding.md))| Efficiently manage time-series data with user-defined sharding.| None| 1h| Intermediate  
[Large-Scale Search](https://qdrant.tech/documentation/tutorials-operations/large-scale-search/) ([local](./09_tutorials/05_operations-scale/05_large-scale-search.md))| Cost-efficient search for LAION-400M datasets.| None| 48h| Advanced  
[Qdrant Cloud Prometheus Monitoring](https://qdrant.tech/documentation/ops-monitoring/managed-cloud-prometheus/) ([local](./_unsorted/ops-monitoring/managed-cloud-prometheus.md))| Observability with Prometheus and Grafana.| Prometheus| 30m| Intermediate  
[Self-Hosted Prometheus Monitoring](https://qdrant.tech/documentation/ops-monitoring/hybrid-cloud-prometheus/) ([local](./_unsorted/ops-monitoring/hybrid-cloud-prometheus.md))| Observability for hybrid/private cloud setups.| Prometheus| 30m| Intermediate  
  
* * *

### Develop & Implement

 _Core tools and APIs for building with Qdrant._

Tutorial| Objective| Stack| Time| Level  
---|---|---|---|---  
[Bulk Operations](https://qdrant.tech/documentation/tutorials-develop/bulk-upload/) ([local](./09_tutorials/07_develop-implement/01_bulk-operations.md))| High-scale ingestion approaches.| Python| 20m| Intermediate  
[Async API](https://qdrant.tech/documentation/tutorials-develop/async-api/) ([local](./09_tutorials/07_develop-implement/02_async-api.md))| Use Asynchronous programming for efficiency.| Python| 25m| Intermediate  
  
* * *

### Migrate to Qdrant

 _Move your vectors from other databases and keep them in sync._

Tutorial| Objective| Stack| Time| Level  
---|---|---|---|---  
[Migration Tool Overview](https://qdrant.tech/documentation/migrate-to-qdrant/) ([local](./_unsorted/migrate-to-qdrant.md))| Migrate vectors from any supported source.| CLI| Varies| Intermediate  
[From Pinecone](https://qdrant.tech/documentation/migrate-to-qdrant/from-pinecone/) ([local](./_unsorted/migrate-to-qdrant/from-pinecone.md))| Migrate from Pinecone serverless indexes.| CLI| 15m| Intermediate  
[From Weaviate](https://qdrant.tech/documentation/migrate-to-qdrant/from-weaviate/) ([local](./_unsorted/migrate-to-qdrant/from-weaviate.md))| Migrate from Weaviate (pre-create collection).| CLI| 20m| Intermediate  
[From Milvus](https://qdrant.tech/documentation/migrate-to-qdrant/from-milvus/) ([local](./_unsorted/migrate-to-qdrant/from-milvus.md))| Migrate from Milvus/Zilliz with partitions.| CLI| 15m| Intermediate  
[From Elasticsearch](https://qdrant.tech/documentation/migrate-to-qdrant/from-elasticsearch/) ([local](./_unsorted/migrate-to-qdrant/from-elasticsearch.md))| Migrate dense vectors from Elasticsearch.| CLI| 15m| Intermediate  
[From pgvector](https://qdrant.tech/documentation/migrate-to-qdrant/from-pgvector/) ([local](./_unsorted/migrate-to-qdrant/from-pgvector.md))| Migrate from PostgreSQL pgvector tables.| CLI| 15m| Intermediate  
[Migration Verification](https://qdrant.tech/documentation/migration-guidance/) ([local](./_unsorted/migration-guidance.md))| Verify data integrity and search quality.| Python| 1h+| Intermediate  
[Keeping Postgres in Sync](https://qdrant.tech/documentation/data-synchronization/) ([local](./_unsorted/data-synchronization.md))| Keep Postgres and Qdrant in sync.| Python| 30m| Intermediate
