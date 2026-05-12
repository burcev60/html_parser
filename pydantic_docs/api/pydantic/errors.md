---
title: Errors
source: https://pydantic.dev/docs/validation/latest/api/pydantic/errors/
---

Pydantic-specific errors.

## PydanticErrorMixin 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticErrorMixin> ([local](./errors.md#pydantic.errors.PydanticErrorMixin)) ([local](./errors.md#pydantic.errors.PydanticErrorMixin))

A mixin class for common functionality shared by all Pydantic-specific errors.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#attributes> ([local](./errors.md#attributes)) ([local](./errors.md#attributes))

#### message 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticErrorMixin.message> ([local](./errors.md#pydantic.errors.PydanticErrorMixin.message)) ([local](./errors.md#pydantic.errors.PydanticErrorMixin.message))

A message describing the error.

#### code 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticErrorMixin.code> ([local](./errors.md#pydantic.errors.PydanticErrorMixin.code)) ([local](./errors.md#pydantic.errors.PydanticErrorMixin.code))

An optional error code from PydanticErrorCodes enum.

## PydanticUserError 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUserError> ([local](./errors.md#pydantic.errors.PydanticUserError)) ([local](./errors.md#pydantic.errors.PydanticUserError))

**Bases:** `PydanticErrorMixin`, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError)

An error raised due to incorrect use of Pydantic.

## PydanticUndefinedAnnotation 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUndefinedAnnotation> ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation)) ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation))

**Bases:** `PydanticErrorMixin`, [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError)

A subclass of `NameError` raised when handling undefined annotations during `CoreSchema` generation.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#attributes-1> ([local](./errors.md#attributes-1)) ([local](./errors.md#attributes-1))

#### name 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUndefinedAnnotation.name> ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation.name)) ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation.name))

Name of the error.

#### message 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUndefinedAnnotation.message> ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation.message)) ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation.message))

Description of the error.

### Methods

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#methods> ([local](./errors.md#methods)) ([local](./errors.md#methods))

#### from_name_error 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUndefinedAnnotation.from_name_error> ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation.from_name_error)) ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation.from_name_error))

`@classmethod`

```
 
    def from_name_error(cls, name_error: NameError) -> Self
    

```

Convert a `NameError` to a `PydanticUndefinedAnnotation` error.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#returns> ([local](./errors.md#returns)) ([local](./errors.md#returns))

[`Self`](https://docs.python.org/3/library/typing.html#typing.Self) — Converted `PydanticUndefinedAnnotation` error.

##### Parameters

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#parameters> ([local](./errors.md#parameters)) ([local](./errors.md#parameters))

**`name_error`** : [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError)

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUndefinedAnnotation.from_name_error\(name_error\> ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation.from_name_error\(name_error\)) ([local](./errors.md#pydantic.errors.PydanticUndefinedAnnotation.from_name_error\(name_error\)))

`NameError` to be converted.

## PydanticImportError 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticImportError> ([local](./errors.md#pydantic.errors.PydanticImportError)) ([local](./errors.md#pydantic.errors.PydanticImportError))

**Bases:** `PydanticErrorMixin`, [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError)

An error raised when an import fails due to module changes between V1 and V2.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#attributes-2> ([local](./errors.md#attributes-2)) ([local](./errors.md#attributes-2))

#### message 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticImportError.message> ([local](./errors.md#pydantic.errors.PydanticImportError.message)) ([local](./errors.md#pydantic.errors.PydanticImportError.message))

Description of the error.

## PydanticSchemaGenerationError 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticSchemaGenerationError> ([local](./errors.md#pydantic.errors.PydanticSchemaGenerationError)) ([local](./errors.md#pydantic.errors.PydanticSchemaGenerationError))

**Bases:** [`PydanticUserError`](https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUserError) ([local](./errors.md#pydantic.errors.PydanticUserError))

An error raised during failures to generate a `CoreSchema` for some type.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#attributes-3> ([local](./errors.md#attributes-3)) ([local](./errors.md#attributes-3))

#### message 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticSchemaGenerationError.message> ([local](./errors.md#pydantic.errors.PydanticSchemaGenerationError.message)) ([local](./errors.md#pydantic.errors.PydanticSchemaGenerationError.message))

Description of the error.

## PydanticInvalidForJsonSchema 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticInvalidForJsonSchema> ([local](./errors.md#pydantic.errors.PydanticInvalidForJsonSchema)) ([local](./errors.md#pydantic.errors.PydanticInvalidForJsonSchema))

**Bases:** [`PydanticUserError`](https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUserError) ([local](./errors.md#pydantic.errors.PydanticUserError))

An error raised during failures to generate a JSON schema for some `CoreSchema`.

### Attributes

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#attributes-4> ([local](./errors.md#attributes-4)) ([local](./errors.md#attributes-4))

#### message 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticInvalidForJsonSchema.message> ([local](./errors.md#pydantic.errors.PydanticInvalidForJsonSchema.message)) ([local](./errors.md#pydantic.errors.PydanticInvalidForJsonSchema.message))

Description of the error.

## PydanticForbiddenQualifier 

<https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticForbiddenQualifier> ([local](./errors.md#pydantic.errors.PydanticForbiddenQualifier)) ([local](./errors.md#pydantic.errors.PydanticForbiddenQualifier))

**Bases:** [`PydanticUserError`](https://pydantic.dev/docs/validation/latest/api/pydantic/errors/#pydantic.errors.PydanticUserError) ([local](./errors.md#pydantic.errors.PydanticUserError))

An error raised if a forbidden type qualifier is found in a type annotation.
