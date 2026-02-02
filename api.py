import asyncio

async def fetchdata() -> str: #asyncronous function
    print("Fetching Data...")
    await asyncio.sleep(2.5) #will make function to wait for 2.5 sec
    print("Data fetched!")

    return 'API Data'