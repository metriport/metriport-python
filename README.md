
# Metriport Python Library

[![pypi](https://img.shields.io/pypi/v/fern-metriport.svg)](https://pypi.python.org/pypi/fern-metriport)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Documentation

API reference documentation is available [here](https://docs.metriport.com/home/welcome).

## Installation

Add this dependency to your project's build file:

```bash
pip install fern-metriport
# or
poetry add fern-metriport
```

## Usage
```python
from metriport import BaseOrganization, OrgType, Address, UsState
from metriport.client import Metriport

metriport_client = Metriport(api_key="YOUR_API_KEY")

document = metriport_client.medical.organization.create(BaseOrganization(
  type=OrgType.PostAcuteCare,
  name="Metriport Inc.",
  location=Address(
    addressLine1="2261 Market Street",
    addressLine2="#4818",
    city="San Francisco",
    state=UsState.CA,
    zip="94114",
    country="USA",
  )
));
```

## Async Client
Our Python SDK exports an async client that you can use with asyncio. 

```python
from metriport import BaseOrganization, OrgType, Address, UsState
from metriport.client import AsyncMetriport

import asyncio

metriport_client = AsyncMetriport(api_key="YOUR_API_KEY")

async def create_organization():
  document = metriport_client.medical.organization.create(BaseOrganization(
      type=OrgType.PostAcuteCare,
      name="Metriport Inc.",
      location=Address(
        addressLine1="2261 Market Street",
        addressLine2="#4818",
        city="San Francisco",
        state=UsState.CA,
        zip="94114",
        country="USA",
      )
    ));

asyncio.run(create_organization())
```

## Error Handling
All exceptions thrown by the SDK will sublcass [ApiError](./src/metriport/core/api_error.py). 

```python
from metriport.core import ApiError
from metriport import BadRequestError

try:
  metriport.medical.patients.get(patient_id='my_id')
except APIError as e:  
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
