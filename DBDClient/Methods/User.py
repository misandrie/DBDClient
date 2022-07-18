from DBDClient.Request import Request

class User:
    """
    Class for user-related method calls
    """

    async def location(Client):
        """
        Returns location where the bvhrSession token was generated
        """

        return await Request("GET", "/v1/me/location", await Client.getSession(), await Client.getHeaders(), None)

    async def playerName(Client):
        """
        Returns username, userid
        """

        return await Request("GET", "/v1/playername", await Client.getSession(), await Client.getHeaders(), None)
    
    async def blockedPlayers(Client):
        """
        Returns players you've blocked in-game
        """

        return await Request("GET", "/v1/players/me/blockedPlayers", await Client.getSession(), await Client.getHeaders(), None)

    async def banStatus(Client):
        """
        Returns player's ban status
        """

        return await Request("GET", "/v1/players/ban/status", await Client.getSession(), await Client.getHeaders(), None)
    
    async def penaltyPoints(Client):
        """
        Returns penalty points (for disconnecting mid-game, for example)
        """

        return await Request("POST", "/v1/players/ban/decayAndGetDisconnectionPenaltyPoints", await Client.getSession(), await Client.getHeaders(), None)

    async def getRituals(Client):
        """
        Returns rituals
        """

        return await Request("POST", "/v1/dbd-core-ritual/get-and-generate-rituals", await Client.getSession(), await Client.getHeaders(), None)
    
    async def currencies(Client):
        """
        Returns currency values
        """
        
        return await Request("GET", "/v1/wallet/currencies", await Client.getSession(), await Client.getHeaders(), None)
    
    async def getPlayerLevel(Client):
        """
        Returns player's XP, level, presige, current xp and xp needed for next level
        """

        return await Request("POST", "/v1/extensions/playerLevels/getPlayerLevel", await Client.getSession(), await Client.getHeaders(), None)