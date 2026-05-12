---
title: RootModel
source: https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/
---

RootModel class and type definitions.

## RootModel 

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel> ([local](./root_model.md#pydantic.root_model.RootModel)) ([local](./root_model.md#pydantic.root_model.RootModel))

**Bases:** [`BaseModel`](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel) ([local](./base_model.md#pydantic.BaseModel)), `Generic[RootModelRootType]`

Usage Documentation

[`RootModel` and Custom Root Types](https://pydantic.dev/docs/validation/latest/concepts/models#rootmodel-and-custom-root-types) ([local](./../../concepts/models.md#rootmodel-and-custom-root-types))

A Pydantic `BaseModel` for the root object of the model.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#attributes> ([local](./root_model.md#attributes)) ([local](./root_model.md#attributes))

#### root 

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel.root> ([local](./root_model.md#pydantic.root_model.RootModel.root)) ([local](./root_model.md#pydantic.root_model.RootModel.root))

The root object of the model.

**Type:** `RootModelRootType`

#### __pydantic_root_model__ 

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel.__pydantic_root_model__> ([local](./root_model.md#pydantic.root_model.RootModel.__pydantic_root_model__)) ([local](./root_model.md#pydantic.root_model.RootModel.__pydantic_root_model__))

Whether the model is a RootModel.

#### __pydantic_private__ 

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel.__pydantic_private__> ([local](./root_model.md#pydantic.root_model.RootModel.__pydantic_private__)) ([local](./root_model.md#pydantic.root_model.RootModel.__pydantic_private__))

Private fields in the model.

#### __pydantic_extra__ 

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel.__pydantic_extra__> ([local](./root_model.md#pydantic.root_model.RootModel.__pydantic_extra__)) ([local](./root_model.md#pydantic.root_model.RootModel.__pydantic_extra__))

Extra fields in the model.

### Methods

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#methods> ([local](./root_model.md#methods)) ([local](./root_model.md#methods))

#### model_construct 

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel.model_construct> ([local](./root_model.md#pydantic.root_model.RootModel.model_construct)) ([local](./root_model.md#pydantic.root_model.RootModel.model_construct))

`@classmethod`

```
 
    def model_construct(
        cls,
        root: RootModelRootType,
        _fields_set: set[str] | None = None,
    ) -> Self
    

```

Create a new model using the provided root object and update fields set.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#returns> ([local](./root_model.md#returns)) ([local](./root_model.md#returns))

[`Self`](https://docs.python.org/3/library/typing.html#typing.Self) — The new model.

##### Parameters

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#parameters> ([local](./root_model.md#parameters)) ([local](./root_model.md#parameters))

**`root`** : `RootModelRootType`

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel.model_construct\(root\> ([local](./root_model.md#pydantic.root_model.RootModel.model_construct\(root\)) ([local](./root_model.md#pydantic.root_model.RootModel.model_construct\(root\)))

The root object of the model.

**`_fields_set`** : [`set`](https://docs.python.org/3/reference/expressions.html#set)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)] | [`None`](https://docs.python.org/3/library/constants.html#None) _Default:_ `None`

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel.model_construct\(_fields_set\> ([local](./root_model.md#pydantic.root_model.RootModel.model_construct\(_fields_set\)) ([local](./root_model.md#pydantic.root_model.RootModel.model_construct\(_fields_set\)))

The set of fields to be updated.

##### Raises

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#raises> ([local](./root_model.md#raises)) ([local](./root_model.md#raises))

  * `NotImplemented` — If the model is not a subclass of `RootModel`.

#### model_dump 

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#pydantic.root_model.RootModel.model_dump> ([local](./root_model.md#pydantic.root_model.RootModel.model_dump)) ([local](./root_model.md#pydantic.root_model.RootModel.model_dump))

```
 
    def model_dump(
        mode: Literal['json', 'python'] | str = 'python',
        include: Any = None,
        exclude: Any = None,
        context: dict[str, Any] | None = None,
        by_alias: bool | None = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        exclude_computed_fields: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal['none', 'warn', 'error'] = True,
        serialize_as_any: bool = False,
    ) -> Any
    

```

This method is included just to get a more accurate return type for type checkers. It is included in this `if TYPE_CHECKING:` block since no override is actually necessary.

See the documentation of `BaseModel.model_dump` for more details about the arguments.

Generally, this method will have a return type of `RootModelRootType`, assuming that `RootModelRootType` is not a `BaseModel` subclass. If `RootModelRootType` is a `BaseModel` subclass, then the return type will likely be `dict[str, Any]`, as `model_dump` calls are recursive. The return type could even be something different, in the case of a custom serializer. Thus, `Any` is used here to catch all of these cases.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/root_model/#returns-1> ([local](./root_model.md#returns-1)) ([local](./root_model.md#returns-1))

[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)
