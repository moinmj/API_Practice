import asyncio
import api

# async def send_data(to: str):
#     print(f"Sending data to {to}...")
#     await asyncio.sleep(2)
#     print(f"Data sent to {to}!")

# async def main():
#     data = await api.fetchdata()
#     print("Data", data)
#     # await send_data("Mario")
#     # await send_data("Luigi")
#     await asyncio.gather(send_data("Mario"), send_data("Luigi"))
async def kill_time(num):
    print("running",num)
    await asyncio.sleep(1)
    print("Finished",num)
async def main():
    print("started")
    list_of_items=[]
    for i in range(1,100+1):
        list_of_items.append(kill_time(i))
    await asyncio.sleep(1)
    await asyncio.gather(*list_of_items)
    print("Done")


if __name__ == '__main__':
    asyncio.run(main())
