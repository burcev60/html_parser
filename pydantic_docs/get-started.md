---
title: Welcome to Pydantic
source: https://pydantic.dev/docs/validation/latest/get-started/
---

[![CI](https://img.shields.io/github/actions/workflow/status/pydantic/pydantic/ci.yml?branch=main&logo=github&label=CI)](<https://github.com/pydantic/pydantic/actions?query=event%3Apush+branch%3Amain+workflow%3ACI>) [![Coverage](https://coverage-badge.samuelcolvin.workers.dev/pydantic/pydantic.svg)](<https://github.com/pydantic/pydantic/actions?query=event%3Apush+branch%3Amain+workflow%3ACI>)  
[![pypi](https://img.shields.io/pypi/v/pydantic.svg)](<https://pypi.python.org/pypi/pydantic>) [![CondaForge](https://img.shields.io/conda/v/conda-forge/pydantic.svg)](<https://anaconda.org/conda-forge/pydantic>) [![downloads](https://static.pepy.tech/badge/pydantic/month)](<https://pepy.tech/project/pydantic>)  
[![license](https://img.shields.io/github/license/pydantic/pydantic.svg)](<https://github.com/pydantic/pydantic/blob/main/LICENSE>) [![llms.txt](https://img.shields.io/badge/llms.txt-green)](<https://docs.pydantic.dev/latest/llms.txt>)

Documentation for version: v2.13.4.

Pydantic is the most widely used data validation library for Python.

Fast and extensible, Pydantic plays nicely with your linters/IDE/brain. Define how data should be in pure, canonical Python 3.9+; validate it with Pydantic.

**Sign up for our newsletter,_The Pydantic Stack_ , with updates & tutorials on Pydantic, Logfire, and Pydantic AI:**

Subscribe

## Why use Pydantic?

[](<https://pydantic.dev/docs/validation/latest/get-started/#why-use-pydantic> ([local](./get-started.md#why-use-pydantic)))

  * **Powered by type hints** — with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and integration with your IDE and static analysis tools. [Learn more…](<https://pydantic.dev/docs/validation/latest/get-started/why#type-hints> ([local](./get-started/why.md#type-hints)))
  * **Speed** — Pydantic’s core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python. [Learn more…](<https://pydantic.dev/docs/validation/latest/get-started/why#performance> ([local](./get-started/why.md#performance)))
  * **JSON Schema** — Pydantic models can emit JSON Schema, allowing for easy integration with other tools. [Learn more…](<https://pydantic.dev/docs/validation/latest/get-started/why#json-schema> ([local](./get-started/why.md#json-schema)))
  * **Strict** and **Lax** mode — Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate. [Learn more…](<https://pydantic.dev/docs/validation/latest/get-started/why#strict-lax> ([local](./get-started/why.md#strict-lax)))
  * **Dataclasses** , **TypedDicts** and more — Pydantic supports validation of many standard library types including `dataclass` and `TypedDict`. [Learn more…](<https://pydantic.dev/docs/validation/latest/get-started/why#dataclasses-typeddict-more> ([local](./get-started/why.md#dataclasses-typeddict-more)))
  * **Customisation** — Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways. [Learn more…](<https://pydantic.dev/docs/validation/latest/get-started/why#customisation> ([local](./get-started/why.md#customisation)))
  * **Ecosystem** — around 8,000 packages on PyPI use Pydantic, including massively popular libraries like _FastAPI_ , _huggingface_ , _Django Ninja_ , _SQLModel_ , & _LangChain_. [Learn more…](<https://pydantic.dev/docs/validation/latest/get-started/why#ecosystem> ([local](./get-started/why.md#ecosystem)))
  * **Battle tested** — Pydantic is downloaded over 550M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you’re trying to do something with Pydantic, someone else has probably already done it. [Learn more…](<https://pydantic.dev/docs/validation/latest/get-started/why#using-pydantic> ([local](./get-started/why.md#using-pydantic)))

[Installing Pydantic](<https://pydantic.dev/docs/validation/latest/get-started/install> ([local](./get-started/install.md))) is as simple as: `pip install pydantic`

## Pydantic examples

[](<https://pydantic.dev/docs/validation/latest/get-started/#pydantic-examples> ([local](./get-started.md#pydantic-examples)))

To see Pydantic at work, let’s start with a simple example, creating a custom class that inherits from `BaseModel`:

Validation Successful

```
 
    from datetime import datetime
    
    from pydantic import BaseModel, PositiveInt
    
    
    class User(BaseModel):
      id: int  # (1)
      name: str = 'John Doe'  # (2)
      signup_ts: datetime | None  # (3)
      tastes: dict[str, PositiveInt]  # (4)
    
    
    external_data = {
      'id': 123,
      'signup_ts': '2019-06-01 12:22',  # (5)
      'tastes': {
          'wine': 9,
          b'cheese': 7,  # (6)
          'cabbage': '1',  # (7)
      },
    }
    
    user = User(**external_data)  # (8)
    
    print(user.id)  # (9)
    #> 123
    print(user.model_dump())  # (10)
    """
    {
      'id': 123,
      'name': 'John Doe',
      'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
      'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
    }
    """

```

If validation fails, Pydantic will raise an error with a breakdown of what was wrong:

Validation Error

```
 
    # continuing the above example...
    
    from datetime import datetime
    from pydantic import BaseModel, PositiveInt, ValidationError
    
    
    class User(BaseModel):
      id: int
      name: str = 'John Doe'
      signup_ts: datetime | None
      tastes: dict[str, PositiveInt]
    
    
    external_data = {'id': 'not an int', 'tastes': {}}  # (1)
    
    try:
      User(**external_data)  # (2)
    except ValidationError as e:
      print(e.errors())
      """
      [
          {
              'type': 'int_parsing',
              'loc': ('id',),
              'msg': 'Input should be a valid integer, unable to parse string as an integer',
              'input': 'not an int',
              'url': 'https://errors.pydantic.dev/2/v/int_parsing',
          },
          {
              'type': 'missing',
              'loc': ('signup_ts',),
              'msg': 'Field required',
              'input': {'id': 'not an int', 'tastes': {}},
              'url': 'https://errors.pydantic.dev/2/v/missing',
          },
      ]
      """

```

## Who is using Pydantic?

[](<https://pydantic.dev/docs/validation/latest/get-started/#who-is-using-pydantic> ([local](./get-started.md#who-is-using-pydantic)))

Hundreds of organisations and packages are using Pydantic. Some of the prominent companies and organizations around the world who are using Pydantic include:

[![Adobe](https://pydantic.dev/docs/validation/logos/adobe_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-adobe> ([local](./get-started/why.md#org-adobe)) "Adobe")

[![Amazon and AWS](https://pydantic.dev/docs/validation/logos/amazon_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-amazon> ([local](./get-started/why.md#org-amazon)) "Amazon and AWS")

[![Anthropic](https://pydantic.dev/docs/validation/logos/anthropic_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-anthropic> ([local](./get-started/why.md#org-anthropic)) "Anthropic")

[![Apple](https://pydantic.dev/docs/validation/logos/apple_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-apple> ([local](./get-started/why.md#org-apple)) "Apple")

[![ASML](https://pydantic.dev/docs/validation/logos/asml_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-asml> ([local](./get-started/why.md#org-asml)) "ASML")

[![AstraZeneca](https://pydantic.dev/docs/validation/logos/astrazeneca_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-astrazeneca> ([local](./get-started/why.md#org-astrazeneca)) "AstraZeneca")

[![Cisco Systems](https://pydantic.dev/docs/validation/logos/cisco_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-cisco> ([local](./get-started/why.md#org-cisco)) "Cisco Systems")

[![Capital One](https://pydantic.dev/docs/validation/logos/capital_one_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-capital_one> ([local](./get-started/why.md#org-capital_one)) "Capital One")

[![Comcast](https://pydantic.dev/docs/validation/logos/comcast_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-comcast> ([local](./get-started/why.md#org-comcast)) "Comcast")

[![Datadog](https://pydantic.dev/docs/validation/logos/datadog_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-datadog> ([local](./get-started/why.md#org-datadog)) "Datadog")

[![Facebook](https://pydantic.dev/docs/validation/logos/facebook_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-facebook> ([local](./get-started/why.md#org-facebook)) "Facebook")

[![GitHub](https://pydantic.dev/docs/validation/logos/github_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-github> ([local](./get-started/why.md#org-github)) "GitHub")

[![Google](https://pydantic.dev/docs/validation/logos/google_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-google> ([local](./get-started/why.md#org-google)) "Google")

[![HSBC](https://pydantic.dev/docs/validation/logos/hsbc_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-hsbc> ([local](./get-started/why.md#org-hsbc)) "HSBC")

[![IBM](https://pydantic.dev/docs/validation/logos/ibm_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-ibm> ([local](./get-started/why.md#org-ibm)) "IBM")

[![Intel](https://pydantic.dev/docs/validation/logos/intel_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-intel> ([local](./get-started/why.md#org-intel)) "Intel")

[![Intuit](https://pydantic.dev/docs/validation/logos/intuit_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-intuit> ([local](./get-started/why.md#org-intuit)) "Intuit")

[![Intergovernmental Panel on Climate Change](https://pydantic.dev/docs/validation/logos/ipcc_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-ipcc> ([local](./get-started/why.md#org-ipcc)) "Intergovernmental Panel on Climate Change")

[![JPMorgan](https://pydantic.dev/docs/validation/logos/jpmorgan_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-jpmorgan> ([local](./get-started/why.md#org-jpmorgan)) "JPMorgan")

[![Jupyter](https://pydantic.dev/docs/validation/logos/jupyter_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-jupyter> ([local](./get-started/why.md#org-jupyter)) "Jupyter")

[![Microsoft](https://pydantic.dev/docs/validation/logos/microsoft_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-microsoft> ([local](./get-started/why.md#org-microsoft)) "Microsoft")

[![Molecular Science Software Institute](https://pydantic.dev/docs/validation/logos/molssi_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-molssi> ([local](./get-started/why.md#org-molssi)) "Molecular Science Software Institute")

[![NASA](https://pydantic.dev/docs/validation/logos/nasa_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-nasa> ([local](./get-started/why.md#org-nasa)) "NASA")

[![Netflix](https://pydantic.dev/docs/validation/logos/netflix_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-netflix> ([local](./get-started/why.md#org-netflix)) "Netflix")

[![NSA](https://pydantic.dev/docs/validation/logos/nsa_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-nsa> ([local](./get-started/why.md#org-nsa)) "NSA")

[![NVIDIA](https://pydantic.dev/docs/validation/logos/nvidia_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-nvidia> ([local](./get-started/why.md#org-nvidia)) "NVIDIA")

[![OpenAI](https://pydantic.dev/docs/validation/logos/openai_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-openai> ([local](./get-started/why.md#org-openai)) "OpenAI")

[![Oracle](https://pydantic.dev/docs/validation/logos/oracle_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-oracle> ([local](./get-started/why.md#org-oracle)) "Oracle")

[![Palantir](https://pydantic.dev/docs/validation/logos/palantir_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-palantir> ([local](./get-started/why.md#org-palantir)) "Palantir")

[![Qualcomm](https://pydantic.dev/docs/validation/logos/qualcomm_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-qualcomm> ([local](./get-started/why.md#org-qualcomm)) "Qualcomm")

[![Red Hat](https://pydantic.dev/docs/validation/logos/redhat_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-redhat> ([local](./get-started/why.md#org-redhat)) "Red Hat")

[![Revolut](https://pydantic.dev/docs/validation/logos/revolut_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-revolut> ([local](./get-started/why.md#org-revolut)) "Revolut")

[![Robusta](https://pydantic.dev/docs/validation/logos/robusta_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-robusta> ([local](./get-started/why.md#org-robusta)) "Robusta")

[![Salesforce](https://pydantic.dev/docs/validation/logos/salesforce_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-salesforce> ([local](./get-started/why.md#org-salesforce)) "Salesforce")

[![Starbucks](https://pydantic.dev/docs/validation/logos/starbucks_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-starbucks> ([local](./get-started/why.md#org-starbucks)) "Starbucks")

[![Texas Instruments](https://pydantic.dev/docs/validation/logos/ti_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-ti> ([local](./get-started/why.md#org-ti)) "Texas Instruments")

[![Twilio](https://pydantic.dev/docs/validation/logos/twilio_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-twilio> ([local](./get-started/why.md#org-twilio)) "Twilio")

[![Twitter](https://pydantic.dev/docs/validation/logos/twitter_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-twitter> ([local](./get-started/why.md#org-twitter)) "Twitter")

[![UK Home Office](https://pydantic.dev/docs/validation/logos/ukhomeoffice_logo.png)](<https://pydantic.dev/docs/validation/latest/get-started/why/#org-ukhomeoffice> ([local](./get-started/why.md#org-ukhomeoffice)) "UK Home Office")

For a more comprehensive list of open-source projects using Pydantic see the [list of dependents on github](<https://github.com/pydantic/pydantic/network/dependents>), or you can find some awesome projects using Pydantic in [awesome-pydantic](<https://github.com/Kludex/awesome-pydantic>).
