---
title: Aliases
source: https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/
---

Support for alias configurations.

## AliasPath 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath> ([local](./aliases.md#pydantic.aliases.AliasPath)) ([local](./aliases.md#pydantic.aliases.AliasPath))

Usage Documentation

[`AliasPath` and `AliasChoices`](https://pydantic.dev/docs/validation/latest/concepts/alias#aliaspath-and-aliaschoices) ([local](./../../concepts/alias.md#aliaspath-and-aliaschoices))

A data class used by `validation_alias` as a convenience to create aliases.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#attributes> ([local](./aliases.md#attributes)) ([local](./aliases.md#attributes))

#### path 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath.path> ([local](./aliases.md#pydantic.aliases.AliasPath.path)) ([local](./aliases.md#pydantic.aliases.AliasPath.path))

A list of string or integer aliases.

**Type:** [`list`](https://docs.python.org/3/glossary.html#term-list)[[`int`](https://docs.python.org/3/library/functions.html#int) | [`str`](https://docs.python.org/3/library/stdtypes.html#str)]

### Methods

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#methods> ([local](./aliases.md#methods)) ([local](./aliases.md#methods))

#### convert_to_aliases 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath.convert_to_aliases> ([local](./aliases.md#pydantic.aliases.AliasPath.convert_to_aliases)) ([local](./aliases.md#pydantic.aliases.AliasPath.convert_to_aliases))

```
 
    def convert_to_aliases() -> list[str | int]
    

```

Converts arguments to a list of string or integer aliases.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#returns> ([local](./aliases.md#returns)) ([local](./aliases.md#returns))

[`list`](https://docs.python.org/3/glossary.html#term-list)[[`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`int`](https://docs.python.org/3/library/functions.html#int)] — The list of aliases.

#### search_dict_for_path 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath.search_dict_for_path> ([local](./aliases.md#pydantic.aliases.AliasPath.search_dict_for_path)) ([local](./aliases.md#pydantic.aliases.AliasPath.search_dict_for_path))

```
 
    def search_dict_for_path(d: dict) -> Any
    

```

Searches a dictionary for the path specified by the alias.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#returns-1> ([local](./aliases.md#returns-1)) ([local](./aliases.md#returns-1))

[`Any`](https://docs.python.org/3/library/typing.html#typing.Any) — The value at the specified path, or `PydanticUndefined` if the path is not found.

## AliasChoices 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasChoices> ([local](./aliases.md#pydantic.aliases.AliasChoices)) ([local](./aliases.md#pydantic.aliases.AliasChoices))

Usage Documentation

[`AliasPath` and `AliasChoices`](https://pydantic.dev/docs/validation/latest/concepts/alias#aliaspath-and-aliaschoices) ([local](./../../concepts/alias.md#aliaspath-and-aliaschoices))

A data class used by `validation_alias` as a convenience to create aliases.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#attributes-1> ([local](./aliases.md#attributes-1)) ([local](./aliases.md#attributes-1))

#### choices 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasChoices.choices> ([local](./aliases.md#pydantic.aliases.AliasChoices.choices)) ([local](./aliases.md#pydantic.aliases.AliasChoices.choices))

A list containing a string or `AliasPath`.

**Type:** [`list`](https://docs.python.org/3/glossary.html#term-list)[[`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`AliasPath`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath) ([local](./aliases.md#pydantic.aliases.AliasPath))]

### Methods

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#methods-1> ([local](./aliases.md#methods-1)) ([local](./aliases.md#methods-1))

#### convert_to_aliases 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasChoices.convert_to_aliases> ([local](./aliases.md#pydantic.aliases.AliasChoices.convert_to_aliases)) ([local](./aliases.md#pydantic.aliases.AliasChoices.convert_to_aliases))

```
 
    def convert_to_aliases() -> list[list[str | int]]
    

```

Converts arguments to a list of lists containing string or integer aliases.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#returns-2> ([local](./aliases.md#returns-2)) ([local](./aliases.md#returns-2))

[`list`](https://docs.python.org/3/glossary.html#term-list)[[`list`](https://docs.python.org/3/glossary.html#term-list)[[`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`int`](https://docs.python.org/3/library/functions.html#int)]] — The list of aliases.

## AliasGenerator 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasGenerator> ([local](./aliases.md#pydantic.aliases.AliasGenerator)) ([local](./aliases.md#pydantic.aliases.AliasGenerator))

Usage Documentation

[Using an `AliasGenerator`](https://pydantic.dev/docs/validation/latest/concepts/alias#using-an-aliasgenerator) ([local](./../../concepts/alias.md#using-an-aliasgenerator))

A data class used by `alias_generator` as a convenience to create various aliases.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#attributes-2> ([local](./aliases.md#attributes-2)) ([local](./aliases.md#attributes-2))

#### alias 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasGenerator.alias> ([local](./aliases.md#pydantic.aliases.AliasGenerator.alias)) ([local](./aliases.md#pydantic.aliases.AliasGenerator.alias))

A callable that takes a field name and returns an alias for it.

**Type:** [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)] | [`None`](https://docs.python.org/3/library/constants.html#None)

#### validation_alias 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasGenerator.validation_alias> ([local](./aliases.md#pydantic.aliases.AliasGenerator.validation_alias)) ([local](./aliases.md#pydantic.aliases.AliasGenerator.validation_alias))

A callable that takes a field name and returns a validation alias for it.

**Type:** [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`AliasPath`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath) ([local](./aliases.md#pydantic.aliases.AliasPath)) | [`AliasChoices`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasChoices) ([local](./aliases.md#pydantic.aliases.AliasChoices))] | [`None`](https://docs.python.org/3/library/constants.html#None)

#### serialization_alias 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasGenerator.serialization_alias> ([local](./aliases.md#pydantic.aliases.AliasGenerator.serialization_alias)) ([local](./aliases.md#pydantic.aliases.AliasGenerator.serialization_alias))

A callable that takes a field name and returns a serialization alias for it.

**Type:** [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`str`](https://docs.python.org/3/library/stdtypes.html#str)], [`str`](https://docs.python.org/3/library/stdtypes.html#str)] | [`None`](https://docs.python.org/3/library/constants.html#None)

### Methods

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#methods-2> ([local](./aliases.md#methods-2)) ([local](./aliases.md#methods-2))

#### generate_aliases 

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasGenerator.generate_aliases> ([local](./aliases.md#pydantic.aliases.AliasGenerator.generate_aliases)) ([local](./aliases.md#pydantic.aliases.AliasGenerator.generate_aliases))

```
 
    def generate_aliases(
        field_name: str,
    ) -> tuple[str | None, str | AliasPath | AliasChoices | None, str | None]
    

```

Generate `alias`, `validation_alias`, and `serialization_alias` for a field.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#returns-3> ([local](./aliases.md#returns-3)) ([local](./aliases.md#returns-3))

[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`None`](https://docs.python.org/3/library/constants.html#None), [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`AliasPath`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath) ([local](./aliases.md#pydantic.aliases.AliasPath)) | [`AliasChoices`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasChoices) ([local](./aliases.md#pydantic.aliases.AliasChoices)) | [`None`](https://docs.python.org/3/library/constants.html#None), [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`None`](https://docs.python.org/3/library/constants.html#None)] — A tuple of three aliases - validation, alias, and serialization.
