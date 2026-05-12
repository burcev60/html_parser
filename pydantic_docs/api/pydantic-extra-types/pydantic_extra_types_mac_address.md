---
title: Mac Address
source: https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_mac_address/
---

The MAC address module provides functionality to parse and validate MAC addresses in different formats, such as IEEE 802 MAC-48, EUI-48, EUI-64, or a 20-octet format.

## MacAddress 

<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_mac_address/#pydantic_extra_types.mac_address.MacAddress> ([local](./pydantic_extra_types_mac_address.md#pydantic_extra_types.mac_address.MacAddress)) ([local](./pydantic_extra_types_mac_address.md#pydantic_extra_types.mac_address.MacAddress))

**Bases:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

Represents a MAC address and provides methods for conversion, validation, and serialization.

```
 
    from pydantic import BaseModel
    
    from pydantic_extra_types.mac_address import MacAddress
    
    
    class Network(BaseModel):
        mac_address: MacAddress
    
    
    network = Network(mac_address='00:00:5e:00:53:01')
    print(network)
    # > mac_address='00:00:5e:00:53:01'
    

```

### Methods

<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_mac_address/#methods> ([local](./pydantic_extra_types_mac_address.md#methods)) ([local](./pydantic_extra_types_mac_address.md#methods))

#### validate_mac_address 

<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_mac_address/#pydantic_extra_types.mac_address.MacAddress.validate_mac_address> ([local](./pydantic_extra_types_mac_address.md#pydantic_extra_types.mac_address.MacAddress.validate_mac_address)) ([local](./pydantic_extra_types_mac_address.md#pydantic_extra_types.mac_address.MacAddress.validate_mac_address))

`@staticmethod`

```
 
    def validate_mac_address(value: bytes) -> str
    

```

Validate a MAC Address from the provided byte value.

##### Returns

<https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_mac_address/#returns> ([local](./pydantic_extra_types_mac_address.md#returns)) ([local](./pydantic_extra_types_mac_address.md#returns))

[`str`](https://docs.python.org/3/library/stdtypes.html#str)
