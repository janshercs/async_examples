import asyncio

async def hi():
    await asyncio.sleep(1)
    return 'Hi'

async def there():
    await asyncio.sleep(1)
    return 'There'

async def jans():
    await asyncio.sleep(1)
    return 'Jans'


async def main():
    a =  await asyncio.gather(hi(), there(), jans())
    print(a)


if __name__ == '__main__':
    import time
    s  = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds')