---
title: Qdrant Edge Quickstart
source: https://qdrant.tech/documentation/edge/edge-quickstart/
---

# Qdrant Edge Quickstart

## Install Qdrant Edge

First, install the [Python Bindings for Qdrant Edge](https://pypi.org/project/qdrant-edge-py/) or the [Rust crate](https://crates.io/crates/qdrant-edge).

## Create a Storage Directory

A Qdrant Edge Shard stores its data in a local directory on disk. Create the directory if it doesn’t exist yet:

```

    from pathlib import Path
    
    SHARD_DIRECTORY = "./qdrant-edge-directory"
    
    Path(SHARD_DIRECTORY).mkdir(parents=True, exist_ok=True)
    

```

```

    const SHARD_DIRECTORY: &str = "./qdrant-edge-directory";
    
    fs_err::create_dir_all(SHARD_DIRECTORY)?;
    

```

## Configure the Edge Shard

An Edge Shard is configured with a definition of the dense and sparse vectors that can be stored in the Edge Shard, similar to how you would configure a Qdrant collection.

Set up a configuration by creating an instance of `EdgeConfig`. For example:

```

    from qdrant_edge import (
        Distance,
        EdgeConfig,
        EdgeVectorParams,
    )
    
    VECTOR_NAME="my-vector"
    VECTOR_DIMENSION=4
    
    config = EdgeConfig(
        vectors={
            VECTOR_NAME: EdgeVectorParams(
                size=VECTOR_DIMENSION,
                distance=Distance.Cosine,
            )
        }
    )
    

```

```

    const VECTOR_NAME: &str = "my-vector";
    const VECTOR_DIMENSION: usize = 4;
    
    let config = EdgeConfig {
        on_disk_payload: true,
        vectors: HashMap::from([(
            VECTOR_NAME.to_string(),
            EdgeVectorParams {
                size: VECTOR_DIMENSION,
                distance: Distance::Cosine,
                on_disk: Some(true),
                quantization_config: None,
                multivector_config: None,
                datatype: None,
                hnsw_config: None,
            },
        )]),
        sparse_vectors: HashMap::new(),
        hnsw_config: Default::default(),
        quantization_config: None,
        optimizers: Default::default(),
    };
    

```

## Initialize the Edge Shard

Now you can create a new `EdgeShard` using `EdgeShard.create` (Python) or `EdgeShard::new` (Rust), passing the storage directory and configuration:

```

    from qdrant_edge import EdgeShard
    
    edge_shard = EdgeShard.create(SHARD_DIRECTORY, config)
    

```

```

    let edge_shard = EdgeShard::new(
        Path::new(SHARD_DIRECTORY),
        config,
    )?;
    

```

Note that `create` and `new` will fail if the storage directory already contains data. To initialize an Edge Shard with existing data, see [Load Existing Edge Shard from Disk](#load-existing-edge-shard-from-disk).

## Work with Points

An Edge Shard has several methods to work with points. To add points, use the `update` method:

```

    from qdrant_edge import ( Point, UpdateOperation )
    
    point = Point(
        id=1,
        vector={VECTOR_NAME: [0.1, 0.2, 0.3, 0.4]},
        payload={"color": "red"}
    )
    
    edge_shard.update(UpdateOperation.upsert_points([point]))
    

```

```

    let points: Vec<PointStructPersisted> = vec![
        PointStruct::new(
            1u64,
            Vectors::new_named([(VECTOR_NAME, vec![0.1f32, 0.2, 0.3, 0.4])]),
            json!({"color": "red"}),
        )
        .into(),
    ];
    
    edge_shard.update(UpdateOperation::PointOperation(
        PointOperations::UpsertPoints(
            PointInsertOperations::PointsList(points),
        ),
    ))?;
    

```

To retrieve a point by ID, use the `retrieve` method:

```

    records = edge_shard.retrieve(
        point_ids=[1],
        with_payload=True,
        with_vector=False
    )
    

```

```

    let retrieved = edge_shard.retrieve(
        &[PointId::NumId(1)],
        Some(WithPayloadInterface::Bool(true)),
        Some(WithVector::Bool(false)),
    )?;
    

```

## Create a Payload Index

To optimize operations like [filtering](#filtering) and [faceting](#faceting) on payload fields, first create a payload index on the fields you plan to use with these operations:

```

    from qdrant_edge import PayloadSchemaType
    
    edge_shard.update(UpdateOperation.create_field_index("color", PayloadSchemaType.Keyword))
    

```

```

    edge_shard.update(UpdateOperation::FieldIndexOperation(
        FieldIndexOperations::CreateIndex(CreateIndex {
            field_name: "color".try_into().unwrap(),
            field_schema: Some(PayloadFieldSchema::FieldType(
                PayloadSchemaType::Keyword,
            )),
        }),
    ))?;
    

```

## Query Points

To query points in the Edge Shard, use the `query` method:

```

    from qdrant_edge import Query, QueryRequest
    
    results = edge_shard.query(
        QueryRequest(
            query=Query.Nearest([0.2, 0.1, 0.9, 0.7], using=VECTOR_NAME),
            limit=10,
            with_vector=False,
            with_payload=True
        )
    )
    

```

```

    let results = edge_shard.query(QueryRequest {
        prefetches: vec![],
        query: Some(ScoringQuery::Vector(QueryEnum::Nearest(NamedQuery {
            query: vec![0.2f32, 0.1, 0.9, 0.7].into(),
            using: Some(VECTOR_NAME.to_string()),
        }))),
        filter: None,
        score_threshold: None,
        limit: 10,
        offset: 0,
        params: None,
        with_vector: WithVector::Bool(false),
        with_payload: WithPayloadInterface::Bool(true),
    })?;
    

```

## Filter points

You can also filter points based on payload fields:

```

    from qdrant_edge import FieldCondition, Filter, MatchValue
    
    results = edge_shard.query(
        QueryRequest(
            query=Query.Nearest([0.2, 0.1, 0.9, 0.7], using=VECTOR_NAME),
            filter=Filter(
                must=[
                    FieldCondition(
                        key="color",
                        match=MatchValue(value="red"),
                    )
                ]
            ),
            limit=10,
            with_vector=False,
            with_payload=True
        )
    )
    

```

```

    let filter = Filter {
        should: None,
        min_should: None,
        must: Some(vec![Condition::Field(FieldCondition::new_match(
            "color".try_into().unwrap(),
            Match::Value(MatchValue {
                value: ValueVariants::String("red".to_string()),
            }),
        ))]),
        must_not: None,
    };
    
    let results = edge_shard.query(QueryRequest {
        prefetches: vec![],
        query: Some(ScoringQuery::Vector(QueryEnum::Nearest(NamedQuery {
            query: vec![0.2f32, 0.1, 0.9, 0.7].into(),
            using: Some(VECTOR_NAME.to_string()),
        }))),
        filter: Some(filter),
        score_threshold: None,
        limit: 10,
        offset: 0,
        params: None,
        with_vector: WithVector::Bool(false),
        with_payload: WithPayloadInterface::Bool(true),
    })?;
    

```

## Create Facets

To create facets on a payload field, use the `facet` method.

```

    from qdrant_edge import FacetRequest
    
    facet_response = edge_shard.facet(FacetRequest(key="color", limit=10, exact=False))
    

```

```

    let facet_response = edge_shard.facet(FacetRequest {
        key: "color".try_into().unwrap(),
        limit: 10,
        filter: None,
        exact: false,
    })?;
    

```

## Optimize the Edge Shard

Optimization is the process of removing data marked for deletion, merging segments, and creating indexes. Qdrant Edge does not have a background optimizer. Instead, an application can call the `optimize` method to synchronously run optimization at a suitable time, such as during low-traffic periods or after a batch of updates.

```

    edge_shard.optimize()
    

```

```

    edge_shard.optimize()?;
    

```

The optimizer can be configured using the `optimizers` parameter of `EdgeConfig` when initializing the Edge Shard. For example:

```

    from qdrant_edge import EdgeOptimizersConfig
    
    config = EdgeConfig(
        vectors={
            VECTOR_NAME: EdgeVectorParams(
                size=VECTOR_DIMENSION,
                distance=Distance.Cosine,
            )
        },
        optimizers=EdgeOptimizersConfig(
            deleted_threshold=0.2,
            vacuum_min_vector_number=100,
            default_segment_number=2,
        ),
    )
    

```

```

    let config = EdgeConfig {
        on_disk_payload: true,
        vectors: HashMap::from([(
            VECTOR_NAME.to_string(),
            EdgeVectorParams {
                size: VECTOR_DIMENSION,
                distance: Distance::Cosine,
                on_disk: Some(true),
                quantization_config: None,
                multivector_config: None,
                datatype: None,
                hnsw_config: None,
            },
        )]),
        sparse_vectors: HashMap::new(),
        hnsw_config: Default::default(),
        quantization_config: None,
        optimizers: EdgeOptimizersConfig {
            deleted_threshold: Some(0.2),
            vacuum_min_vector_number: Some(100),
            default_segment_number: Some(2),
            ..Default::default()
        },
    };
    

```

## Close the Edge Shard

When shutting down your application, close the Edge Shard to ensure all data is flushed to disk. The data is persisted on disk and can be used to reopen the Edge Shard.

```

    edge_shard.close()
    

```

```

    drop(edge_shard);
    

```

## Load Existing Edge Shard from Disk

After closing an Edge Shard, you can reopen it by loading its data and configuration from disk using the `load` method:

```

    edge_shard = EdgeShard.load(SHARD_DIRECTORY)
    

```

```

    let edge_shard = EdgeShard::load(Path::new(SHARD_DIRECTORY), None)?;
    

```

## More Examples

The Qdrant GitHub repository contains examples of using the Qdrant Edge API in [Python](https://github.com/qdrant/qdrant/tree/dev/lib/edge/python/examples) and [Rust](https://github.com/qdrant/qdrant/tree/dev/lib/edge/publish/examples).
