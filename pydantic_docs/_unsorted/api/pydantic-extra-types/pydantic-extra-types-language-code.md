---
title: Language
source: https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_language_code/
---

Language definitions that are based on the [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) & [ISO 639-5](https://en.wikipedia.org/wiki/ISO_639-5).

## LanguageInfo 

#pydantic_extra_types.language_code.LanguageInfo

LanguageInfo is a dataclass that contains the language information.

### Constructor Parameters

#constructor-parameters

**`alpha2`** : [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`None`](https://docs.python.org/3/library/constants.html#None)] 

#pydantic_extra_types.language_code.LanguageInfo.__init__\(alpha2\)

The language code in the [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/ISO_639-1) format.

**`alpha3`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

#pydantic_extra_types.language_code.LanguageInfo.__init__\(alpha3\)

The language code in the [ISO 639-3 alpha-3](https://en.wikipedia.org/wiki/ISO_639-3) format.

**`name`** : [`str`](https://docs.python.org/3/library/stdtypes.html#str)

#pydantic_extra_types.language_code.LanguageInfo.__init__\(name\)

The language name.

## LanguageAlpha2 

#pydantic_extra_types.language_code.LanguageAlpha2

**Bases:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

LanguageAlpha2 parses languages codes in the [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/ISO_639-1) format.

```
 
    from pydantic import BaseModel
    
    from pydantic_extra_types.language_code import LanguageAlpha2
    
    
    class Movie(BaseModel):
        audio_lang: LanguageAlpha2
        subtitles_lang: LanguageAlpha2
    
    
    movie = Movie(audio_lang='de', subtitles_lang='fr')
    print(movie)
    # > audio_lang='de' subtitles_lang='fr'
    

```

### Attributes

#attributes

#### alpha3 

#pydantic_extra_types.language_code.LanguageAlpha2.alpha3

The language code in the [ISO 639-3 alpha-3](https://en.wikipedia.org/wiki/ISO_639-3) format.

**Type:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

#### name 

#pydantic_extra_types.language_code.LanguageAlpha2.name

The language name.

**Type:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

## LanguageName 

#pydantic_extra_types.language_code.LanguageName

**Bases:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

LanguageName parses languages names listed in the [ISO 639-3 standard](https://en.wikipedia.org/wiki/ISO_639-3) format.

```
 
    from pydantic import BaseModel
    
    from pydantic_extra_types.language_code import LanguageName
    
    
    class Movie(BaseModel):
        audio_lang: LanguageName
        subtitles_lang: LanguageName
    
    
    movie = Movie(audio_lang='Dutch', subtitles_lang='Mandarin Chinese')
    print(movie)
    # > audio_lang='Dutch' subtitles_lang='Mandarin Chinese'
    

```

### Attributes

#attributes-1

#### alpha2 

#pydantic_extra_types.language_code.LanguageName.alpha2

The language code in the [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/ISO_639-1) format. Does not exist for all languages.

**Type:** [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`None`](https://docs.python.org/3/library/constants.html#None)]

#### alpha3 

#pydantic_extra_types.language_code.LanguageName.alpha3

The language code in the [ISO 639-3 alpha-3](https://en.wikipedia.org/wiki/ISO_639-3) format.

**Type:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

## ISO639_3 

#pydantic_extra_types.language_code.ISO639_3

**Bases:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

ISO639_3 parses Language in the [ISO 639-3 alpha-3](https://en.wikipedia.org/wiki/ISO_639-3_alpha-3) format.

```
 
    from pydantic import BaseModel
    
    from pydantic_extra_types.language_code import ISO639_3
    
    
    class Language(BaseModel):
        alpha_3: ISO639_3
    
    
    lang = Language(alpha_3='ssr')
    print(lang)
    # > alpha_3='ssr'
    

```

## ISO639_5 

#pydantic_extra_types.language_code.ISO639_5

**Bases:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

ISO639_5 parses Language in the [ISO 639-5 alpha-3](https://en.wikipedia.org/wiki/ISO_639-5_alpha-3) format.

```
 
    from pydantic import BaseModel
    
    from pydantic_extra_types.language_code import ISO639_5
    
    
    class Language(BaseModel):
        alpha_3: ISO639_5
    
    
    lang = Language(alpha_3='gem')
    print(lang)
    # > alpha_3='gem'
    

```
