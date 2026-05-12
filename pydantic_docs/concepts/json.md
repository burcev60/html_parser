---
title: JSON
source: https://pydantic.dev/docs/validation/latest/concepts/json
---

## Json Parsing

[](<https://pydantic.dev/docs/validation/latest/concepts/json#json-parsing> ([local](./json.md#json-parsing)))

API Documentation

[`pydantic.main.BaseModel.model_validate_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_validate_json> ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_validate_json))) [`pydantic.type_adapter.TypeAdapter.validate_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_json> ([local](./../api/pydantic/type_adapter.md#pydantic.type_adapter.TypeAdapter.validate_json))) [`pydantic_core.from_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic-core/pydantic_core/#pydantic_core.from_json> ([local](./../api/pydantic-core/pydantic_core.md#pydantic_core.from_json)))

Pydantic provides builtin JSON parsing, which helps achieve:

  * Significant performance improvements without the cost of using a 3rd party library
  * Support for custom errors
  * Support for `strict` specifications

Here’s an example of Pydantic’s builtin JSON parsing via the [`model_validate_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_validate_json> ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_validate_json))) method, showcasing the support for `strict` specifications while parsing JSON data that doesn’t match the model’s type annotations:

```
 
    from datetime import date
    
    from pydantic import BaseModel, ConfigDict, ValidationError
    
    
    class Event(BaseModel):
      model_config = ConfigDict(strict=True)
    
      when: date
      where: tuple[int, int]
    
    
    json_data = '{"when": "1987-01-28", "where": [51, -1]}'
    print(Event.model_validate_json(json_data))  # (1)
    #> when=datetime.date(1987, 1, 28) where=(51, -1)
    
    try:
      Event.model_validate({'when': '1987-01-28', 'where': [51, -1]})  # (2)
    except ValidationError as e:
      print(e)
      """
      2 validation errors for Event
      when
        Input should be a valid date [type=date_type, input_value='1987-01-28', input_type=str]
      where
        Input should be a valid tuple [type=tuple_type, input_value=[51, -1], input_type=list]
      """

```

In v2.5.0 and above, Pydantic uses [`jiter`](<https://docs.rs/jiter/latest/jiter/>), a fast and iterable JSON parser, to parse JSON data. Using `jiter` compared to `serde` results in modest performance improvements that will get even better in the future.

The `jiter` JSON parser is almost entirely compatible with the `serde` JSON parser, with one noticeable enhancement being that `jiter` supports deserialization of `inf` and `NaN` values. In the future, `jiter` is intended to enable support validation errors to include the location in the original JSON input which contained the invalid value.

### Partial JSON Parsing

[](<https://pydantic.dev/docs/validation/latest/concepts/json#partial-json-parsing> ([local](./json.md#partial-json-parsing)))

**Starting in v2.7.0** , Pydantic’s [JSON parser](<https://docs.rs/jiter/latest/jiter/>) offers support for partial JSON parsing, which is exposed via [`pydantic_core.from_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic-core/pydantic_core/#pydantic_core.from_json> ([local](./../api/pydantic-core/pydantic_core.md#pydantic_core.from_json))). Here’s an example of this feature in action:

```
 
    from pydantic_core import from_json
    
    partial_json_data = '["aa", "bb", "c'  # (1)
    
    try:
      result = from_json(partial_json_data, allow_partial=False)
    except ValueError as e:
      print(e)  # (2)
      #> EOF while parsing a string at line 1 column 15
    
    result = from_json(partial_json_data, allow_partial=True)
    print(result)  # (3)
    #> ['aa', 'bb']

```

This also works for deserializing partial dictionaries. For example:

```
 
    from pydantic_core import from_json
    
    partial_dog_json = '{"breed": "lab", "name": "fluffy", "friends": ["buddy", "spot", "rufus"], "age'
    dog_dict = from_json(partial_dog_json, allow_partial=True)
    print(dog_dict)
    #> {'breed': 'lab', 'name': 'fluffy', 'friends': ['buddy', 'spot', 'rufus']}
    

```

Validating LLM Output

This feature is particularly beneficial for validating LLM outputs. We’ve written some blog posts about this topic, which you can find on [our website](<https://pydantic.dev/articles>).

In future versions of Pydantic, we expect to expand support for this feature through either Pydantic’s other JSON validation functions ([`pydantic.main.BaseModel.model_validate_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_validate_json> ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_validate_json))) and [`pydantic.type_adapter.TypeAdapter.validate_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_json> ([local](./../api/pydantic/type_adapter.md#pydantic.type_adapter.TypeAdapter.validate_json)))) or model configuration. Stay tuned 🚀!

For now, you can use [`pydantic_core.from_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic-core/pydantic_core/#pydantic_core.from_json> ([local](./../api/pydantic-core/pydantic_core.md#pydantic_core.from_json))) in combination with [`pydantic.main.BaseModel.model_validate`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_validate> ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_validate))) to achieve the same result. Here’s an example:

```
 
    from pydantic_core import from_json
    
    from pydantic import BaseModel
    
    
    class Dog(BaseModel):
        breed: str
        name: str
        friends: list
    
    
    partial_dog_json = '{"breed": "lab", "name": "fluffy", "friends": ["buddy", "spot", "rufus"], "age'
    dog = Dog.model_validate(from_json(partial_dog_json, allow_partial=True))
    print(repr(dog))
    #> Dog(breed='lab', name='fluffy', friends=['buddy', 'spot', 'rufus'])
    

```

Tip

For partial JSON parsing to work reliably, all fields on the model should have default values.

Check out the following example for a more in-depth look at how to use default values with partial JSON parsing:

Using default values with partial JSON parsing

```

    from typing import Annotated, Any, Optional
    
    import pydantic_core
    
    from pydantic import BaseModel, ValidationError, WrapValidator
    
    
    def default_on_error(v, handler) -> Any:
        """
        Raise a PydanticUseDefault exception if the value is missing.
    
        This is useful for avoiding errors from partial
        JSON preventing successful validation.
        """
        try:
            return handler(v)
        except ValidationError as exc:
            # there might be other types of errors resulting from partial JSON parsing
            # that you allow here, feel free to customize as needed
            if all(e['type'] == 'missing' for e in exc.errors()):
                raise pydantic_core.PydanticUseDefault()
            else:
                raise
    
    
    class NestedModel(BaseModel):
        x: int
        y: str
    
    
    class MyModel(BaseModel):
        foo: Optional[str] = None
        bar: Annotated[
            Optional[tuple[str, int]], WrapValidator(default_on_error)
        ] = None
        nested: Annotated[
            Optional[NestedModel], WrapValidator(default_on_error)
        ] = None
    
    
    m = MyModel.model_validate(
        pydantic_core.from_json('{"foo": "x", "bar": ["world",', allow_partial=True)
    )
    print(repr(m))
    #> MyModel(foo='x', bar=None, nested=None)
    
    
    m = MyModel.model_validate(
        pydantic_core.from_json(
            '{"foo": "x", "bar": ["world", 1], "nested": {"x":', allow_partial=True
        )
    )
    print(repr(m))
    #> MyModel(foo='x', bar=('world', 1), nested=None)
    

```

### Caching Strings

[](<https://pydantic.dev/docs/validation/latest/concepts/json#caching-strings> ([local](./json.md#caching-strings)))

**Starting in v2.7.0** , Pydantic’s [JSON parser](<https://docs.rs/jiter/latest/jiter/>) offers support for configuring how Python strings are cached during JSON parsing and validation (when Python strings are constructed from Rust strings during Python validation, e.g. after `strip_whitespace=True`). The `cache_strings` setting is exposed via both [model config](<https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.config.ConfigDict> ([local](./../api/pydantic/config.md#pydantic.config.ConfigDict))) and [`pydantic_core.from_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic-core/pydantic_core/#pydantic_core.from_json> ([local](./../api/pydantic-core/pydantic_core.md#pydantic_core.from_json))).

The `cache_strings` setting can take any of the following values:

  * `True` or `'all'` (the default): cache all strings
  * `'keys'`: cache only dictionary keys, this **only** applies when used with [`pydantic_core.from_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic-core/pydantic_core/#pydantic_core.from_json> ([local](./../api/pydantic-core/pydantic_core.md#pydantic_core.from_json))) or when parsing JSON using [`Json`](<https://pydantic.dev/docs/validation/latest/api/pydantic/types/#pydantic.types.Json> ([local](./../api/pydantic/types.md#pydantic.types.Json)))
  * `False` or `'none'`: no caching

Using the string caching feature results in performance improvements, but increases memory usage slightly.

String Caching Details

  1. Strings are cached using a fully associative cache with a size of [16,384](<https://github.com/pydantic/jiter/blob/5bbdcfd22882b7b286416b22f74abd549c7b2fd7/src/py_string_cache.rs#L113>).
  2. Only strings where `len(string) < 64` are cached.
  3. There is some overhead to looking up the cache, which is normally worth it to avoid constructing strings. However, if you know there will be very few repeated strings in your data, you might get a performance boost by disabling this setting with `cache_strings=False`.

## JSON Serialization

[](<https://pydantic.dev/docs/validation/latest/concepts/json#json-serialization> ([local](./json.md#json-serialization)))

API Documentation

[`pydantic.main.BaseModel.model_dump_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_dump_json> ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_dump_json)))  
[`pydantic.type_adapter.TypeAdapter.dump_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic/type_adapter/#pydantic.type_adapter.TypeAdapter.dump_json> ([local](./../api/pydantic/type_adapter.md#pydantic.type_adapter.TypeAdapter.dump_json)))  
[`pydantic_core.to_json`](<https://pydantic.dev/docs/validation/latest/api/pydantic-core/pydantic_core/#pydantic_core.to_json> ([local](./../api/pydantic-core/pydantic_core.md#pydantic_core.to_json)))  

For more information on JSON serialization, see the [serialization concepts](<https://pydantic.dev/docs/validation/latest/concepts/serialization> ([local](./serialization.md))) page.
