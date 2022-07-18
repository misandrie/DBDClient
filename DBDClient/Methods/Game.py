import requests
from DBDClient.Request import Request

class Game:
    def __init__(self) -> None:
        pass

    async def config(Client):

        """
        Returns config for the game if valid token
        """
        return await Request("GET", "/v1/config", await Client.getSession(), await Client.getHeaders(), None)
    
    async def version():
        return await Request("GET", "/v1/version", None, None, None)

    async def healthCheck():
        return await Request("GET", "/v1/healthcheck", None, None, None)

    async def contentVersion(version=None):
        if version is not None:
            version = f"?versionPattern={version}"
        return await Request("GET", f"/v1/utils/contentVersion/version{version}", None, None, None)