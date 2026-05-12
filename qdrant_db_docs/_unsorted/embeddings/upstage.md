---
title: Upstage
source: https://qdrant.tech/documentation/embeddings/upstage/
---

# Upstage

Qdrant supports working with the Solar Embeddings API from [Upstage](https://upstage.ai/).

[Solar Embeddings](https://developers.upstage.ai/docs/apis/embeddings) API features dual models for user queries and document embedding, within a unified vector space, designed for performant text processing.

You can generate an API key to authenticate the requests from the [Upstage Console](https://console.upstage.ai/api-keys).

### Setting up the Qdrant client and Upstage session

```

    import requests
    from qdrant_client import QdrantClient
    
    UPSTAGE_BASE_URL = "https://api.upstage.ai/v1/solar/embeddings"
    
    UPSTAGE_API_KEY = "<YOUR_API_KEY>"
    
    upstage_session = requests.Session()
    
    client = QdrantClient(url="http://localhost:6333")
    
    headers = {
        "Authorization": f"Bearer {UPSTAGE_API_KEY}",
        "Accept": "application/json",
    }
    
    texts = [
        "Qdrant is the best vector search engine!",
        "Loved by Enterprises and everyone building for low latency, high performance, and scale.",
    ]
    

```

```

    import { QdrantClient } from '@qdrant/js-client-rest';
    
    const UPSTAGE_BASE_URL = "https://api.upstage.ai/v1/solar/embeddings"
    const UPSTAGE_API_KEY = "<YOUR_API_KEY>"
    
    const client = new QdrantClient({ url: 'http://localhost:6333' });
    
    const headers = {
        "Authorization": "Bearer " + UPSTAGE_API_KEY,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    const texts = [
        "Qdrant is the best vector search engine!",
        "Loved by Enterprises and everyone building for low latency, high performance, and scale.",
    ]
    

```

The following example shows how to embed documents with the recommended `solar-embedding-1-large-passage` and `solar-embedding-1-large-query` models that generates sentence embeddings of size 4096.

### Embedding documents

```

    body = {
        "input": texts,
        "model": "solar-embedding-1-large-passage",
    }
    
    response_body = upstage_session.post(
        UPSTAGE_BASE_URL, headers=headers, json=body
    ).json()
    

```

```

    let body = {
        "input": texts,
        "model": "solar-embedding-1-large-passage",
    }
    
    let response = await fetch(UPSTAGE_BASE_URL, {
        method: "POST",
        body: JSON.stringify(body),
        headers
    });
    
    let response_body = await response.json()
    

```

### Converting the model outputs to Qdrant points

```

    from qdrant_client.models import PointStruct
    
    points = [
        PointStruct(
            id=idx,
            vector=data["embedding"],
            payload={"text": text},
        )
        for idx, (data, text) in enumerate(zip(response_body["data"], texts))
    ]
    

```

```

    let points = response_body.data.map((data, i) => {
        return {
            id: i,
            vector: data.embedding,
            payload: {
                text: texts[i]
            }
        }
    })
    

```

### Creating a collection to insert the documents

```

    from qdrant_client.models import VectorParams, Distance
    
    collection_name = "example_collection"
    
    client.create_collection(
        collection_name,
        vectors_config=VectorParams(
            size=4096,
            distance=Distance.COSINE,
        ),
    )
    client.upsert(collection_name, points)
    

```

```

    const COLLECTION_NAME = "example_collection"
    
    await client.createCollection(COLLECTION_NAME, {
        vectors: {
            size: 4096,
            distance: 'Cosine',
        }
    });
    
    await client.upsert(COLLECTION_NAME, {
        wait: true,
        points
    })
    

```

## Searching for documents with Qdrant

Once all the documents are added, you can search for the most relevant documents.

```

    body = {
        "input": "What is the best to use for vector search scaling?",
        "model": "solar-embedding-1-large-query",
    }
    
    response_body = upstage_session.post(
        UPSTAGE_BASE_URL, headers=headers, json=body
    ).json()
    
    client.search(
        collection_name=collection_name,
        query_vector=response_body["data"][0]["embedding"],
    )
    

```

```

    body = {
        "input": "What is the best to use for vector search scaling?",
        "model": "solar-embedding-1-large-query",
    }
    
    response = await fetch(UPSTAGE_BASE_URL, {
        method: "POST",
        body: JSON.stringify(body),
        headers
    });
    
    response_body = await response.json()
    
    await client.search(COLLECTION_NAME, {
        vector: response_body.data[0].embedding,
    });
    

```
