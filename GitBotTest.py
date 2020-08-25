import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "WillMcLV",
                       oauth_token=os.getenv("GH_AUTH"))
        await gh.post("/repos/WillMcLV/BotTest/issues",
                      data={"title": "Hello",
                            "body": "Goodbye."})

asyncio.run(main())
