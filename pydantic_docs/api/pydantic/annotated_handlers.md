---
title: Annotated Handlers
source: https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/
---

Type annotations to use with `__get_pydantic_core_schema__` and `__get_pydantic_json_schema__`.

## GetJsonSchemaHandler 

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetJsonSchemaHandler> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetJsonSchemaHandler)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetJsonSchemaHandler))

Handler to call into the next JSON schema generation function.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#attributes> ([local](./annotated_handlers.md#attributes)) ([local](./annotated_handlers.md#attributes))

#### mode 

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetJsonSchemaHandler.mode> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetJsonSchemaHandler.mode)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetJsonSchemaHandler.mode))

Json schema mode, can be `validation` or `serialization`.

**Type:** `JsonSchemaMode`

### Methods

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#methods> ([local](./annotated_handlers.md#methods)) ([local](./annotated_handlers.md#methods))

#### resolve_ref_schema 

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetJsonSchemaHandler.resolve_ref_schema> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetJsonSchemaHandler.resolve_ref_schema)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetJsonSchemaHandler.resolve_ref_schema))

```
 
    def resolve_ref_schema(maybe_ref_json_schema: JsonSchemaValue) -> JsonSchemaValue
    

```

Get the real schema for a `{"$ref": ...}` schema. If the schema given is not a `$ref` schema, it will be returned as is. This means you don’t have to check before calling this function.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#returns> ([local](./annotated_handlers.md#returns)) ([local](./annotated_handlers.md#returns))

`JsonSchemaValue` — A JsonSchemaValue that has no `$ref`.

##### Parameters

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#parameters> ([local](./annotated_handlers.md#parameters)) ([local](./annotated_handlers.md#parameters))

**`maybe_ref_json_schema`** : `JsonSchemaValue`

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetJsonSchemaHandler.resolve_ref_schema\(maybe_ref_json_schema\> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetJsonSchemaHandler.resolve_ref_schema\(maybe_ref_json_schema\)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetJsonSchemaHandler.resolve_ref_schema\(maybe_ref_json_schema\)))

A JsonSchemaValue which may be a `$ref` schema.

##### Raises

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#raises> ([local](./annotated_handlers.md#raises)) ([local](./annotated_handlers.md#raises))

  * `LookupError` — If the ref is not found.

## GetCoreSchemaHandler 

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetCoreSchemaHandler> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler))

Handler to call into the next CoreSchema schema generation function.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#attributes-1> ([local](./annotated_handlers.md#attributes-1)) ([local](./annotated_handlers.md#attributes-1))

#### field_name 

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetCoreSchemaHandler.field_name> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.field_name)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.field_name))

Get the name of the closest field to this validator.

**Type:** [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`None`](https://docs.python.org/3/library/constants.html#None)

### Methods

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#methods-1> ([local](./annotated_handlers.md#methods-1)) ([local](./annotated_handlers.md#methods-1))

#### generate_schema 

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetCoreSchemaHandler.generate_schema> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.generate_schema)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.generate_schema))

```
 
    def generate_schema(source_type: Any) -> core_schema.CoreSchema
    

```

Generate a schema unrelated to the current context. Use this function if e.g. you are handling schema generation for a sequence and want to generate a schema for its items. Otherwise, you may end up doing something like applying a `min_length` constraint that was intended for the sequence itself to its items!

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#returns-1> ([local](./annotated_handlers.md#returns-1)) ([local](./annotated_handlers.md#returns-1))

`core_schema.CoreSchema` — The `pydantic-core` CoreSchema generated.

##### Parameters

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#parameters-1> ([local](./annotated_handlers.md#parameters-1)) ([local](./annotated_handlers.md#parameters-1))

**`source_type`** : [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetCoreSchemaHandler.generate_schema\(source_type\> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.generate_schema\(source_type\)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.generate_schema\(source_type\)))

The input type.

#### resolve_ref_schema 

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetCoreSchemaHandler.resolve_ref_schema> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.resolve_ref_schema)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.resolve_ref_schema))

```
 
    def resolve_ref_schema(
        maybe_ref_schema: core_schema.CoreSchema,
    ) -> core_schema.CoreSchema
    

```

Get the real schema for a `definition-ref` schema. If the schema given is not a `definition-ref` schema, it will be returned as is. This means you don’t have to check before calling this function.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#returns-2> ([local](./annotated_handlers.md#returns-2)) ([local](./annotated_handlers.md#returns-2))

`core_schema.CoreSchema` — A concrete `CoreSchema`.

##### Parameters

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#parameters-2> ([local](./annotated_handlers.md#parameters-2)) ([local](./annotated_handlers.md#parameters-2))

**`maybe_ref_schema`** : `core_schema.CoreSchema`

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#pydantic.annotated_handlers.GetCoreSchemaHandler.resolve_ref_schema\(maybe_ref_schema\> ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.resolve_ref_schema\(maybe_ref_schema\)) ([local](./annotated_handlers.md#pydantic.annotated_handlers.GetCoreSchemaHandler.resolve_ref_schema\(maybe_ref_schema\)))

A `CoreSchema`, `ref`-based or not.

##### Raises

<https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/#raises-1> ([local](./annotated_handlers.md#raises-1)) ([local](./annotated_handlers.md#raises-1))

  * `LookupError` — If the `ref` is not found.
