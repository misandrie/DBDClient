from DBDClient.Request import Request

class Shrine:
    """
    Object for shrine methods
    """
    def __init__(self) -> None:
        pass

    """
    Returns current perks in the shrine of secrets
    """
    async def getAvailable(Client):
        return await Request("GET", "/v1/dbd-shrine/get-available", await Client.getSession(), await Client.getHeaders(), None)

class Store:
    """
    Object for store methods
    """

    def __init__(self) -> None:
        pass
    
    async def getAvailableBundles(Client):
        """
        Retrieves all auric cell bundles in store
        """
        return await Request("POST", "/v1/extensions/store/getAvailableBundles", await Client.getSession(), await Client.getHeaders(), None)
