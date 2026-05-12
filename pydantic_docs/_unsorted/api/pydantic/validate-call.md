---
title: Validate Call
source: https://pydantic.dev/docs/validation/latest/api/pydantic/validate_call/
---

Decorator for validating function calls.

## validate_call 

#pydantic.validate_call_decorator.validate_call

```
 
    def validate_call(
        config: ConfigDict | None = None,
        validate_return: bool = False,
    ) -> Callable[[AnyCallableT], AnyCallableT]
    def validate_call(func: AnyCallableT) -> AnyCallableT
    

```

Usage Documentation

[Validation Decorator](https://pydantic.dev/docs/validation/latest/concepts/validation_decorator) ([local](./../../concepts/validation-decorator.md))

Returns a decorated wrapper around the function that validates the arguments and, optionally, the return value.

Usage may be either as a plain decorator `@validate_call` or with arguments `@validate_call(...)`.

### Returns

#returns

`AnyCallableT` | [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`AnyCallableT`], `AnyCallableT`] — The decorated function.

### Parameters

#parameters

**`func`** : `AnyCallableT` | [`None`](https://docs.python.org/3/library/constants.html#None) _Default:_ `None`

#pydantic.validate_call_decorator.validate_call\(func\)

The function to be decorated.

**`config`** : [`ConfigDict`](https://pydantic.dev/docs/validation/latest/api/pydantic/config/#pydantic.config.ConfigDict) ([local](./config.md#pydantic.config.ConfigDict)) | [`None`](https://docs.python.org/3/library/constants.html#None) _Default:_ `None`

#pydantic.validate_call_decorator.validate_call\(config\)

The configuration dictionary.

**`validate_return`** : [`bool`](https://docs.python.org/3/library/functions.html#bool) _Default:_ `False`

#pydantic.validate_call_decorator.validate_call\(validate_return\)

Whether to validate the return value.
