from DBDClient.Request import Request

class Info:
    """
    Class for user-related information
    """
    async def playerName(Client):
        """
        Returns username, userid
        """

        return await Request("GET", "/v1/playername", await Client.getSession(), await Client.getHeaders(), None)
    
    async def location(Client):
        """
        Returns location where the bvhrSession token was generated
        """

        return await Request("GET", "/v1/me/location", await Client.getSession(), await Client.getHeaders(), None)
    
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

    async def resetGetPips(Client):
        """
        Retrieves player's pips, next rank reset date and seasonRefresh boolean
        """

        return await Request("POST", "/v1/ranks/reset-get-pips-v2", await Client.getSession(), await Client.getHeaders(), None)

class Relations:

    async def blockedPlayers(Client):
        """
        Returns players you've blocked in-game
        """

        return await Request("GET", "/v1/players/me/blockedPlayers", await Client.getSession(), await Client.getHeaders(), None)

class Tasks:
    """
    Class for user-related tasks (Archive, Rituals)
    """
    async def getRituals(Client):
        """
        Creates and returns current rituals (daily tasks)
        """

        return await Request("POST", "/v1/dbd-core-ritual/get-and-generate-rituals", await Client.getSession(), await Client.getHeaders(), None)
    
    async def archiveStatus(Client):
        """
        Returns status of the archive
        """

        return await Request("GET", "/v1/feature/status/archives", await Client.getSession(), await Client.getHeaders(), None)

    async def archiveActiveNode(Client):
        """
        Returns active archive node
        """

        return await Request("GET", "/v1/archives/stories/get/activeNode", await Client.getSession(), await Client.getHeaders(), None)
