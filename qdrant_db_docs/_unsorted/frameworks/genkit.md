---
title: Firebase Genkit
source: https://qdrant.tech/documentation/frameworks/genkit/
---

# Firebase Genkit

[Genkit](https://firebase.google.com/products/genkit) is a framework to build, deploy, and monitor production-ready AI-powered apps.

You can build apps that generate custom content, use semantic search, handle unstructured inputs, answer questions with your business data, autonomously make decisions, orchestrate tool calls, and more.

You can use Qdrant for indexing/semantic retrieval of data in your Genkit applications via the [Qdrant-Genkit plugin](https://github.com/qdrant/qdrant-genkit).

Genkit currently supports server-side development in JavaScript/TypeScript (Node.js) with Go support in active development.

## Installation

```

    npm i genkitx-qdrant
    

```

## Configuration

To use this plugin, specify it when you call `configureGenkit()`:

```

    import { qdrant } from 'genkitx-qdrant';
    
    const ai = genkit({
        plugins: [
            qdrant([
                {
                    embedder: googleAI.embedder('text-embedding-004'),
                    collectionName: 'collectionName',
                    clientParams: {
                        url: 'http://localhost:6333',
                    }
                }
            ]),
        ],
    });
    

```

You’ll need to specify a collection name, the embedding model you want to use and the Qdrant client parameters. In addition, there are a few optional parameters:

  * `embedderOptions`: Additional options to pass options to the embedder:

```
embedderOptions: { taskType: 'RETRIEVAL_DOCUMENT' },
        

```

  * `contentPayloadKey`: Name of the payload filed with the document content. Defaults to “content”.

```
contentPayloadKey: 'content';
        

```

  * `metadataPayloadKey`: Name of the payload filed with the document metadata. Defaults to “metadata”.

```
metadataPayloadKey: 'metadata';
        

```

  * `dataTypePayloadKey`: Name of the payload filed with the document datatype. Defaults to “_content_type”.

```
dataTypePayloadKey: '_datatype';
        

```

  * `collectionCreateOptions`: [Additional options](https://qdrant.tech/documentation/manage-data/collections/#create-a-collection) ([local](./../../04_user-manual/01_manage-data/04_collections.md#create-a-collection)) when creating the Qdrant collection.

## Usage

Import retriever and indexer references like so:

```

    import { qdrantIndexerRef, qdrantRetrieverRef } from 'genkitx-qdrant';
    

```

Then, pass their references to `retrieve()` and `index()`:

```

    // To export an indexer reference:
    export const qdrantIndexer = qdrantIndexerRef('collectionName', 'displayName');
    

```

```

    // To export a retriever reference:
    export const qdrantRetriever = qdrantRetrieverRef('collectionName', 'displayName');
    

```

You can refer to [Retrieval-augmented generation](https://genkit.dev/docs/rag/) for a general discussion on indexers and retrievers.

## Further Reading

  * [Introduction to Genkit](https://genkit.dev/)
  * [Genkit Documentation](https://genkit.dev/docs/get-started/)
  * [Source Code](https://github.com/qdrant/qdrant-genkit)
