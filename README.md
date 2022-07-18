# Nightfall
### An asynchronous API wrapped for Dead By Daylight, written in Python
___

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