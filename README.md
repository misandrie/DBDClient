# Nightfall
An asynchronous API wrapper for Dead By Daylight, written in Python

#### Installation
To install the library normally, run:  
`python -m pip install --user --upgrade git+https://github.com/malchanceux/Nightfall.git`

#### Example usage

Retrieve current shrine of secrets perks
```python

from DBDClient.Client import Client
from DBDClient.Methods import Store
import asyncio

# Declare behaviour session token variable
bhvrSession='value'

# Create Client object
Player = Client(bhvrSession)

async def main():
    # Initialize object
    await Player.init()  
    
    # Get current shrine perks
    perks = await Store.Shrine.getAvailable(Player)  
    
    print(perks)

asyncio.run(main())
```

#### Usage with Fiddler (or any other HTTPS traffic capturing program)
Go to [this line](https://github.com/malchanceux/Nightfall/blob/13972a7fd11445bf7d6556e8b17baa7c045f2136/DBDClient/Request.py#L12) and change `verify=True` to `verify=False`.  
This will disable SSL verification and allow you to use the library with Fiddler