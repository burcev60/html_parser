---
title: Routing Numbers
source: https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_routing_numbers/
---

The `pydantic_extra_types.routing_number` module provides the [`ABARoutingNumber`](#pydantic_extra_types.routing_number.ABARoutingNumber) data type.

## ABARoutingNumber 

#pydantic_extra_types.routing_number.ABARoutingNumber

**Bases:** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

The `ABARoutingNumber` data type is a string of 9 digits representing an ABA routing transit number.

The algorithm used to validate the routing number is described in the [ABA routing transit number](https://en.wikipedia.org/wiki/ABA_routing_transit_number#Check_digit) Wikipedia article.

```
 
    from pydantic import BaseModel
    
    from pydantic_extra_types.routing_number import ABARoutingNumber
    
    
    class BankAccount(BaseModel):
        routing_number: ABARoutingNumber
    
    
    account = BankAccount(routing_number='122105155')
    print(account)
    # > routing_number='122105155'
    

```
