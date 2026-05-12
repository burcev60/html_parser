---
title: Alias
source: https://pydantic.dev/docs/validation/latest/concepts/alias
---

An alias is an alternative name for a field, used when serializing and deserializing data.

You can specify an alias in the following ways:

  * `alias` on the [`Field`](https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.Field) ([local](./../api/pydantic/fields.md#pydantic.fields.Field))
    * must be a `str`
  * `validation_alias` on the [`Field`](https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.Field) ([local](./../api/pydantic/fields.md#pydantic.fields.Field))
    * can be an instance of `str`, [`AliasPath`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath) ([local](./../api/pydantic/aliases.md#pydantic.aliases.AliasPath)), or [`AliasChoices`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasChoices) ([local](./../api/pydantic/aliases.md#pydantic.aliases.AliasChoices))
  * `serialization_alias` on the [`Field`](https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.Field) ([local](./../api/pydantic/fields.md#pydantic.fields.Field))
    * must be a `str`
  * `alias_generator` on the [`Config`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.config.ConfigDict.alias_generator) ([local](./../api/pydantic/config.md#pydantic.config.ConfigDict.alias_generator))
    * can be a callable or an instance of [`AliasGenerator`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasGenerator) ([local](./../api/pydantic/aliases.md#pydantic.aliases.AliasGenerator))

For examples of how to use `alias`, `validation_alias`, and `serialization_alias`, see [Field aliases](https://pydantic.dev/docs/validation/latest/concepts/fields#field-aliases) ([local](./fields.md#field-aliases)).

## `AliasPath` and `AliasChoices`

<https://pydantic.dev/docs/validation/latest/concepts/alias#aliaspath-and-aliaschoices> ([local](./alias.md#aliaspath-and-aliaschoices)) ([local](./alias.md#aliaspath-and-aliaschoices))

API Documentation

[`pydantic.aliases.AliasPath`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasPath) ([local](./../api/pydantic/aliases.md#pydantic.aliases.AliasPath))  
[`pydantic.aliases.AliasChoices`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasChoices) ([local](./../api/pydantic/aliases.md#pydantic.aliases.AliasChoices))  

Pydantic provides two special types for convenience when using `validation_alias`: `AliasPath` and `AliasChoices`.

The `AliasPath` is used to specify a path to a field using aliases. For example:

```
 
    from pydantic import BaseModel, Field, AliasPath
    
    
    class User(BaseModel):
      first_name: str = Field(validation_alias=AliasPath('names', 0))
      last_name: str = Field(validation_alias=AliasPath('names', 1))
      address: str = Field(validation_alias=AliasPath('contact', 'address'))
    
    user = User.model_validate({  # (1)
      'names': ['John', 'Doe'],
      'contact': {'address': '221B Baker Street'}
    })
    print(user)
    #> first_name='John' last_name='Doe' address='221B Baker Street'

```

In the `'first_name'` field, we are using the alias `'names'` and the index `0` to specify the path to the first name. In the `'last_name'` field, we are using the alias `'names'` and the index `1` to specify the path to the last name.

`AliasChoices` is used to specify a list of choices of aliases. Choices that appear first in the list will have higher priority during validation. For example:

```
 
    from pydantic import BaseModel, Field, AliasChoices
    
    
    class User(BaseModel):
      first_name: str = Field(validation_alias=AliasChoices('first_name', 'fname'))
      last_name: str = Field(validation_alias=AliasChoices('last_name', 'lname'))
    
    user = User.model_validate({'fname': 'John', 'lname': 'Doe'})  # (1)
    print(user)
    #> first_name='John' last_name='Doe'
    user = User.model_validate({'first_name': 'John', 'lname': 'Doe'})  # (2)
    print(user)
    #> first_name='John' last_name='Doe'
    user = User.model_validate({'first_name': 'John', 'fname': 'J', 'lname': 'Doe'})  # (3)
    print(user)
    #> first_name='John' last_name='Doe'

```

You can also use `AliasChoices` with `AliasPath`:

```
 
    from pydantic import BaseModel, Field, AliasPath, AliasChoices
    
    
    class User(BaseModel):
        first_name: str = Field(validation_alias=AliasChoices('first_name', AliasPath('names', 0)))
        last_name: str = Field(validation_alias=AliasChoices('last_name', AliasPath('names', 1)))
    
    
    user = User.model_validate({'first_name': 'John', 'last_name': 'Doe'})
    print(user)
    #> first_name='John' last_name='Doe'
    user = User.model_validate({'names': ['John', 'Doe']})
    print(user)
    #> first_name='John' last_name='Doe'
    user = User.model_validate({'names': ['John'], 'last_name': 'Doe'})
    print(user)
    #> first_name='John' last_name='Doe'
    

```

## Using alias generators

<https://pydantic.dev/docs/validation/latest/concepts/alias#using-alias-generators> ([local](./alias.md#using-alias-generators)) ([local](./alias.md#using-alias-generators))

You can use the `alias_generator` parameter of [`Config`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.config.ConfigDict.alias_generator) ([local](./../api/pydantic/config.md#pydantic.config.ConfigDict.alias_generator)) to specify a callable (or group of callables, via `AliasGenerator`) that will generate aliases for all fields in a model. This is useful if you want to use a consistent naming convention for all fields in a model, but do not want to specify the alias for each field individually.

Note

Pydantic offers three built-in alias generators that you can use out of the box:

[`to_pascal`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.alias_generators.to_pascal) ([local](./../api/pydantic/config.md#pydantic.alias_generators.to_pascal))  
[`to_camel`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.alias_generators.to_camel) ([local](./../api/pydantic/config.md#pydantic.alias_generators.to_camel))  
[`to_snake`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.alias_generators.to_snake) ([local](./../api/pydantic/config.md#pydantic.alias_generators.to_snake))  

### Using a callable

<https://pydantic.dev/docs/validation/latest/concepts/alias#using-a-callable> ([local](./alias.md#using-a-callable)) ([local](./alias.md#using-a-callable))

Here’s a basic example using a callable:

```
 
    from pydantic import BaseModel, ConfigDict
    
    
    class Tree(BaseModel):
        model_config = ConfigDict(
            alias_generator=lambda field_name: field_name.upper()
        )
    
        age: int
        height: float
        kind: str
    
    
    t = Tree.model_validate({'AGE': 12, 'HEIGHT': 1.2, 'KIND': 'oak'})
    print(t.model_dump(by_alias=True))
    #> {'AGE': 12, 'HEIGHT': 1.2, 'KIND': 'oak'}
    

```

### Using an `AliasGenerator`

<https://pydantic.dev/docs/validation/latest/concepts/alias#using-an-aliasgenerator> ([local](./alias.md#using-an-aliasgenerator)) ([local](./alias.md#using-an-aliasgenerator))

API Documentation

[`pydantic.aliases.AliasGenerator`](https://pydantic.dev/docs/validation/latest/api/pydantic/aliases/#pydantic.aliases.AliasGenerator) ([local](./../api/pydantic/aliases.md#pydantic.aliases.AliasGenerator))  

`AliasGenerator` is a class that allows you to specify multiple alias generators for a model. You can use an `AliasGenerator` to specify different alias generators for validation and serialization.

This is particularly useful if you need to use different naming conventions for loading and saving data, but you don’t want to specify the validation and serialization aliases for each field individually.

For example:

```
 
    from pydantic import AliasGenerator, BaseModel, ConfigDict
    
    
    class Tree(BaseModel):
        model_config = ConfigDict(
            alias_generator=AliasGenerator(
                validation_alias=lambda field_name: field_name.upper(),
                serialization_alias=lambda field_name: field_name.title(),
            )
        )
    
        age: int
        height: float
        kind: str
    
    
    t = Tree.model_validate({'AGE': 12, 'HEIGHT': 1.2, 'KIND': 'oak'})
    print(t.model_dump(by_alias=True))
    #> {'Age': 12, 'Height': 1.2, 'Kind': 'oak'}
    

```

## Alias Precedence

<https://pydantic.dev/docs/validation/latest/concepts/alias#alias-precedence> ([local](./alias.md#alias-precedence)) ([local](./alias.md#alias-precedence))

If you specify an `alias` on the [`Field`](https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.Field) ([local](./../api/pydantic/fields.md#pydantic.fields.Field)), it will take precedence over the generated alias by default:

```
 
    from pydantic import BaseModel, ConfigDict, Field
    
    
    def to_camel(string: str) -> str:
        return ''.join(word.capitalize() for word in string.split('_'))
    
    
    class Voice(BaseModel):
        model_config = ConfigDict(alias_generator=to_camel)
    
        name: str
        language_code: str = Field(alias='lang')
    
    
    voice = Voice(Name='Filiz', lang='tr-TR')
    print(voice.language_code)
    #> tr-TR
    print(voice.model_dump(by_alias=True))
    #> {'Name': 'Filiz', 'lang': 'tr-TR'}
    

```

### Alias Priority

<https://pydantic.dev/docs/validation/latest/concepts/alias#alias-priority> ([local](./alias.md#alias-priority)) ([local](./alias.md#alias-priority))

You may set `alias_priority` on a field to change this behavior:

  * `alias_priority=2` the alias will _not_ be overridden by the alias generator.
  * `alias_priority=1` the alias _will_ be overridden by the alias generator.
  * `alias_priority` not set: 
    * alias is set: the alias will _not_ be overridden by the alias generator.
    * alias is not set: the alias _will_ be overridden by the alias generator.

The same precedence applies to `validation_alias` and `serialization_alias`. See more about the different field aliases under [field aliases](https://pydantic.dev/docs/validation/latest/concepts/fields#field-aliases) ([local](./fields.md#field-aliases)).

## Alias Configuration

<https://pydantic.dev/docs/validation/latest/concepts/alias#alias-configuration> ([local](./alias.md#alias-configuration)) ([local](./alias.md#alias-configuration))

You can use [`ConfigDict`](https://pydantic.dev/docs/validation/latest/concepts/config) ([local](./config.md)) settings or runtime validation/serialization settings to control whether or not aliases are used.

### `ConfigDict` Settings

<https://pydantic.dev/docs/validation/latest/concepts/alias#configdict-settings> ([local](./alias.md#configdict-settings)) ([local](./alias.md#configdict-settings))

You can use [configuration settings](https://pydantic.dev/docs/validation/latest/concepts/config) ([local](./config.md)) to control, at the model level, whether or not aliases are used for validation and serialization. If you would like to control this behavior for nested models/surpassing the config-model boundary, use [runtime settings](https://pydantic.dev/docs/validation/latest/concepts/alias#runtime-settings) ([local](./alias.md#runtime-settings)).

#### Validation

<https://pydantic.dev/docs/validation/latest/concepts/alias#validation> ([local](./alias.md#validation)) ([local](./alias.md#validation))

When validating data, you can enable population of attributes by attribute name, alias, or both. **By default** , Pydantic uses aliases for validation. Further configuration is available via:

  * [`ConfigDict.validate_by_alias`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.config.ConfigDict.validate_by_alias) ([local](./../api/pydantic/config.md#pydantic.config.ConfigDict.validate_by_alias)): `True` by default
  * [`ConfigDict.validate_by_name`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.config.ConfigDict.validate_by_name) ([local](./../api/pydantic/config.md#pydantic.config.ConfigDict.validate_by_name)): `False` by default

  * [ validate_by_alias ](https://pydantic.dev/docs/validation/latest/concepts/alias#tab-panel-516) ([local](./alias.md#tab-panel-516))
  * [ validate_by_name ](https://pydantic.dev/docs/validation/latest/concepts/alias#tab-panel-517) ([local](./alias.md#tab-panel-517))
  * [ validate_by_alias and validate_by_name ](https://pydantic.dev/docs/validation/latest/concepts/alias#tab-panel-518) ([local](./alias.md#tab-panel-518))

```
 
    from pydantic import BaseModel, ConfigDict, Field
    
    
    class Model(BaseModel):
      my_field: str = Field(validation_alias='my_alias')
    
      model_config = ConfigDict(validate_by_alias=True, validate_by_name=False)
    
    
    print(repr(Model(my_alias='foo')))  # (1)
    #> Model(my_field='foo')

```

```
 
    from pydantic import BaseModel, ConfigDict, Field
    
    
    class Model(BaseModel):
      my_field: str = Field(validation_alias='my_alias')
    
      model_config = ConfigDict(validate_by_alias=False, validate_by_name=True)
    
    
    print(repr(Model(my_field='foo')))  # (1)
    #> Model(my_field='foo')

```

```
 
    from pydantic import BaseModel, ConfigDict, Field
    
    
    class Model(BaseModel):
      my_field: str = Field(validation_alias='my_alias')
    
      model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)
    
    
    print(repr(Model(my_alias='foo')))  # (1)
    #> Model(my_field='foo')
    
    print(repr(Model(my_field='foo')))  # (2)
    #> Model(my_field='foo')

```

Caution

You cannot set both `validate_by_alias` and `validate_by_name` to `False`. A [user error](https://pydantic.dev/docs/validation/latest/errors/usage_errors#validate-by-alias-and-name-false) ([local](./../errors/usage_errors.md#validate-by-alias-and-name-false)) is raised in this case.

#### Serialization

<https://pydantic.dev/docs/validation/latest/concepts/alias#serialization> ([local](./alias.md#serialization)) ([local](./alias.md#serialization))

When serializing data, you can enable serialization by alias, which is disabled by default. See the [`ConfigDict.serialize_by_alias`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.config.ConfigDict.serialize_by_alias) ([local](./../api/pydantic/config.md#pydantic.config.ConfigDict.serialize_by_alias)) API documentation for more details.

```
 
    from pydantic import BaseModel, ConfigDict, Field
    
    
    class Model(BaseModel):
      my_field: str = Field(serialization_alias='my_alias')
    
      model_config = ConfigDict(serialize_by_alias=True)
    
    
    m = Model(my_field='foo')
    print(m.model_dump())  # (1)
    #> {'my_alias': 'foo'}

```

Note

The fact that serialization by alias is disabled by default is notably inconsistent with the default for validation (where aliases are used by default). We anticipate changing this default in V3.

### Runtime Settings

<https://pydantic.dev/docs/validation/latest/concepts/alias#runtime-settings> ([local](./alias.md#runtime-settings)) ([local](./alias.md#runtime-settings))

You can use runtime alias flags to control alias use for validation and serialization on a per-call basis. If you would like to control this behavior on a model level, use [`ConfigDict` settings](https://pydantic.dev/docs/validation/latest/concepts/alias#configdict-settings) ([local](./alias.md#configdict-settings)).

#### Validation

<https://pydantic.dev/docs/validation/latest/concepts/alias#validation-1> ([local](./alias.md#validation-1)) ([local](./alias.md#validation-1))

When validating data, you can enable population of attributes by attribute name, alias, or both.

The `by_alias` and `by_name` flags are available on the [`model_validate()`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_validate) ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_validate)), [`model_validate_json()`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_validate_json) ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_validate_json)), and [`model_validate_strings()`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_validate_strings) ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_validate_strings)) methods, as well as the [`TypeAdapter`](https://pydantic.dev/docs/validation/latest/api/pydantic/type_adapter/#pydantic.type_adapter.TypeAdapter) ([local](./../api/pydantic/type_adapter.md#pydantic.type_adapter.TypeAdapter)) validation methods.

By default:

  * `by_alias` is `True`
  * `by_name` is `False`

  * [ by_alias ](https://pydantic.dev/docs/validation/latest/concepts/alias#tab-panel-519) ([local](./alias.md#tab-panel-519))
  * [ by_name ](https://pydantic.dev/docs/validation/latest/concepts/alias#tab-panel-520) ([local](./alias.md#tab-panel-520))
  * [ validate_by_alias and validate_by_name ](https://pydantic.dev/docs/validation/latest/concepts/alias#tab-panel-521) ([local](./alias.md#tab-panel-521))

```
 
    from pydantic import BaseModel, Field
    
    
    class Model(BaseModel):
      my_field: str = Field(validation_alias='my_alias')
    
    
    m = Model.model_validate(
      {'my_alias': 'foo'},  # (1)
      by_alias=True,
      by_name=False,
    )
    print(repr(m))
    #> Model(my_field='foo')

```

```
 
    from pydantic import BaseModel, Field
    
    
    class Model(BaseModel):
      my_field: str = Field(validation_alias='my_alias')
    
    
    m = Model.model_validate(
      {'my_field': 'foo'}, by_alias=False, by_name=True  # (1)
    )
    print(repr(m))
    #> Model(my_field='foo')

```

```
 
    from pydantic import BaseModel, Field
    
    
    class Model(BaseModel):
      my_field: str = Field(validation_alias='my_alias')
    
    
    m = Model.model_validate(
      {'my_alias': 'foo'}, by_alias=True, by_name=True  # (1)
    )
    print(repr(m))
    #> Model(my_field='foo')
    
    m = Model.model_validate(
      {'my_field': 'foo'}, by_alias=True, by_name=True  # (2)
    )
    print(repr(m))
    #> Model(my_field='foo')

```

Caution

You cannot set both `by_alias` and `by_name` to `False`. A [user error](https://pydantic.dev/docs/validation/latest/errors/usage_errors#validate-by-alias-and-name-false) ([local](./../errors/usage_errors.md#validate-by-alias-and-name-false)) is raised in this case.

#### Serialization

<https://pydantic.dev/docs/validation/latest/concepts/alias#serialization-1> ([local](./alias.md#serialization-1)) ([local](./alias.md#serialization-1))

When serializing data, you can enable serialization by alias via the `by_alias` flag which is available on the [`model_dump()`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_dump) ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_dump)) and [`model_dump_json()`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_dump_json) ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_dump_json)) methods, as well as the [`TypeAdapter`](https://pydantic.dev/docs/validation/latest/api/pydantic/type_adapter/#pydantic.type_adapter.TypeAdapter) ([local](./../api/pydantic/type_adapter.md#pydantic.type_adapter.TypeAdapter)) ones.

By default, `by_alias` is `False`.

```
 
    from pydantic import BaseModel, Field
    
    
    class Model(BaseModel):
      my_field: str = Field(serialization_alias='my_alias')
    
    
    m = Model(my_field='foo')
    print(m.model_dump(by_alias=True))  # (1)
    #> {'my_alias': 'foo'}

```

Note

The fact that serialization by alias is disabled by default is notably inconsistent with the default for validation (where aliases are used by default). We anticipate changing this default in V3.
