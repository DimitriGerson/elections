#ESSAIS d'asynchronysation sur la lecture d'un fichier
import asyncio 
import aiofiles

async def chargement_csv():
    async with aiofiles.open("path/to/file") as f:
        async for line in f: 
            print(line)
