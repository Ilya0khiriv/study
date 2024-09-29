import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    tries = 5
    inverse_power = 6 - power

    for i in range(1, tries+1):
        await asyncio.sleep(inverse_power)
        print(f'Силач {name} поднял {i}')

    print(f'Силач {name} закончил соревнования.')
    
async def start_tournament():

    tasks = (
        asyncio.create_task(start_strongman('Pasha', 3)),
        asyncio.create_task(start_strongman('Denis', 4)),
        asyncio.create_task(start_strongman('Apollon', 5))
    )

    for i in tasks:
        await i


asyncio.run(start_tournament())
