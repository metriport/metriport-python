# Metriport Python Library

[![pypi](https://img.shields.io/pypi/v/metriport.svg)](https://pypi.python.org/pypi/metriport)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://buildwithfern.com/?utm_source=metriport/metriport-python/readme)

## Documentation

API reference documentation is available [here](https://docs.metriport.com/home/welcome).

## Installation

Add this dependency to your project's build file:

```bash
pip install metriport
# or
poetry add metriport
```

## Usage
```python
import os
from dotenv import load_dotenv
from metriport.client import Metriport
from metriport.medical import BasePatient, PersonalIdentifier_DriversLicense
from metriport.commons import Address, UsState

load_dotenv()

facility_id = os.environ.get("FACILITY_ID")
api_key = os.environ.get("API_KEY")
base_url = os.environ.get("BASE_URL") ## optional param to base to client if want to point to sandbox url.

client = Metriport(api_key=api_key)
patient_data = BasePatient(
    first_name="John",
    last_name="Doe",
    dob="1980-01-01",
    gender_at_birth="M",
    personal_identifiers=[
        PersonalIdentifier_DriversLicense(
            type="driversLicense",
            state=UsState.CA,
            value="12345678",
        )
    ],
    address=[Address(
        address_line_1="123 Main St",
        city="Los Angeles",
        state=UsState.CA,
        zip="90001",
        country="USA"
    )]
)
response = client.medical.patient.create(facility_id=facility_id, request=patient_data)
```

## Async Client
Our Python SDK exports an async client that you can use with asyncio. 

```python

import os
from dotenv import load_dotenv
from metriport.client import AsyncMetriport
from metriport.medical import BasePatient, PersonalIdentifier_DriversLicense
from metriport.commons import Address, UsState
import asyncio

load_dotenv()

facility_id = os.environ.get("FACILITY_ID")
api_key = os.environ.get("API_KEY")

metriport_client = AsyncMetriport(api_key="YOUR_API_KEY")

async def create_patient():
  patient_data = BasePatient(
    first_name="John",
    last_name="Doe",
    dob="1980-01-01",
    gender_at_birth="M",
    personal_identifiers=[
        PersonalIdentifier_DriversLicense(
            type="driversLicense",
            state=UsState.CA,
            value="12345678",
        )
    ],
    address=[Address(
        address_line_1="123 Main St",
        city="Los Angeles",
        state=UsState.CA,
        zip="90001",
        country="USA"
    )]
  )
  response = client.medical.patient.create(facility_id=facility_id, request=patient_data)

asyncio.run(create_patient())
```

## Error Handling
All exceptions thrown by the SDK will sublcass [ApiError](./src/metriport/core/api_error.py). 

```python
from metriport.core import ApiError

try:
  client.medical.patient.create(facility_id='bad_id', request="bad_req")
except ApiError as e:  
  print(e) 
  # handle any api related error
```

## Timeouts
By default, the client is configured to have a timeout of 60 seconds. You can customize this value at client instantiation.

```python
from metriport.client import Metriport

metriport_client = Metriport(api_key="YOUR_API_KEY", timeout=15)
```

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!

##

```
            ,▄,
          ▄▓███▌
      ▄▀╙   ▀▓▀    ²▄
    ▄└               ╙▌
  ,▀                   ╨▄
  ▌                     ║
                         ▌
                         ▌
,▓██▄                 ╔███▄
╙███▌                 ▀███▀
    ▀▄
      ▀╗▄         ,▄
         '╙▀▀▀▀▀╙''


      by Metriport Inc.

```
