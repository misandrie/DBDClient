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
        """
        Returns game's health state
        """

        return await Request("GET", "/v1/healthcheck", None, None, None)

    async def contentVersion(version=None):
        """
        Returns content versions for specified version
        If the value is none - returns all available versions
        """
        
        if version is not None:
            version = f"?versionPattern={version}"
        return await Request("GET", f"/v1/utils/contentVersion/version{version}", None, None, None)