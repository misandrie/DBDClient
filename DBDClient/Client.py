import requests
import json
from .Headers import Headers
from .Methods.Game import Game

class Client:
    __slots__ = ['bhvrSession']

    def __init__(self, bhvrSession):
        self.bhvrSession = {'bhvrSession': bhvrSession}

    async def init(self):
        await self.checkSession(self.bhvrSession)

    async def checkSession(self, bhvrSession):
        Config = await Game.config(self)
        Config = json.loads(Config)
        if type(Config) == list:
            return True
        else:
            return False
    
    async def getSession(self):
        return self.bhvrSession

    async def getHeaders(self):
        return Headers

