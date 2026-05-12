---
title: JSON Schema
source: https://pydantic.dev/docs/validation/latest/api/pydantic/json_schema
---

Usage Documentation

[JSON Schema](https://pydantic.dev/docs/validation/latest/concepts/json_schema) ([local](./../../concepts/json-schema.md))

The `json_schema` module contains classes and functions to allow the way [JSON Schema](https://json-schema.org/) is generated to be customized.

In general you shouldn’t need to use this module directly; instead, you can use [`BaseModel.model_json_schema`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_json_schema) ([local](./base-model.md#pydantic.BaseModel.model_json_schema)) and [`TypeAdapter.json_schema`](https://pydantic.dev/docs/validation/latest/api/pydantic/type_adapter/#pydantic.type_adapter.TypeAdapter.json_schema) ([local](./type-adapter.md#pydantic.type_adapter.TypeAdapter.json_schema)).

## PydanticJsonSchemaWarning 

#pydantic.json_schema.PydanticJsonSchemaWarning

**Bases:** [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning)

This class is used to emit warnings produced during JSON schema generation. See the [`GenerateJsonSchema.emit_warning`](#pydantic.json_schema.GenerateJsonSchema.emit_warning) and [`GenerateJsonSchema.render_warning_message`](#pydantic.json_schema.GenerateJsonSchema.render_warning_message) methods for more details; these can be overridden to control warning behavior.

## GenerateJsonSchema 

#pydantic.json_schema.GenerateJsonSchema

Usage Documentation

[Customizing the JSON Schema Generation Process](https://pydantic.dev/docs/validation/latest/concepts/json_schema#customizing-the-json-schema-generation-process) ([local](./../../concepts/json-schema.md#customizing-the-json-schema-generation-process))

A class for generating JSON schemas.

This class generates JSON schemas based on configured parameters. The default schema dialect is <https://json-schema.org/draft/2020-12/schema>. The class uses `by_alias` to configure how fields with multiple names are handled and `ref_template` to format reference names.

### Attributes

#attributes

#### schema_dialect 

#pydantic.json_schema.GenerateJsonSchema.schema_dialect

The JSON schema dialect used to generate the schema. See [Declaring a Dialect](https://json-schema.org/understanding-json-schema/reference/schema.html#id4) in the JSON Schema documentation for more information about dialects.

#### ignored_warning_kinds 

#pydantic.json_schema.GenerateJsonSchema.ignored_warning_kinds

Warnings to ignore when generating the schema. `self.render_warning_message` will do nothing if its argument `kind` is in `ignored_warning_kinds`; this value can be modified on subclasses to easily control which warnings are emitted.

**Type:** [`set`](https://docs.python.org/3/reference/expressions.html#set)[`JsonSchemaWarningKind`]

#### by_alias 

#pydantic.json_schema.GenerateJsonSchema.by_alias

Whether to use field aliases when generating the schema.

#### ref_template 

#pydantic.json_schema.GenerateJsonSchema.ref_template

The format string used when generating reference names.

#### core_to_json_refs 

#pydantic.json_schema.GenerateJsonSchema.core_to_json_refs

A mapping of core refs to JSON refs.

**Type:** [`dict`](https://docs.python.org/3/reference/expressions.html#dict)[`CoreModeRef`, `JsonRef`]

#### core_to_defs_refs 

#pydantic.json_schema.GenerateJsonSchema.core_to_defs_refs

A mapping of core refs to definition refs.

**Type:** [`dict`](https://docs.python.org/3/reference/expressions.html#dict)[`CoreModeRef`, `DefsRef`]

#### defs_to_core_refs 

#pydantic.json_schema.GenerateJsonSchema.defs_to_core_refs

A mapping of definition refs to core refs.

**Type:** [`dict`](https://docs.python.org/3/reference/expressions.html#dict)[`DefsRef`, `CoreModeRef`]

#### json_to_defs_refs 

#pydantic.json_schema.GenerateJsonSchema.json_to_defs_refs

A mapping of JSON refs to definition refs.

**Type:** [`dict`](https://docs.python.org/3/reference/expressions.html#dict)[`JsonRef`, `DefsRef`]

#### definitions 

#pydantic.json_schema.GenerateJsonSchema.definitions

Definitions in the schema.

**Type:** [`dict`](https://docs.python.org/3/reference/expressions.html#dict)[`DefsRef`, `JsonSchemaValue`]

### Constructor Parameters

#constructor-parameters

**`by_alias`** : [`bool`](https://docs.python.org/3/library/functions.html#bool) _Default:_ `True`

#pydantic.json_schema.GenerateJsonSchema.__init__\(by_alias\)

Whether to use field aliases in the generated schemas.

**`ref_template`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str) _Default:_ `DEFAULT_REF_TEMPLATE`

#pydantic.json_schema.GenerateJsonSchema.__init__\(ref_template\)

The format string to use when generating reference names.

**`union_format`** : [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal)[‘any_of’, ‘primitive_type_array’] _Default:_ `'any_of'`

#pydantic.json_schema.GenerateJsonSchema.__init__\(union_format\)

The format to use when combining schemas from unions together. Can be one of:

  * `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf) keyword to combine schemas (the default).
  * `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type) keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

### Methods

#methods

#### build_schema_type_to_method 

#pydantic.json_schema.GenerateJsonSchema.build_schema_type_to_method

```
 
    def build_schema_type_to_method(
    
    ) -> dict[CoreSchemaOrFieldType, Callable[[CoreSchemaOrField], JsonSchemaValue]]
    

```

Builds a dictionary mapping fields to methods for generating JSON schemas.

##### Returns

#returns

[`dict`](https://docs.python.org/3/reference/expressions.html#dict)[`CoreSchemaOrFieldType`, [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`CoreSchemaOrField`], `JsonSchemaValue`]] — A dictionary containing the mapping of `CoreSchemaOrFieldType` to a handler method.

##### Raises

#raises

  * `TypeError` — If no method has been defined for generating a JSON schema for a given pydantic core schema type.

#### generate_definitions 

#pydantic.json_schema.GenerateJsonSchema.generate_definitions

```
 
    def generate_definitions(
        inputs: Sequence[tuple[JsonSchemaKeyT, JsonSchemaMode, core_schema.CoreSchema]],
    ) -> tuple[dict[tuple[JsonSchemaKeyT, JsonSchemaMode], JsonSchemaValue], dict[DefsRef, JsonSchemaValue]]
    

```

Generates JSON schema definitions from a list of core schemas, pairing the generated definitions with a mapping that links the input keys to the definition references.

##### Returns

#returns-1

[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[[`dict`](https://docs.python.org/3/reference/expressions.html#dict)[[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[`JsonSchemaKeyT`, `JsonSchemaMode`], `JsonSchemaValue`], [`dict`](https://docs.python.org/3/reference/expressions.html#dict)[`DefsRef`, `JsonSchemaValue`]] — A tuple where:

  * The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have JsonRef references to definitions that are defined in the second returned element.)
  * The second element is a dictionary whose keys are definition references for the JSON schemas from the first returned element, and whose values are the actual JSON schema definitions.

##### Parameters

#parameters

**`inputs`** : [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence)[[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[`JsonSchemaKeyT`, `JsonSchemaMode`, `core_schema.CoreSchema`]] 

#pydantic.json_schema.GenerateJsonSchema.generate_definitions\(inputs\)

A sequence of tuples, where:

  * The first element is a JSON schema key type.
  * The second element is the JSON mode: either ‘validation’ or ‘serialization’.
  * The third element is a core schema.

##### Raises

#raises-1

  * `PydanticUserError` — Raised if the JSON schema generator has already been used to generate a JSON schema.

#### generate 

#pydantic.json_schema.GenerateJsonSchema.generate

```
 
    def generate(schema: CoreSchema, mode: JsonSchemaMode = 'validation') -> JsonSchemaValue
    

```

Generates a JSON schema for a specified schema in a specified mode.

##### Returns

#returns-2

`JsonSchemaValue` — A JSON schema representing the specified schema.

##### Parameters

#parameters-1

**`schema`** : `CoreSchema`

#pydantic.json_schema.GenerateJsonSchema.generate\(schema\)

A Pydantic model.

**`mode`** : `JsonSchemaMode` _Default:_ `'validation'`

#pydantic.json_schema.GenerateJsonSchema.generate\(mode\)

The mode in which to generate the schema. Defaults to ‘validation’.

##### Raises

#raises-2

  * `PydanticUserError` — If the JSON schema generator has already been used to generate a JSON schema.

#### generate_inner 

#pydantic.json_schema.GenerateJsonSchema.generate_inner

```
 
    def generate_inner(schema: CoreSchemaOrField) -> JsonSchemaValue
    

```

Generates a JSON schema for a given core schema.

TODO: the nested function definitions here seem like bad practice, I’d like to unpack these in a future PR. It’d be great if we could shorten the call stack a bit for JSON schema generation, and I think there’s potential for that here.

##### Returns

#returns-3

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-2

**`schema`** : `CoreSchemaOrField`

#pydantic.json_schema.GenerateJsonSchema.generate_inner\(schema\)

The given core schema.

#### sort 

#pydantic.json_schema.GenerateJsonSchema.sort

```
 
    def sort(value: JsonSchemaValue, parent_key: str | None = None) -> JsonSchemaValue
    

```

Override this method to customize the sorting of the JSON schema (e.g., don’t sort at all, sort all keys unconditionally, etc.)

By default, alphabetically sort the keys in the JSON schema, skipping the ‘properties’ and ‘default’ keys to preserve field definition order. This sort is recursive, so it will sort all nested dictionaries as well.

##### Returns

#returns-4

`JsonSchemaValue`

#### invalid_schema 

#pydantic.json_schema.GenerateJsonSchema.invalid_schema

```
 
    def invalid_schema(schema: core_schema.InvalidSchema) -> JsonSchemaValue
    

```

Placeholder - should never be called.

##### Returns

#returns-5

`JsonSchemaValue`

#### any_schema 

#pydantic.json_schema.GenerateJsonSchema.any_schema

```
 
    def any_schema(schema: core_schema.AnySchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches any value.

##### Returns

#returns-6

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-3

**`schema`** : `core_schema.AnySchema`

#pydantic.json_schema.GenerateJsonSchema.any_schema\(schema\)

The core schema.

#### none_schema 

#pydantic.json_schema.GenerateJsonSchema.none_schema

```
 
    def none_schema(schema: core_schema.NoneSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches `None`.

##### Returns

#returns-7

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-4

**`schema`** : `core_schema.NoneSchema`

#pydantic.json_schema.GenerateJsonSchema.none_schema\(schema\)

The core schema.

#### bool_schema 

#pydantic.json_schema.GenerateJsonSchema.bool_schema

```
 
    def bool_schema(schema: core_schema.BoolSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a bool value.

##### Returns

#returns-8

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-5

**`schema`** : `core_schema.BoolSchema`

#pydantic.json_schema.GenerateJsonSchema.bool_schema\(schema\)

The core schema.

#### int_schema 

#pydantic.json_schema.GenerateJsonSchema.int_schema

```
 
    def int_schema(schema: core_schema.IntSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches an int value.

##### Returns

#returns-9

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-6

**`schema`** : `core_schema.IntSchema`

#pydantic.json_schema.GenerateJsonSchema.int_schema\(schema\)

The core schema.

#### float_schema 

#pydantic.json_schema.GenerateJsonSchema.float_schema

```
 
    def float_schema(schema: core_schema.FloatSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a float value.

##### Returns

#returns-10

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-7

**`schema`** : `core_schema.FloatSchema`

#pydantic.json_schema.GenerateJsonSchema.float_schema\(schema\)

The core schema.

#### decimal_schema 

#pydantic.json_schema.GenerateJsonSchema.decimal_schema

```
 
    def decimal_schema(schema: core_schema.DecimalSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a decimal value.

##### Returns

#returns-11

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-8

**`schema`** : `core_schema.DecimalSchema`

#pydantic.json_schema.GenerateJsonSchema.decimal_schema\(schema\)

The core schema.

#### str_schema 

#pydantic.json_schema.GenerateJsonSchema.str_schema

```
 
    def str_schema(schema: core_schema.StringSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a string value.

##### Returns

#returns-12

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-9

**`schema`** : `core_schema.StringSchema`

#pydantic.json_schema.GenerateJsonSchema.str_schema\(schema\)

The core schema.

#### bytes_schema 

#pydantic.json_schema.GenerateJsonSchema.bytes_schema

```
 
    def bytes_schema(schema: core_schema.BytesSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a bytes value.

##### Returns

#returns-13

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-10

**`schema`** : `core_schema.BytesSchema`

#pydantic.json_schema.GenerateJsonSchema.bytes_schema\(schema\)

The core schema.

#### date_schema 

#pydantic.json_schema.GenerateJsonSchema.date_schema

```
 
    def date_schema(schema: core_schema.DateSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a date value.

##### Returns

#returns-14

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-11

**`schema`** : `core_schema.DateSchema`

#pydantic.json_schema.GenerateJsonSchema.date_schema\(schema\)

The core schema.

#### time_schema 

#pydantic.json_schema.GenerateJsonSchema.time_schema

```
 
    def time_schema(schema: core_schema.TimeSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a time value.

##### Returns

#returns-15

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-12

**`schema`** : `core_schema.TimeSchema`

#pydantic.json_schema.GenerateJsonSchema.time_schema\(schema\)

The core schema.

#### datetime_schema 

#pydantic.json_schema.GenerateJsonSchema.datetime_schema

```
 
    def datetime_schema(schema: core_schema.DatetimeSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a datetime value.

##### Returns

#returns-16

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-13

**`schema`** : `core_schema.DatetimeSchema`

#pydantic.json_schema.GenerateJsonSchema.datetime_schema\(schema\)

The core schema.

#### timedelta_schema 

#pydantic.json_schema.GenerateJsonSchema.timedelta_schema

```
 
    def timedelta_schema(schema: core_schema.TimedeltaSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a timedelta value.

##### Returns

#returns-17

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-14

**`schema`** : `core_schema.TimedeltaSchema`

#pydantic.json_schema.GenerateJsonSchema.timedelta_schema\(schema\)

The core schema.

#### literal_schema 

#pydantic.json_schema.GenerateJsonSchema.literal_schema

```
 
    def literal_schema(schema: core_schema.LiteralSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a literal value.

##### Returns

#returns-18

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-15

**`schema`** : `core_schema.LiteralSchema`

#pydantic.json_schema.GenerateJsonSchema.literal_schema\(schema\)

The core schema.

#### missing_sentinel_schema 

#pydantic.json_schema.GenerateJsonSchema.missing_sentinel_schema

```
 
    def missing_sentinel_schema(
        schema: core_schema.MissingSentinelSchema,
    ) -> JsonSchemaValue
    

```

Generates a JSON schema that matches the `MISSING` sentinel value.

##### Returns

#returns-19

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-16

**`schema`** : `core_schema.MissingSentinelSchema`

#pydantic.json_schema.GenerateJsonSchema.missing_sentinel_schema\(schema\)

The core schema.

#### enum_schema 

#pydantic.json_schema.GenerateJsonSchema.enum_schema

```
 
    def enum_schema(schema: core_schema.EnumSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches an Enum value.

##### Returns

#returns-20

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-17

**`schema`** : `core_schema.EnumSchema`

#pydantic.json_schema.GenerateJsonSchema.enum_schema\(schema\)

The core schema.

#### is_instance_schema 

#pydantic.json_schema.GenerateJsonSchema.is_instance_schema

```
 
    def is_instance_schema(schema: core_schema.IsInstanceSchema) -> JsonSchemaValue
    

```

Handles JSON schema generation for a core schema that checks if a value is an instance of a class.

Unless overridden in a subclass, this raises an error.

##### Returns

#returns-21

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-18

**`schema`** : `core_schema.IsInstanceSchema`

#pydantic.json_schema.GenerateJsonSchema.is_instance_schema\(schema\)

The core schema.

#### is_subclass_schema 

#pydantic.json_schema.GenerateJsonSchema.is_subclass_schema

```
 
    def is_subclass_schema(schema: core_schema.IsSubclassSchema) -> JsonSchemaValue
    

```

Handles JSON schema generation for a core schema that checks if a value is a subclass of a class.

For backwards compatibility with v1, this does not raise an error, but can be overridden to change this.

##### Returns

#returns-22

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-19

**`schema`** : `core_schema.IsSubclassSchema`

#pydantic.json_schema.GenerateJsonSchema.is_subclass_schema\(schema\)

The core schema.

#### callable_schema 

#pydantic.json_schema.GenerateJsonSchema.callable_schema

```
 
    def callable_schema(schema: core_schema.CallableSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a callable value.

Unless overridden in a subclass, this raises an error.

##### Returns

#returns-23

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-20

**`schema`** : `core_schema.CallableSchema`

#pydantic.json_schema.GenerateJsonSchema.callable_schema\(schema\)

The core schema.

#### list_schema 

#pydantic.json_schema.GenerateJsonSchema.list_schema

```
 
    def list_schema(schema: core_schema.ListSchema) -> JsonSchemaValue
    

```

Returns a schema that matches a list schema.

##### Returns

#returns-24

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-21

**`schema`** : `core_schema.ListSchema`

#pydantic.json_schema.GenerateJsonSchema.list_schema\(schema\)

The core schema.

#### tuple_positional_schema 

#pydantic.json_schema.GenerateJsonSchema.tuple_positional_schema

```
 
    def tuple_positional_schema(schema: core_schema.TupleSchema) -> JsonSchemaValue
    

```

Replaced by `tuple_schema`.

##### Returns

#returns-25

`JsonSchemaValue`

#### tuple_variable_schema 

#pydantic.json_schema.GenerateJsonSchema.tuple_variable_schema

```
 
    def tuple_variable_schema(schema: core_schema.TupleSchema) -> JsonSchemaValue
    

```

Replaced by `tuple_schema`.

##### Returns

#returns-26

`JsonSchemaValue`

#### tuple_schema 

#pydantic.json_schema.GenerateJsonSchema.tuple_schema

```
 
    def tuple_schema(schema: core_schema.TupleSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a tuple schema e.g. `tuple[int, str, bool]` or `tuple[int, ...]`.

##### Returns

#returns-27

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-22

**`schema`** : `core_schema.TupleSchema`

#pydantic.json_schema.GenerateJsonSchema.tuple_schema\(schema\)

The core schema.

#### set_schema 

#pydantic.json_schema.GenerateJsonSchema.set_schema

```
 
    def set_schema(schema: core_schema.SetSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a set schema.

##### Returns

#returns-28

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-23

**`schema`** : `core_schema.SetSchema`

#pydantic.json_schema.GenerateJsonSchema.set_schema\(schema\)

The core schema.

#### frozenset_schema 

#pydantic.json_schema.GenerateJsonSchema.frozenset_schema

```
 
    def frozenset_schema(schema: core_schema.FrozenSetSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a frozenset schema.

##### Returns

#returns-29

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-24

**`schema`** : `core_schema.FrozenSetSchema`

#pydantic.json_schema.GenerateJsonSchema.frozenset_schema\(schema\)

The core schema.

#### generator_schema 

#pydantic.json_schema.GenerateJsonSchema.generator_schema

```
 
    def generator_schema(schema: core_schema.GeneratorSchema) -> JsonSchemaValue
    

```

Returns a JSON schema that represents the provided GeneratorSchema.

##### Returns

#returns-30

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-25

**`schema`** : `core_schema.GeneratorSchema`

#pydantic.json_schema.GenerateJsonSchema.generator_schema\(schema\)

The schema.

#### dict_schema 

#pydantic.json_schema.GenerateJsonSchema.dict_schema

```
 
    def dict_schema(schema: core_schema.DictSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a dict schema.

##### Returns

#returns-31

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-26

**`schema`** : `core_schema.DictSchema`

#pydantic.json_schema.GenerateJsonSchema.dict_schema\(schema\)

The core schema.

#### function_before_schema 

#pydantic.json_schema.GenerateJsonSchema.function_before_schema

```
 
    def function_before_schema(
        schema: core_schema.BeforeValidatorFunctionSchema,
    ) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a function-before schema.

##### Returns

#returns-32

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-27

**`schema`** : `core_schema.BeforeValidatorFunctionSchema`

#pydantic.json_schema.GenerateJsonSchema.function_before_schema\(schema\)

The core schema.

#### function_after_schema 

#pydantic.json_schema.GenerateJsonSchema.function_after_schema

```
 
    def function_after_schema(
        schema: core_schema.AfterValidatorFunctionSchema,
    ) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a function-after schema.

##### Returns

#returns-33

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-28

**`schema`** : `core_schema.AfterValidatorFunctionSchema`

#pydantic.json_schema.GenerateJsonSchema.function_after_schema\(schema\)

The core schema.

#### function_plain_schema 

#pydantic.json_schema.GenerateJsonSchema.function_plain_schema

```
 
    def function_plain_schema(
        schema: core_schema.PlainValidatorFunctionSchema,
    ) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a function-plain schema.

##### Returns

#returns-34

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-29

**`schema`** : `core_schema.PlainValidatorFunctionSchema`

#pydantic.json_schema.GenerateJsonSchema.function_plain_schema\(schema\)

The core schema.

#### function_wrap_schema 

#pydantic.json_schema.GenerateJsonSchema.function_wrap_schema

```
 
    def function_wrap_schema(
        schema: core_schema.WrapValidatorFunctionSchema,
    ) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a function-wrap schema.

##### Returns

#returns-35

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-30

**`schema`** : `core_schema.WrapValidatorFunctionSchema`

#pydantic.json_schema.GenerateJsonSchema.function_wrap_schema\(schema\)

The core schema.

#### default_schema 

#pydantic.json_schema.GenerateJsonSchema.default_schema

```
 
    def default_schema(schema: core_schema.WithDefaultSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema with a default value.

##### Returns

#returns-36

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-31

**`schema`** : `core_schema.WithDefaultSchema`

#pydantic.json_schema.GenerateJsonSchema.default_schema\(schema\)

The core schema.

#### get_default_value 

#pydantic.json_schema.GenerateJsonSchema.get_default_value

```
 
    def get_default_value(schema: core_schema.WithDefaultSchema) -> Any
    

```

Get the default value to be used when generating a JSON Schema for a core schema with a default.

The default implementation is to use the statically defined default value. This method can be overridden if you want to make use of the default factory.

##### Returns

#returns-37

[`Any`](https://docs.python.org/3/library/typing.html#typing.Any) — The default value to use, or [`NoDefault`](#pydantic.json_schema.NoDefault) if no default value is available.

##### Parameters

#parameters-32

**`schema`** : `core_schema.WithDefaultSchema`

#pydantic.json_schema.GenerateJsonSchema.get_default_value\(schema\)

The `'with-default'` core schema.

#### nullable_schema 

#pydantic.json_schema.GenerateJsonSchema.nullable_schema

```
 
    def nullable_schema(schema: core_schema.NullableSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that allows null values.

##### Returns

#returns-38

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-33

**`schema`** : `core_schema.NullableSchema`

#pydantic.json_schema.GenerateJsonSchema.nullable_schema\(schema\)

The core schema.

#### union_schema 

#pydantic.json_schema.GenerateJsonSchema.union_schema

```
 
    def union_schema(schema: core_schema.UnionSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that allows values matching any of the given schemas.

##### Returns

#returns-39

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-34

**`schema`** : `core_schema.UnionSchema`

#pydantic.json_schema.GenerateJsonSchema.union_schema\(schema\)

The core schema.

#### get_union_of_schemas 

#pydantic.json_schema.GenerateJsonSchema.get_union_of_schemas

```
 
    def get_union_of_schemas(schemas: list[JsonSchemaValue]) -> JsonSchemaValue
    

```

Returns the JSON Schema representation for the union of the provided JSON Schemas.

The result depends on the configured `'union_format'`.

##### Returns

#returns-40

`JsonSchemaValue` — The JSON Schema representing the union of schemas.

##### Parameters

#parameters-35

**`schemas`** : [`list`](https://docs.python.org/3/glossary.html#term-list)[`JsonSchemaValue`] 

#pydantic.json_schema.GenerateJsonSchema.get_union_of_schemas\(schemas\)

The list of JSON Schemas to be included in the union.

#### tagged_union_schema 

#pydantic.json_schema.GenerateJsonSchema.tagged_union_schema

```
 
    def tagged_union_schema(schema: core_schema.TaggedUnionSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that allows values matching any of the given schemas, where the schemas are tagged with a discriminator field that indicates which schema should be used to validate the value.

##### Returns

#returns-41

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-36

**`schema`** : `core_schema.TaggedUnionSchema`

#pydantic.json_schema.GenerateJsonSchema.tagged_union_schema\(schema\)

The core schema.

#### chain_schema 

#pydantic.json_schema.GenerateJsonSchema.chain_schema

```
 
    def chain_schema(schema: core_schema.ChainSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a core_schema.ChainSchema.

When generating a schema for validation, we return the validation JSON schema for the first step in the chain. For serialization, we return the serialization JSON schema for the last step in the chain.

##### Returns

#returns-42

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-37

**`schema`** : `core_schema.ChainSchema`

#pydantic.json_schema.GenerateJsonSchema.chain_schema\(schema\)

The core schema.

#### lax_or_strict_schema 

#pydantic.json_schema.GenerateJsonSchema.lax_or_strict_schema

```
 
    def lax_or_strict_schema(schema: core_schema.LaxOrStrictSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that allows values matching either the lax schema or the strict schema.

##### Returns

#returns-43

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-38

**`schema`** : `core_schema.LaxOrStrictSchema`

#pydantic.json_schema.GenerateJsonSchema.lax_or_strict_schema\(schema\)

The core schema.

#### json_or_python_schema 

#pydantic.json_schema.GenerateJsonSchema.json_or_python_schema

```
 
    def json_or_python_schema(schema: core_schema.JsonOrPythonSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that allows values matching either the JSON schema or the Python schema.

The JSON schema is used instead of the Python schema. If you want to use the Python schema, you should override this method.

##### Returns

#returns-44

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-39

**`schema`** : `core_schema.JsonOrPythonSchema`

#pydantic.json_schema.GenerateJsonSchema.json_or_python_schema\(schema\)

The core schema.

#### typed_dict_schema 

#pydantic.json_schema.GenerateJsonSchema.typed_dict_schema

```
 
    def typed_dict_schema(schema: core_schema.TypedDictSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a typed dict.

##### Returns

#returns-45

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-40

**`schema`** : `core_schema.TypedDictSchema`

#pydantic.json_schema.GenerateJsonSchema.typed_dict_schema\(schema\)

The core schema.

#### typed_dict_field_schema 

#pydantic.json_schema.GenerateJsonSchema.typed_dict_field_schema

```
 
    def typed_dict_field_schema(schema: core_schema.TypedDictField) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a typed dict field.

##### Returns

#returns-46

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-41

**`schema`** : `core_schema.TypedDictField`

#pydantic.json_schema.GenerateJsonSchema.typed_dict_field_schema\(schema\)

The core schema.

#### dataclass_field_schema 

#pydantic.json_schema.GenerateJsonSchema.dataclass_field_schema

```
 
    def dataclass_field_schema(schema: core_schema.DataclassField) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a dataclass field.

##### Returns

#returns-47

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-42

**`schema`** : `core_schema.DataclassField`

#pydantic.json_schema.GenerateJsonSchema.dataclass_field_schema\(schema\)

The core schema.

#### model_field_schema 

#pydantic.json_schema.GenerateJsonSchema.model_field_schema

```
 
    def model_field_schema(schema: core_schema.ModelField) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a model field.

##### Returns

#returns-48

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-43

**`schema`** : `core_schema.ModelField`

#pydantic.json_schema.GenerateJsonSchema.model_field_schema\(schema\)

The core schema.

#### computed_field_schema 

#pydantic.json_schema.GenerateJsonSchema.computed_field_schema

```
 
    def computed_field_schema(schema: core_schema.ComputedField) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a computed field.

##### Returns

#returns-49

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-44

**`schema`** : `core_schema.ComputedField`

#pydantic.json_schema.GenerateJsonSchema.computed_field_schema\(schema\)

The core schema.

#### model_schema 

#pydantic.json_schema.GenerateJsonSchema.model_schema

```
 
    def model_schema(schema: core_schema.ModelSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a model.

##### Returns

#returns-50

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-45

**`schema`** : `core_schema.ModelSchema`

#pydantic.json_schema.GenerateJsonSchema.model_schema\(schema\)

The core schema.

#### resolve_ref_schema 

#pydantic.json_schema.GenerateJsonSchema.resolve_ref_schema

```
 
    def resolve_ref_schema(json_schema: JsonSchemaValue) -> JsonSchemaValue
    

```

Resolve a JsonSchemaValue to the non-ref schema if it is a $ref schema.

##### Returns

#returns-51

`JsonSchemaValue` — The resolved schema.

##### Parameters

#parameters-46

**`json_schema`** : `JsonSchemaValue`

#pydantic.json_schema.GenerateJsonSchema.resolve_ref_schema\(json_schema\)

The schema to resolve.

##### Raises

#raises-3

  * `RuntimeError` — If the schema reference can’t be found in definitions.

#### model_fields_schema 

#pydantic.json_schema.GenerateJsonSchema.model_fields_schema

```
 
    def model_fields_schema(schema: core_schema.ModelFieldsSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a model’s fields.

##### Returns

#returns-52

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-47

**`schema`** : `core_schema.ModelFieldsSchema`

#pydantic.json_schema.GenerateJsonSchema.model_fields_schema\(schema\)

The core schema.

#### field_is_present 

#pydantic.json_schema.GenerateJsonSchema.field_is_present

```
 
    def field_is_present(field: CoreSchemaField) -> bool
    

```

Whether the field should be included in the generated JSON schema.

##### Returns

#returns-53

[`bool`](https://docs.python.org/3/library/functions.html#bool) — `True` if the field should be included in the generated JSON schema, `False` otherwise.

##### Parameters

#parameters-48

**`field`** : `CoreSchemaField`

#pydantic.json_schema.GenerateJsonSchema.field_is_present\(field\)

The schema for the field itself.

#### field_is_required 

#pydantic.json_schema.GenerateJsonSchema.field_is_required

```
 
    def field_is_required(
        field: core_schema.ModelField | core_schema.DataclassField | core_schema.TypedDictField,
        total: bool,
    ) -> bool
    

```

Whether the field should be marked as required in the generated JSON schema. (Note that this is irrelevant if the field is not present in the JSON schema.).

##### Returns

#returns-54

[`bool`](https://docs.python.org/3/library/functions.html#bool) — `True` if the field should be marked as required in the generated JSON schema, `False` otherwise.

##### Parameters

#parameters-49

**`field`** : `core_schema.ModelField` | `core_schema.DataclassField` | `core_schema.TypedDictField`

#pydantic.json_schema.GenerateJsonSchema.field_is_required\(field\)

The schema for the field itself.

**`total`** : [`bool`](https://docs.python.org/3/library/functions.html#bool)

#pydantic.json_schema.GenerateJsonSchema.field_is_required\(total\)

Only applies to `TypedDictField`s. Indicates if the `TypedDict` this field belongs to is total, in which case any fields that don’t explicitly specify `required=False` are required.

#### dataclass_args_schema 

#pydantic.json_schema.GenerateJsonSchema.dataclass_args_schema

```
 
    def dataclass_args_schema(schema: core_schema.DataclassArgsSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a dataclass’s constructor arguments.

##### Returns

#returns-55

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-50

**`schema`** : `core_schema.DataclassArgsSchema`

#pydantic.json_schema.GenerateJsonSchema.dataclass_args_schema\(schema\)

The core schema.

#### dataclass_schema 

#pydantic.json_schema.GenerateJsonSchema.dataclass_schema

```
 
    def dataclass_schema(schema: core_schema.DataclassSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a dataclass.

##### Returns

#returns-56

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-51

**`schema`** : `core_schema.DataclassSchema`

#pydantic.json_schema.GenerateJsonSchema.dataclass_schema\(schema\)

The core schema.

#### arguments_schema 

#pydantic.json_schema.GenerateJsonSchema.arguments_schema

```
 
    def arguments_schema(schema: core_schema.ArgumentsSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a function’s arguments.

##### Returns

#returns-57

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-52

**`schema`** : `core_schema.ArgumentsSchema`

#pydantic.json_schema.GenerateJsonSchema.arguments_schema\(schema\)

The core schema.

#### kw_arguments_schema 

#pydantic.json_schema.GenerateJsonSchema.kw_arguments_schema

```
 
    def kw_arguments_schema(
        arguments: list[core_schema.ArgumentsParameter],
        var_kwargs_schema: CoreSchema | None,
    ) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a function’s keyword arguments.

##### Returns

#returns-58

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-53

**`arguments`** : [`list`](https://docs.python.org/3/glossary.html#term-list)[`core_schema.ArgumentsParameter`] 

#pydantic.json_schema.GenerateJsonSchema.kw_arguments_schema\(arguments\)

The core schema.

#### p_arguments_schema 

#pydantic.json_schema.GenerateJsonSchema.p_arguments_schema

```
 
    def p_arguments_schema(
        arguments: list[core_schema.ArgumentsParameter],
        var_args_schema: CoreSchema | None,
    ) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a function’s positional arguments.

##### Returns

#returns-59

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-54

**`arguments`** : [`list`](https://docs.python.org/3/glossary.html#term-list)[`core_schema.ArgumentsParameter`] 

#pydantic.json_schema.GenerateJsonSchema.p_arguments_schema\(arguments\)

The core schema.

#### get_argument_name 

#pydantic.json_schema.GenerateJsonSchema.get_argument_name

```
 
    def get_argument_name(
        argument: core_schema.ArgumentsParameter | core_schema.ArgumentsV3Parameter,
    ) -> str
    

```

Retrieves the name of an argument.

##### Returns

#returns-60

[`str`](https://docs.python.org/3/library/stdtypes.html#str) — The name of the argument.

##### Parameters

#parameters-55

**`argument`** : `core_schema.ArgumentsParameter` | `core_schema.ArgumentsV3Parameter`

#pydantic.json_schema.GenerateJsonSchema.get_argument_name\(argument\)

The core schema.

#### arguments_v3_schema 

#pydantic.json_schema.GenerateJsonSchema.arguments_v3_schema

```
 
    def arguments_v3_schema(schema: core_schema.ArgumentsV3Schema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a function’s arguments.

##### Returns

#returns-61

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-56

**`schema`** : `core_schema.ArgumentsV3Schema`

#pydantic.json_schema.GenerateJsonSchema.arguments_v3_schema\(schema\)

The core schema.

#### call_schema 

#pydantic.json_schema.GenerateJsonSchema.call_schema

```
 
    def call_schema(schema: core_schema.CallSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a function call.

##### Returns

#returns-62

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-57

**`schema`** : `core_schema.CallSchema`

#pydantic.json_schema.GenerateJsonSchema.call_schema\(schema\)

The core schema.

#### custom_error_schema 

#pydantic.json_schema.GenerateJsonSchema.custom_error_schema

```
 
    def custom_error_schema(schema: core_schema.CustomErrorSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a custom error.

##### Returns

#returns-63

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-58

**`schema`** : `core_schema.CustomErrorSchema`

#pydantic.json_schema.GenerateJsonSchema.custom_error_schema\(schema\)

The core schema.

#### json_schema 

#pydantic.json_schema.GenerateJsonSchema.json_schema

```
 
    def json_schema(schema: core_schema.JsonSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a JSON object.

##### Returns

#returns-64

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-59

**`schema`** : `core_schema.JsonSchema`

#pydantic.json_schema.GenerateJsonSchema.json_schema\(schema\)

The core schema.

#### url_schema 

#pydantic.json_schema.GenerateJsonSchema.url_schema

```
 
    def url_schema(schema: core_schema.UrlSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a URL.

##### Returns

#returns-65

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-60

**`schema`** : `core_schema.UrlSchema`

#pydantic.json_schema.GenerateJsonSchema.url_schema\(schema\)

The core schema.

#### multi_host_url_schema 

#pydantic.json_schema.GenerateJsonSchema.multi_host_url_schema

```
 
    def multi_host_url_schema(schema: core_schema.MultiHostUrlSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a URL that can be used with multiple hosts.

##### Returns

#returns-66

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-61

**`schema`** : `core_schema.MultiHostUrlSchema`

#pydantic.json_schema.GenerateJsonSchema.multi_host_url_schema\(schema\)

The core schema.

#### uuid_schema 

#pydantic.json_schema.GenerateJsonSchema.uuid_schema

```
 
    def uuid_schema(schema: core_schema.UuidSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a UUID.

##### Returns

#returns-67

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-62

**`schema`** : `core_schema.UuidSchema`

#pydantic.json_schema.GenerateJsonSchema.uuid_schema\(schema\)

The core schema.

#### definitions_schema 

#pydantic.json_schema.GenerateJsonSchema.definitions_schema

```
 
    def definitions_schema(schema: core_schema.DefinitionsSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that defines a JSON object with definitions.

##### Returns

#returns-68

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-63

**`schema`** : `core_schema.DefinitionsSchema`

#pydantic.json_schema.GenerateJsonSchema.definitions_schema\(schema\)

The core schema.

#### definition_ref_schema 

#pydantic.json_schema.GenerateJsonSchema.definition_ref_schema

```
 
    def definition_ref_schema(
        schema: core_schema.DefinitionReferenceSchema,
    ) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a schema that references a definition.

##### Returns

#returns-69

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-64

**`schema`** : `core_schema.DefinitionReferenceSchema`

#pydantic.json_schema.GenerateJsonSchema.definition_ref_schema\(schema\)

The core schema.

#### ser_schema 

#pydantic.json_schema.GenerateJsonSchema.ser_schema

```
 
    def ser_schema(
        schema: core_schema.SerSchema | core_schema.IncExSeqSerSchema | core_schema.IncExDictSerSchema,
    ) -> JsonSchemaValue | None
    

```

Generates a JSON schema that matches a schema that defines a serialized object.

##### Returns

#returns-70

`JsonSchemaValue` | [`None`](https://docs.python.org/3/library/constants.html#None) — The generated JSON schema.

##### Parameters

#parameters-65

**`schema`** : `core_schema.SerSchema` | `core_schema.IncExSeqSerSchema` | `core_schema.IncExDictSerSchema`

#pydantic.json_schema.GenerateJsonSchema.ser_schema\(schema\)

The core schema.

#### complex_schema 

#pydantic.json_schema.GenerateJsonSchema.complex_schema

```
 
    def complex_schema(schema: core_schema.ComplexSchema) -> JsonSchemaValue
    

```

Generates a JSON schema that matches a complex number.

JSON has no standard way to represent complex numbers. Complex number is not a numeric type. Here we represent complex number as strings following the rule defined by Python. For instance, ‘1+2j’ is an accepted complex string. Details can be found in [Python’s `complex` documentation](https://docs.python.org/3/library/functions.html#complex).

##### Returns

#returns-71

`JsonSchemaValue` — The generated JSON schema.

##### Parameters

#parameters-66

**`schema`** : `core_schema.ComplexSchema`

#pydantic.json_schema.GenerateJsonSchema.complex_schema\(schema\)

The core schema.

#### get_title_from_name 

#pydantic.json_schema.GenerateJsonSchema.get_title_from_name

```
 
    def get_title_from_name(name: str) -> str
    

```

Retrieves a title from a name.

##### Returns

#returns-72

[`str`](https://docs.python.org/3/library/stdtypes.html#str) — The title.

##### Parameters

#parameters-67

**`name`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

#pydantic.json_schema.GenerateJsonSchema.get_title_from_name\(name\)

The name to retrieve a title from.

#### field_title_should_be_set 

#pydantic.json_schema.GenerateJsonSchema.field_title_should_be_set

```
 
    def field_title_should_be_set(schema: CoreSchemaOrField) -> bool
    

```

Returns true if a field with the given schema should have a title set based on the field name.

Intuitively, we want this to return true for schemas that wouldn’t otherwise provide their own title (e.g., int, float, str), and false for those that would (e.g., BaseModel subclasses).

##### Returns

#returns-73

[`bool`](https://docs.python.org/3/library/functions.html#bool) — `True` if the field should have a title set, `False` otherwise.

##### Parameters

#parameters-68

**`schema`** : `CoreSchemaOrField`

#pydantic.json_schema.GenerateJsonSchema.field_title_should_be_set\(schema\)

The schema to check.

#### normalize_name 

#pydantic.json_schema.GenerateJsonSchema.normalize_name

```
 
    def normalize_name(name: str) -> str
    

```

Normalizes a name to be used as a key in a dictionary.

##### Returns

#returns-74

[`str`](https://docs.python.org/3/library/stdtypes.html#str) — The normalized name.

##### Parameters

#parameters-69

**`name`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

#pydantic.json_schema.GenerateJsonSchema.normalize_name\(name\)

The name to normalize.

#### get_defs_ref 

#pydantic.json_schema.GenerateJsonSchema.get_defs_ref

```
 
    def get_defs_ref(core_mode_ref: CoreModeRef) -> DefsRef
    

```

Override this method to change the way that definitions keys are generated from a core reference.

##### Returns

#returns-75

`DefsRef` — The definitions key.

##### Parameters

#parameters-70

**`core_mode_ref`** : `CoreModeRef`

#pydantic.json_schema.GenerateJsonSchema.get_defs_ref\(core_mode_ref\)

The core reference.

#### get_cache_defs_ref_schema 

#pydantic.json_schema.GenerateJsonSchema.get_cache_defs_ref_schema

```
 
    def get_cache_defs_ref_schema(core_ref: CoreRef) -> tuple[DefsRef, JsonSchemaValue]
    

```

This method wraps the get_defs_ref method with some cache-lookup/population logic, and returns both the produced defs_ref and the JSON schema that will refer to the right definition.

##### Returns

#returns-76

[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[`DefsRef`, `JsonSchemaValue`] — A tuple of the definitions reference and the JSON schema that will refer to it.

##### Parameters

#parameters-71

**`core_ref`** : `CoreRef`

#pydantic.json_schema.GenerateJsonSchema.get_cache_defs_ref_schema\(core_ref\)

The core reference to get the definitions reference for.

#### handle_ref_overrides 

#pydantic.json_schema.GenerateJsonSchema.handle_ref_overrides

```
 
    def handle_ref_overrides(json_schema: JsonSchemaValue) -> JsonSchemaValue
    

```

Remove any sibling keys that are redundant with the referenced schema.

##### Returns

#returns-77

`JsonSchemaValue` — The schema with redundant sibling keys removed.

##### Parameters

#parameters-72

**`json_schema`** : `JsonSchemaValue`

#pydantic.json_schema.GenerateJsonSchema.handle_ref_overrides\(json_schema\)

The schema to remove redundant sibling keys from.

#### encode_default 

#pydantic.json_schema.GenerateJsonSchema.encode_default

```
 
    def encode_default(dft: Any) -> Any
    

```

Encode a default value to a JSON-serializable value.

This is used to encode default values for fields in the generated JSON schema.

##### Returns

#returns-78

[`Any`](https://docs.python.org/3/library/typing.html#typing.Any) — The encoded default value.

##### Parameters

#parameters-73

**`dft`** : [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)

#pydantic.json_schema.GenerateJsonSchema.encode_default\(dft\)

The default value to encode.

#### update_with_validations 

#pydantic.json_schema.GenerateJsonSchema.update_with_validations

```
 
    def update_with_validations(
        json_schema: JsonSchemaValue,
        core_schema: CoreSchema,
        mapping: dict[str, str],
    ) -> None
    

```

Update the json_schema with the corresponding validations specified in the core_schema, using the provided mapping to translate keys in core_schema to the appropriate keys for a JSON schema.

##### Returns

#returns-79

[`None`](https://docs.python.org/3/library/constants.html#None)

##### Parameters

#parameters-74

**`json_schema`** : `JsonSchemaValue`

#pydantic.json_schema.GenerateJsonSchema.update_with_validations\(json_schema\)

The JSON schema to update.

**`core_schema`** : `CoreSchema`

#pydantic.json_schema.GenerateJsonSchema.update_with_validations\(core_schema\)

The core schema to get the validations from.

**`mapping`** : [`dict`](https://docs.python.org/3/reference/expressions.html#dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`str`](https://docs.python.org/3/library/stdtypes.html#str)] 

#pydantic.json_schema.GenerateJsonSchema.update_with_validations\(mapping\)

A mapping from core_schema attribute names to the corresponding JSON schema attribute names.

#### get_json_ref_counts 

#pydantic.json_schema.GenerateJsonSchema.get_json_ref_counts

```
 
    def get_json_ref_counts(json_schema: JsonSchemaValue) -> dict[JsonRef, int]
    

```

Get all values corresponding to the key ‘$ref’ anywhere in the json_schema.

##### Returns

#returns-80

[`dict`](https://docs.python.org/3/reference/expressions.html#dict)[`JsonRef`, [`int`](https://docs.python.org/3/library/functions.html#int)]

#### emit_warning 

#pydantic.json_schema.GenerateJsonSchema.emit_warning

```
 
    def emit_warning(kind: JsonSchemaWarningKind, detail: str) -> None
    

```

This method simply emits PydanticJsonSchemaWarnings based on handling in the `warning_message` method.

##### Returns

#returns-81

[`None`](https://docs.python.org/3/library/constants.html#None)

#### render_warning_message 

#pydantic.json_schema.GenerateJsonSchema.render_warning_message

```
 
    def render_warning_message(kind: JsonSchemaWarningKind, detail: str) -> str | None
    

```

This method is responsible for ignoring warnings as desired, and for formatting the warning messages.

You can override the value of `ignored_warning_kinds` in a subclass of GenerateJsonSchema to modify what warnings are generated. If you want more control, you can override this method; just return None in situations where you don’t want warnings to be emitted.

##### Returns

#returns-82

[`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`None`](https://docs.python.org/3/library/constants.html#None) — The formatted warning message, or `None` if no warning should be emitted.

##### Parameters

#parameters-75

**`kind`** : `JsonSchemaWarningKind`

#pydantic.json_schema.GenerateJsonSchema.render_warning_message\(kind\)

The kind of warning to render. It can be one of the following:

  * ‘skipped-choice’: A choice field was skipped because it had no valid choices.
  * ‘non-serializable-default’: A default value was skipped because it was not JSON-serializable.

**`detail`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

#pydantic.json_schema.GenerateJsonSchema.render_warning_message\(detail\)

A string with additional details about the warning.

## WithJsonSchema 

#pydantic.json_schema.WithJsonSchema

Usage Documentation

[`WithJsonSchema` Annotation](https://pydantic.dev/docs/validation/latest/concepts/json_schema#withjsonschema-annotation) ([local](./../../concepts/json-schema.md#withjsonschema-annotation))

An annotation used to override the JSON Schema for a type.

This is useful when you want to set a JSON Schema for a type that don’t produce any JSON Schemas by default (e.g. [`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)).

If `mode` is set this will only apply to that schema generation mode, allowing you to set different JSON Schemas for validation and serialization.

Note

If the `WithJsonSchema` annotation is coupled with the [`Field()`](https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.Field) ([local](./fields.md#pydantic.fields.Field)) function, the behavior overriding will vary depending on the location:

  * If the [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) metadata is specified at the “top-level” field, `Field()` metadata arguments (excluding [constraints](https://pydantic.dev/docs/validation/latest/concepts/fields#field-constraints) ([local](./../../concepts/fields.md#field-constraints))) such as `title` and `description` will be applied on top of the `WithJsonSchema`, no matter the order:

```
 from typing import Annotated
        
        from pydantic import BaseModel, Field, WithJsonSchema
        
        class Model(BaseModel):
            field: Annotated[
                int,
                Field(title='My Field'),
                WithJsonSchema({'type': 'integer', 'extra': 'data'}),
            ]
        
        Model.model_json_schema()['properties']['field']
        #> {'type': 'integer', 'extra': 'data', 'title': 'My Field'}
        

```

  * If the [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) metadata is specified on a specific inner type, `WithJsonSchema` will unconditionally override the JSON Schema:

```
 from typing import Annotated
        
        from pydantic import BaseModel, Field, WithJsonSchema
        
        class Model(BaseModel):
            field: list[
                Annotated[
                    int,
                    Field(title='My Field'),
                    WithJsonSchema({'type': 'integer', 'extra': 'data'}),
                ]
            ]
        
        Model.model_json_schema()['properties']['field']
        #> {'items': {'extra': 'data', 'type': 'integer'}, 'title': 'Field', 'type': 'array'}
        

```

See also the documentation about [the annotated pattern](https://pydantic.dev/docs/validation/latest/concepts/fields#the-annotated-pattern) ([local](./../../concepts/fields.md#the-annotated-pattern)).

## Examples 

#pydantic.json_schema.Examples

Add examples to a JSON schema.

If the JSON Schema already contains examples, the provided examples will be appended.

If `mode` is set this will only apply to that schema generation mode, allowing you to add different examples for validation and serialization.

## SkipJsonSchema 

#pydantic.json_schema.SkipJsonSchema

Usage Documentation

[`SkipJsonSchema` Annotation](https://pydantic.dev/docs/validation/latest/concepts/json_schema#skipjsonschema-annotation) ([local](./../../concepts/json-schema.md#skipjsonschema-annotation))

Add this as an annotation on a field to skip generating a JSON schema for that field.

## model_json_schema 

#pydantic.json_schema.model_json_schema

```
 
    def model_json_schema(
        cls: type[BaseModel] | type[PydanticDataclass],
        by_alias: bool = True,
        ref_template: str = DEFAULT_REF_TEMPLATE,
        union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
        schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
        mode: JsonSchemaMode = 'validation',
    ) -> dict[str, Any]
    

```

Utility function to generate a JSON Schema for a model.

### Returns

#returns-83

[`dict`](https://docs.python.org/3/reference/expressions.html#dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)] — The generated JSON Schema.

### Parameters

#parameters-76

**`cls`** : [`type`](https://docs.python.org/3/glossary.html#term-type)[[`BaseModel`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel) ([local](./base-model.md#pydantic.BaseModel))] | [`type`](https://docs.python.org/3/glossary.html#term-type)[`PydanticDataclass`] 

#pydantic.json_schema.model_json_schema\(cls\)

The model class to generate a JSON Schema for.

**`by_alias`** : [`bool`](https://docs.python.org/3/library/functions.html#bool) _Default:_ `True`

#pydantic.json_schema.model_json_schema\(by_alias\)

If `True` (the default), fields will be serialized according to their alias. If `False`, fields will be serialized according to their attribute name.

**`ref_template`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str) _Default:_ `DEFAULT_REF_TEMPLATE`

#pydantic.json_schema.model_json_schema\(ref_template\)

The template to use for generating JSON Schema references.

**`union_format`** : [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal)[‘any_of’, ‘primitive_type_array’] _Default:_ `'any_of'`

#pydantic.json_schema.model_json_schema\(union_format\)

The format to use when combining schemas from unions together. Can be one of:

  * `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf) keyword to combine schemas (the default).
  * `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type) keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

**`schema_generator`** : [`type`](https://docs.python.org/3/glossary.html#term-type)[`GenerateJsonSchema`] _Default:_ `GenerateJsonSchema`

#pydantic.json_schema.model_json_schema\(schema_generator\)

The class to use for generating the JSON Schema.

**`mode`** : `JsonSchemaMode` _Default:_ `'validation'`

#pydantic.json_schema.model_json_schema\(mode\)

The mode to use for generating the JSON Schema. It can be one of the following:

  * ‘validation’: Generate a JSON Schema for validating data.
  * ‘serialization’: Generate a JSON Schema for serializing data.

## models_json_schema 

#pydantic.json_schema.models_json_schema

```
 
    def models_json_schema(
        models: Sequence[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode]],
        by_alias: bool = True,
        title: str | None = None,
        description: str | None = None,
        ref_template: str = DEFAULT_REF_TEMPLATE,
        union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
        schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
    ) -> tuple[dict[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode], JsonSchemaValue], JsonSchemaValue]
    

```

Utility function to generate a JSON Schema for multiple models.

### Returns

#returns-84

[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[[`dict`](https://docs.python.org/3/reference/expressions.html#dict)[[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[[`type`](https://docs.python.org/3/glossary.html#term-type)[[`BaseModel`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel) ([local](./base-model.md#pydantic.BaseModel))] | [`type`](https://docs.python.org/3/glossary.html#term-type)[`PydanticDataclass`], `JsonSchemaMode`], `JsonSchemaValue`], `JsonSchemaValue`] — A tuple where:

  * The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have JsonRef references to definitions that are defined in the second returned element.)
  * The second element is a JSON schema containing all definitions referenced in the first returned element, along with the optional title and description keys.

### Parameters

#parameters-77

**`models`** : [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence)[[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[[`type`](https://docs.python.org/3/glossary.html#term-type)[[`BaseModel`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel) ([local](./base-model.md#pydantic.BaseModel))] | [`type`](https://docs.python.org/3/glossary.html#term-type)[`PydanticDataclass`], `JsonSchemaMode`]] 

#pydantic.json_schema.models_json_schema\(models\)

A sequence of tuples of the form (model, mode).

**`by_alias`** : [`bool`](https://docs.python.org/3/library/functions.html#bool) _Default:_ `True`

#pydantic.json_schema.models_json_schema\(by_alias\)

Whether field aliases should be used as keys in the generated JSON Schema.

**`title`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`None`](https://docs.python.org/3/library/constants.html#None) _Default:_ `None`

#pydantic.json_schema.models_json_schema\(title\)

The title of the generated JSON Schema.

**`description`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`None`](https://docs.python.org/3/library/constants.html#None) _Default:_ `None`

#pydantic.json_schema.models_json_schema\(description\)

The description of the generated JSON Schema.

**`ref_template`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str) _Default:_ `DEFAULT_REF_TEMPLATE`

#pydantic.json_schema.models_json_schema\(ref_template\)

The reference template to use for generating JSON Schema references.

**`union_format`** : [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal)[‘any_of’, ‘primitive_type_array’] _Default:_ `'any_of'`

#pydantic.json_schema.models_json_schema\(union_format\)

The format to use when combining schemas from unions together. Can be one of:

  * `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf) keyword to combine schemas (the default).
  * `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type) keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

**`schema_generator`** : [`type`](https://docs.python.org/3/glossary.html#term-type)[`GenerateJsonSchema`] _Default:_ `GenerateJsonSchema`

#pydantic.json_schema.models_json_schema\(schema_generator\)

The schema generator to use for generating the JSON Schema.

## CoreSchemaOrFieldType 

#pydantic.json_schema.CoreSchemaOrFieldType

A type alias for defined schema types that represents a union of `core_schema.CoreSchemaType` and `core_schema.CoreSchemaFieldType`.

**Default:** `Literal[core_schema.CoreSchemaType, core_schema.CoreSchemaFieldType]`

## JsonSchemaValue 

#pydantic.json_schema.JsonSchemaValue

A type alias for a JSON schema value. This is a dictionary of string keys to arbitrary JSON values.

**Default:** `dict[str, Any]`

## JsonSchemaMode 

#pydantic.json_schema.JsonSchemaMode

A type alias that represents the mode of a JSON schema; either ‘validation’ or ‘serialization’.

For some types, the inputs to validation differ from the outputs of serialization. For example, computed fields will only be present when serializing, and should not be provided when validating. This flag provides a way to indicate whether you want the JSON schema required for validation inputs, or that will be matched by serialization outputs.

**Default:** `Literal['validation', 'serialization']`

## JsonSchemaWarningKind 

#pydantic.json_schema.JsonSchemaWarningKind

A type alias representing the kinds of warnings that can be emitted during JSON schema generation.

See [`GenerateJsonSchema.render_warning_message`](#pydantic.json_schema.GenerateJsonSchema.render_warning_message) for more details.

**Default:** `Literal['skipped-choice', 'non-serializable-default', 'skipped-discriminator']`

## NoDefault 

#pydantic.json_schema.NoDefault

A sentinel value used to indicate that no default value should be used when generating a JSON Schema for a core schema with a default value.

**Default:** `object()`

## DEFAULT_REF_TEMPLATE 

#pydantic.json_schema.DEFAULT_REF_TEMPLATE

The default format string used to generate reference names.

**Default:** `'#/$defs/{model}'`
