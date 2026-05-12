---
title: Annotated Handlers
source: https://pydantic.dev/docs/validation/latest/api/pydantic/annotated_handlers/
---

Type annotations to use with `__get_pydantic_core_schema__` and `__get_pydantic_json_schema__`.

## GetJsonSchemaHandler 

#pydantic.annotated_handlers.GetJsonSchemaHandler

Handler to call into the next JSON schema generation function.

### Attributes

#attributes

#### mode 

#pydantic.annotated_handlers.GetJsonSchemaHandler.mode

Json schema mode, can be `validation` or `serialization`.

**Type:** `JsonSchemaMode`

### Methods

#methods

#### resolve_ref_schema 

#pydantic.annotated_handlers.GetJsonSchemaHandler.resolve_ref_schema

```
 
    def resolve_ref_schema(maybe_ref_json_schema: JsonSchemaValue) -> JsonSchemaValue
    

```

Get the real schema for a `{"$ref": ...}` schema. If the schema given is not a `$ref` schema, it will be returned as is. This means you don’t have to check before calling this function.

##### Returns

#returns

`JsonSchemaValue` — A JsonSchemaValue that has no `$ref`.

##### Parameters

#parameters

**`maybe_ref_json_schema`** : `JsonSchemaValue`

#pydantic.annotated_handlers.GetJsonSchemaHandler.resolve_ref_schema\(maybe_ref_json_schema\)

A JsonSchemaValue which may be a `$ref` schema.

##### Raises

#raises

  * `LookupError` — If the ref is not found.

## GetCoreSchemaHandler 

#pydantic.annotated_handlers.GetCoreSchemaHandler

Handler to call into the next CoreSchema schema generation function.

### Attributes

#attributes-1

#### field_name 

#pydantic.annotated_handlers.GetCoreSchemaHandler.field_name

Get the name of the closest field to this validator.

**Type:** [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`None`](https://docs.python.org/3/library/constants.html#None)

### Methods

#methods-1

#### generate_schema 

#pydantic.annotated_handlers.GetCoreSchemaHandler.generate_schema

```
 
    def generate_schema(source_type: Any) -> core_schema.CoreSchema
    

```

Generate a schema unrelated to the current context. Use this function if e.g. you are handling schema generation for a sequence and want to generate a schema for its items. Otherwise, you may end up doing something like applying a `min_length` constraint that was intended for the sequence itself to its items!

##### Returns

#returns-1

`core_schema.CoreSchema` — The `pydantic-core` CoreSchema generated.

##### Parameters

#parameters-1

**`source_type`** : [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)

#pydantic.annotated_handlers.GetCoreSchemaHandler.generate_schema\(source_type\)

The input type.

#### resolve_ref_schema 

#pydantic.annotated_handlers.GetCoreSchemaHandler.resolve_ref_schema

```
 
    def resolve_ref_schema(
        maybe_ref_schema: core_schema.CoreSchema,
    ) -> core_schema.CoreSchema
    

```

Get the real schema for a `definition-ref` schema. If the schema given is not a `definition-ref` schema, it will be returned as is. This means you don’t have to check before calling this function.

##### Returns

#returns-2

`core_schema.CoreSchema` — A concrete `CoreSchema`.

##### Parameters

#parameters-2

**`maybe_ref_schema`** : `core_schema.CoreSchema`

#pydantic.annotated_handlers.GetCoreSchemaHandler.resolve_ref_schema\(maybe_ref_schema\)

A `CoreSchema`, `ref`-based or not.

##### Raises

#raises-1

  * `LookupError` — If the `ref` is not found.
