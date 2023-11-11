import asyncio


async def sum(n1, n2):
    print('Start sum of', n1, n2)
    s = n1 + n2
    print('End sum of ', n1, n2)
    return s

loop = asyncio.get_event_loop()
results = loop.run_until_complete(sum(1,2))
print(results)
