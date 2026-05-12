---
title: Dynamic models
source: https://pydantic.dev/docs/validation/latest/examples/dynamic_models
---

Models can be [created dynamically](<https://pydantic.dev/docs/validation/latest/concepts/models#dynamic-model-creation> ([local](./../concepts/models.md#dynamic-model-creation))) using the [`create_model()`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.create_model> ([local](./../api/pydantic/base_model.md#pydantic.create_model))) factory function.

In this example, we will show how to dynamically derive a model from an existing one, making every field optional. To achieve this, we will make use of the [`model_fields`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_fields> ([local](./../api/pydantic/base_model.md#pydantic.BaseModel.model_fields))) model class attribute, and derive new annotations from the field definitions to be passed to the [`create_model()`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.create_model> ([local](./../api/pydantic/base_model.md#pydantic.create_model))) factory. Of course, this example can apply to any use case where you need to derive a new model from another (remove default values, add aliases, etc).

  * [ Python 3.9 ](<https://pydantic.dev/docs/validation/latest/examples/dynamic_models#tab-panel-553> ([local](./dynamic_models.md#tab-panel-553)))
  * [ Python 3.10 ](<https://pydantic.dev/docs/validation/latest/examples/dynamic_models#tab-panel-554> ([local](./dynamic_models.md#tab-panel-554)))
  * [ Python 3.11 and above ](<https://pydantic.dev/docs/validation/latest/examples/dynamic_models#tab-panel-555> ([local](./dynamic_models.md#tab-panel-555)))

```
 
    from typing import Annotated, Union
    
    from pydantic import BaseModel, Field, create_model
    
    
    def make_fields_optional(model_cls: type[BaseModel]) -> type[BaseModel]:
      new_fields = {}
    
      for f_name, f_info in model_cls.model_fields.items():
          f_dct = f_info.asdict()
          new_fields[f_name] = (
              Annotated[(Union[f_dct['annotation'], None], *f_dct['metadata'], Field(**f_dct['attributes']))],
              None,
          )
    
      return create_model(
          f'{model_cls.__name__}Optional',
          __base__=model_cls,  # (1)
          **new_fields,
      )

```

The parent fields are overridden by the ones we define.

```
 
    from typing import Annotated
    
    from pydantic import BaseModel, Field, create_model
    
    
    def make_fields_optional(model_cls: type[BaseModel]) -> type[BaseModel]:
      new_fields = {}
    
      for f_name, f_info in model_cls.model_fields.items():
          f_dct = f_info.asdict()
          new_fields[f_name] = (
              Annotated[(f_dct['annotation'] | None, *f_dct['metadata'], Field(**f_dct['attributes']))],
              None,
          )
    
      return create_model(
          f'{model_cls.__name__}Optional',
          __base__=model_cls,  # (1)
          **new_fields,
      )

```

The parent fields are overridden by the ones we define.

```
 
    from typing import Annotated
    
    from pydantic import BaseModel, Field, create_model
    
    
    def make_fields_optional(model_cls: type[BaseModel]) -> type[BaseModel]:
      new_fields = {}
    
      for f_name, f_info in model_cls.model_fields.items():
          f_dct = f_info.asdict()
          new_fields[f_name] = (
              Annotated[f_dct['annotation'] | None, *f_dct['metadata'], Field(**f_dct['attributes'])],
              None,
          )
    
      return create_model(
          f'{model_cls.__name__}Optional',
          __base__=model_cls,  # (1)
          **new_fields,
      )

```

The parent fields are overridden by the ones we define.

For each field, we generate a dictionary representation of the [`FieldInfo`](<https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.FieldInfo> ([local](./../api/pydantic/fields.md#pydantic.fields.FieldInfo))) instance using the [`asdict()`](<https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.FieldInfo.asdict> ([local](./../api/pydantic/fields.md#pydantic.fields.FieldInfo.asdict))) method, containing the annotation, metadata and attributes.

With the following model:

```
 
    class Model(BaseModel):
        f: Annotated[int, Field(gt=1), WithJsonSchema({'extra': 'data'}), Field(title='F')] = 1
    

```

The [`FieldInfo`](<https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.FieldInfo> ([local](./../api/pydantic/fields.md#pydantic.fields.FieldInfo))) instance of `f` will have three items in its dictionary representation:

  * `annotation`: `int`.
  * `metadata`: A list containing the type-specific constraints and other metadata: `[Gt(1), WithJsonSchema({'extra': 'data'})]`.
  * `attributes`: The remaining field-specific attributes: `{'title': 'F'}`.

With that in mind, we can recreate an annotation that “simulates” the one from the original model:

  * [ Python 3.9 and above ](<https://pydantic.dev/docs/validation/latest/examples/dynamic_models#tab-panel-551> ([local](./dynamic_models.md#tab-panel-551)))
  * [ Python 3.11 and above ](<https://pydantic.dev/docs/validation/latest/examples/dynamic_models#tab-panel-552> ([local](./dynamic_models.md#tab-panel-552)))

```
 
    new_annotation = Annotated[(
      f_dct['annotation'] | None,  # (1)
      *f_dct['metadata'],  # (2)
      Field(**f_dct['attributes']),  # (3)
    )]

```

```
 
    new_annotation = Annotated[
      f_dct['annotation'] | None,  # (1)
      *f_dct['metadata'],  # (2)
      Field(**f_dct['attributes']),  # (3)
    ]

```

and specify `None` as a default value (the second element of the tuple for the field definition accepted by [`create_model()`](<https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.create_model> ([local](./../api/pydantic/base_model.md#pydantic.create_model)))).

Here is a demonstration of our factory function:

```
 
    from pydantic import BaseModel, Field
    
    
    class Model(BaseModel):
        a: Annotated[int, Field(gt=1)]
    
    
    ModelOptional = make_fields_optional(Model)
    
    m = ModelOptional()
    print(m.a)
    #> None
    

```

A couple notes on the implementation:

  * Our `make_fields_optional()` function is defined as returning an arbitrary Pydantic model class (`-> type[BaseModel]`). An alternative solution can be to use a type variable to preserve the input class:

  * [ Python 3.9 and above ](<https://pydantic.dev/docs/validation/latest/examples/dynamic_models#tab-panel-549> ([local](./dynamic_models.md#tab-panel-549)))
  * [ Python 3.12 and above ](<https://pydantic.dev/docs/validation/latest/examples/dynamic_models#tab-panel-550> ([local](./dynamic_models.md#tab-panel-550)))

```
 
    ModelTypeT = TypeVar('ModelTypeT', bound=type[BaseModel])
    
    def make_fields_optional(model_cls: ModelTypeT) -> ModelTypeT:
        ...
    

```

```
 
    def make_fields_optional[ModelTypeT: type[BaseModel]](model_cls: ModelTypeT) -> ModelTypeT:
        ...
    

```

However, note that static type checkers _won’t_ be able to understand that all fields are now optional.

  * The experimental [`MISSING` sentinel](<https://pydantic.dev/docs/validation/latest/concepts/experimental#missing-sentinel> ([local](./../concepts/experimental.md#missing-sentinel))) can be used as an alternative to `None` for the default values. Simply replace `None` by `MISSING` in the new annotation and default value.

  * You might be tempted to make a copy of the original [`FieldInfo`](<https://pydantic.dev/docs/validation/latest/api/pydantic/fields/#pydantic.fields.FieldInfo> ([local](./../api/pydantic/fields.md#pydantic.fields.FieldInfo))) instances, add a default and/or perform other mutations, to then reuse it as [`Annotated`](<https://docs.python.org/3/library/typing.html#typing.Annotated>) metadata. While this may work in some cases, it is **not** a supported pattern, and could break or be deprecated at any point. We strongly encourage using the pattern from this example instead.
