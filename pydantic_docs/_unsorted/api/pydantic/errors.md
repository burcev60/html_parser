---
title: Errors
source: https://pydantic.dev/docs/validation/latest/api/pydantic/errors/
---

Pydantic-specific errors.

## PydanticErrorMixin 

#pydantic.errors.PydanticErrorMixin

A mixin class for common functionality shared by all Pydantic-specific errors.

### Attributes

#attributes

#### message 

#pydantic.errors.PydanticErrorMixin.message

A message describing the error.

#### code 

#pydantic.errors.PydanticErrorMixin.code

An optional error code from PydanticErrorCodes enum.

## PydanticUserError 

#pydantic.errors.PydanticUserError

**Bases:** `PydanticErrorMixin`, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError)

An error raised due to incorrect use of Pydantic.

## PydanticUndefinedAnnotation 

#pydantic.errors.PydanticUndefinedAnnotation

**Bases:** `PydanticErrorMixin`, [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError)

A subclass of `NameError` raised when handling undefined annotations during `CoreSchema` generation.

### Attributes

#attributes-1

#### name 

#pydantic.errors.PydanticUndefinedAnnotation.name

Name of the error.

#### message 

#pydantic.errors.PydanticUndefinedAnnotation.message

Description of the error.

### Methods

#methods

#### from_name_error 

#pydantic.errors.PydanticUndefinedAnnotation.from_name_error

`@classmethod`

```
 
    def from_name_error(cls, name_error: NameError) -> Self
    

```

Convert a `NameError` to a `PydanticUndefinedAnnotation` error.

##### Returns

#returns

[`Self`](https://docs.python.org/3/library/typing.html#typing.Self) — Converted `PydanticUndefinedAnnotation` error.

##### Parameters

#parameters

**`name_error`** : [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError)

#pydantic.errors.PydanticUndefinedAnnotation.from_name_error\(name_error\)

`NameError` to be converted.

## PydanticImportError 

#pydantic.errors.PydanticImportError

**Bases:** `PydanticErrorMixin`, [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError)

An error raised when an import fails due to module changes between V1 and V2.

### Attributes

#attributes-2

#### message 

#pydantic.errors.PydanticImportError.message

Description of the error.

## PydanticSchemaGenerationError 

#pydantic.errors.PydanticSchemaGenerationError

**Bases:** [`PydanticUserError`](#pydantic.errors.PydanticUserError)

An error raised during failures to generate a `CoreSchema` for some type.

### Attributes

#attributes-3

#### message 

#pydantic.errors.PydanticSchemaGenerationError.message

Description of the error.

## PydanticInvalidForJsonSchema 

#pydantic.errors.PydanticInvalidForJsonSchema

**Bases:** [`PydanticUserError`](#pydantic.errors.PydanticUserError)

An error raised during failures to generate a JSON schema for some `CoreSchema`.

### Attributes

#attributes-4

#### message 

#pydantic.errors.PydanticInvalidForJsonSchema.message

Description of the error.

## PydanticForbiddenQualifier 

#pydantic.errors.PydanticForbiddenQualifier

**Bases:** [`PydanticUserError`](#pydantic.errors.PydanticUserError)

An error raised if a forbidden type qualifier is found in a type annotation.
