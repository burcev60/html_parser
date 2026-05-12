---
title: Script Code
source: https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_script_code/
---

# Script Code

script definitions that are based on the [ISO 15924](<https://en.wikipedia.org/wiki/ISO_15924>)

## ISO_15924 

[](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_script_code/#pydantic_extra_types.script_code.ISO_15924>)

**Bases:** [`str`](<https://docs.python.org/3/library/stdtypes.html#str>)

ISO_15924 parses script in the [ISO 15924](<https://en.wikipedia.org/wiki/ISO_15924>) format.

```
 
    from pydantic import BaseModel
    
    from pydantic_extra_types.script_code import ISO_15924
    
    
    class Script(BaseModel):
        alpha_4: ISO_15924
    
    
    script = Script(alpha_4='Java')
    print(lang)
    # > script='Java'
    

```

Was this page helpful?

Thanks for your feedback!

[ Previous   
Language ](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_language_code/>) [ Next   
Semantic Version ](<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_semantic_version/>)
