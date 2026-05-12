---
title: Color
source: https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color
---

Color definitions are used as per the CSS3 [CSS Color Module Level 3](<http://www.w3.org/TR/css3-color/#svg-color>) specification.

A few colors have multiple names referring to the same colors, e.g. `grey` and `gray` or `aqua` and `cyan`.

In these cases the _last_ color when sorted alphabetically takes precedence. eg. `Color((0, 255, 255)).as_named() == 'cyan'` because “cyan” comes after “aqua”.

## RGBA 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.RGBA> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.RGBA)))

Internal use only as a representation of a color.

## Color 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color)))

**Bases:** `Representation`

Represents a color.

### Methods

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#methods> ([local](./pydantic_extra_types_color.md#methods)))

#### original 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.original> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.original)))

```
 
    def original() -> ColorType
    

```

Original value passed to `Color`.

##### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns> ([local](./pydantic_extra_types_color.md#returns)))

`ColorType`

#### as_named 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_named> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_named)))

```
 
    def as_named(fallback: bool = False) -> str
    

```

Returns the name of the color if it can be found in `COLORS_BY_VALUE` dictionary, otherwise returns the hexadecimal representation of the color or raises `ValueError`.

##### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-1> ([local](./pydantic_extra_types_color.md#returns-1)))

[`str`](<https://docs.python.org/3/library/stdtypes.html#str>) — The name of the color, or the hexadecimal representation of the color.

##### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters> ([local](./pydantic_extra_types_color.md#parameters)))

**`fallback`** : [`bool`](<https://docs.python.org/3/library/functions.html#bool>) _Default:_ `False`

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_named\(fallback\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_named\(fallback\))))

If True, falls back to returning the hexadecimal representation of the color instead of raising a ValueError when no named color is found.

##### Raises

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#raises> ([local](./pydantic_extra_types_color.md#raises)))

  * `ValueError` — When no named color is found and fallback is `False`.

#### as_hex 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_hex> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_hex)))

```
 
    def as_hex(format: Literal['short', 'long'] = 'short') -> str
    

```

Returns the hexadecimal representation of the color.

Hex string representing the color can be 3, 4, 6, or 8 characters depending on whether the string a “short” representation of the color is possible and whether there’s an alpha channel.

##### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-2> ([local](./pydantic_extra_types_color.md#returns-2)))

[`str`](<https://docs.python.org/3/library/stdtypes.html#str>) — The hexadecimal representation of the color.

#### as_rgb 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_rgb> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_rgb)))

```
 
    def as_rgb() -> str
    

```

Color as an `rgb(<r>, <g>, <b>)` or `rgba(<r>, <g>, <b>, <a>)` string.

##### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-3> ([local](./pydantic_extra_types_color.md#returns-3)))

[`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

#### as_rgb_tuple 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_rgb_tuple> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_rgb_tuple)))

```
 
    def as_rgb_tuple(alpha: bool | None = None) -> ColorTuple
    

```

Returns the color as an RGB or RGBA tuple.

##### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-4> ([local](./pydantic_extra_types_color.md#returns-4)))

`ColorTuple` — A tuple that contains the values of the red, green, and blue channels in the range 0 to 255. If alpha is included, it is in the range 0 to 1.

##### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-1> ([local](./pydantic_extra_types_color.md#parameters-1)))

**`alpha`** : [`bool`](<https://docs.python.org/3/library/functions.html#bool>) | [`None`](<https://docs.python.org/3/library/constants.html#None>) _Default:_ `None`

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_rgb_tuple\(alpha\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_rgb_tuple\(alpha\))))

Whether to include the alpha channel. There are three options for this input:

  * `None` (default): Include alpha only if it’s set. (e.g. not `None`)
  * `True`: Always include alpha.
  * `False`: Always omit alpha.

#### as_hsl 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_hsl> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_hsl)))

```
 
    def as_hsl() -> str
    

```

Color as an `hsl(<h>, <s>, <l>)` or `hsl(<h>, <s>, <l>, <a>)` string.

##### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-5> ([local](./pydantic_extra_types_color.md#returns-5)))

[`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

#### as_hsl_tuple 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_hsl_tuple> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_hsl_tuple)))

```
 
    def as_hsl_tuple(alpha: bool | None = None) -> HslColorTuple
    

```

Returns the color as an HSL or HSLA tuple.

##### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-6> ([local](./pydantic_extra_types_color.md#returns-6)))

`HslColorTuple` — The color as a tuple of hue, saturation, lightness, and alpha (if included). All elements are in the range 0 to 1.

##### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-2> ([local](./pydantic_extra_types_color.md#parameters-2)))

**`alpha`** : [`bool`](<https://docs.python.org/3/library/functions.html#bool>) | [`None`](<https://docs.python.org/3/library/constants.html#None>) _Default:_ `None`

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.Color.as_hsl_tuple\(alpha\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.Color.as_hsl_tuple\(alpha\))))

Whether to include the alpha channel.

  * `None` (default): Include the alpha channel only if it’s set (e.g. not `None`).
  * `True`: Always include alpha.
  * `False`: Always omit alpha.

## parse_tuple 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_tuple> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_tuple)))

```
 
    def parse_tuple(value: tuple[Any, ...]) -> RGBA
    

```

Parse a tuple or list to get RGBA values.

### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-7> ([local](./pydantic_extra_types_color.md#returns-7)))

`RGBA` — An `RGBA` tuple parsed from the input tuple.

### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-3> ([local](./pydantic_extra_types_color.md#parameters-3)))

**`value`** : [`tuple`](<https://docs.python.org/3/library/stdtypes.html#tuple>)[[`Any`](<https://docs.python.org/3/library/typing.html#typing.Any>), …] 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_tuple\(value\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_tuple\(value\))))

A tuple or list.

### Raises

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#raises-1> ([local](./pydantic_extra_types_color.md#raises-1)))

  * `PydanticCustomError` — If tuple is not valid.

## parse_str 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_str> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_str)))

```
 
    def parse_str(value: str) -> RGBA
    

```

Parse a string representing a color to an RGBA tuple.

Possible formats for the input string include:

  * named color, see `COLORS_BY_NAME`
  * hex short eg. `<prefix>fff` (prefix can be `#`, `0x` or nothing)
  * hex long eg. `<prefix>ffffff` (prefix can be `#`, `0x` or nothing)
  * `rgb(<r>, <g>, <b>)`
  * `rgba(<r>, <g>, <b>, <a>)`
  * `transparent`

### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-8> ([local](./pydantic_extra_types_color.md#returns-8)))

`RGBA` — An `RGBA` tuple parsed from the input string.

### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-4> ([local](./pydantic_extra_types_color.md#parameters-4)))

**`value`** : [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_str\(value\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_str\(value\))))

A string representing a color.

### Raises

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#raises-2> ([local](./pydantic_extra_types_color.md#raises-2)))

  * `ValueError` — If the input string cannot be parsed to an RGBA tuple.

## ints_to_rgba 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.ints_to_rgba> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.ints_to_rgba)))

```
 
    def ints_to_rgba(
        r: int | str,
        g: int | str,
        b: int | str,
        alpha: float | None = None,
    ) -> RGBA
    

```

Converts integer or string values for RGB color and an optional alpha value to an `RGBA` object.

### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-9> ([local](./pydantic_extra_types_color.md#returns-9)))

`RGBA` — An instance of the `RGBA` class with the corresponding color and alpha values.

### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-5> ([local](./pydantic_extra_types_color.md#parameters-5)))

**`r`** : [`int`](<https://docs.python.org/3/library/functions.html#int>) | [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.ints_to_rgba\(r\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.ints_to_rgba\(r\))))

An integer or string representing the red color value.

**`g`** : [`int`](<https://docs.python.org/3/library/functions.html#int>) | [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.ints_to_rgba\(g\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.ints_to_rgba\(g\))))

An integer or string representing the green color value.

**`b`** : [`int`](<https://docs.python.org/3/library/functions.html#int>) | [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.ints_to_rgba\(b\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.ints_to_rgba\(b\))))

An integer or string representing the blue color value.

**`alpha`** : [`float`](<https://docs.python.org/3/library/functions.html#float>) | [`None`](<https://docs.python.org/3/library/constants.html#None>) _Default:_ `None`

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.ints_to_rgba\(alpha\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.ints_to_rgba\(alpha\))))

A float representing the alpha value. Defaults to None.

## parse_color_value 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_color_value> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_color_value)))

```
 
    def parse_color_value(value: int | str, max_val: int = 255) -> float
    

```

Parse the color value provided and return a number between 0 and 1.

### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-10> ([local](./pydantic_extra_types_color.md#returns-10)))

[`float`](<https://docs.python.org/3/library/functions.html#float>) — A number between 0 and 1.

### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-6> ([local](./pydantic_extra_types_color.md#parameters-6)))

**`value`** : [`int`](<https://docs.python.org/3/library/functions.html#int>) | [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_color_value\(value\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_color_value\(value\))))

An integer or string color value.

**`max_val`** : [`int`](<https://docs.python.org/3/library/functions.html#int>) _Default:_ `255`

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_color_value\(max_val\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_color_value\(max_val\))))

Maximum range value. Defaults to 255.

### Raises

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#raises-3> ([local](./pydantic_extra_types_color.md#raises-3)))

  * `PydanticCustomError` — If the value is not a valid color.

## parse_float_alpha 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_float_alpha> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_float_alpha)))

```
 
    def parse_float_alpha(value: None | str | float | int) -> float | None
    

```

Parse an alpha value checking it’s a valid float in the range 0 to 1.

### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-11> ([local](./pydantic_extra_types_color.md#returns-11)))

[`float`](<https://docs.python.org/3/library/functions.html#float>) | [`None`](<https://docs.python.org/3/library/constants.html#None>) — The parsed value as a float, or `None` if the value was None or equal 1.

### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-7> ([local](./pydantic_extra_types_color.md#parameters-7)))

**`value`** : [`None`](<https://docs.python.org/3/library/constants.html#None>) | [`str`](<https://docs.python.org/3/library/stdtypes.html#str>) | [`float`](<https://docs.python.org/3/library/functions.html#float>) | [`int`](<https://docs.python.org/3/library/functions.html#int>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_float_alpha\(value\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_float_alpha\(value\))))

The input value to parse.

### Raises

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#raises-4> ([local](./pydantic_extra_types_color.md#raises-4)))

  * `PydanticCustomError` — If the input value cannot be successfully parsed as a float in the expected range.

## parse_hsl 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_hsl> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_hsl)))

```
 
    def parse_hsl(
        h: str,
        h_units: str,
        sat: str,
        light: str,
        alpha: float | None = None,
    ) -> RGBA
    

```

Parse raw hue, saturation, lightness, and alpha values and convert to RGBA.

### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-12> ([local](./pydantic_extra_types_color.md#returns-12)))

`RGBA` — An instance of `RGBA`.

### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-8> ([local](./pydantic_extra_types_color.md#parameters-8)))

**`h`** : [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_hsl\(h\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_hsl\(h\))))

The hue value.

**`h_units`** : [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_hsl\(h_units\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_hsl\(h_units\))))

The unit for hue value.

**`sat`** : [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_hsl\(sat\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_hsl\(sat\))))

The saturation value.

**`light`** : [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_hsl\(light\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_hsl\(light\))))

The lightness value.

**`alpha`** : [`float`](<https://docs.python.org/3/library/functions.html#float>) | [`None`](<https://docs.python.org/3/library/constants.html#None>) _Default:_ `None`

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.parse_hsl\(alpha\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.parse_hsl\(alpha\))))

Alpha value.

## float_to_255 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.float_to_255> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.float_to_255)))

```
 
    def float_to_255(c: float) -> int
    

```

Converts a float value between 0 and 1 (inclusive) to an integer between 0 and 255 (inclusive).

### Returns

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#returns-13> ([local](./pydantic_extra_types_color.md#returns-13)))

[`int`](<https://docs.python.org/3/library/functions.html#int>) — The integer equivalent of the given float value rounded to the nearest whole number.

### Parameters

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#parameters-9> ([local](./pydantic_extra_types_color.md#parameters-9)))

**`c`** : [`float`](<https://docs.python.org/3/library/functions.html#float>)

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_color#pydantic_extra_types.color.float_to_255\(c\)> ([local](./pydantic_extra_types_color.md#pydantic_extra_types.color.float_to_255\(c\))))

The float value to be converted. Must be between 0 and 1 (inclusive).
