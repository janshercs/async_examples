import asyncio
import random
import time

# TODO: change it so that it chooses food based on any given day. Each day there are certain food available, fn1 chooses the day, fn2 chooses a food that is available on the day.
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MENU = dict(
    Monday=['Chicken', 'Fish'],
    Tuesday=['Rabbit', 'Lamb'],
    Wednesday=['Pesto', 'Beef'],
    Thursday=['Veal', 'Squab'],
    Friday=['Cod', 'Mackerel'],
    Saturday=['Carrots', 'Tamago'],
    Sunday=['Mango', 'Pear'],
)
# random_day = random.choice(DAYS)
# random_food = random.choice(MENU[random_day])

async def choose_day(n) -> str:
    i = random.randint(0, 10)
    print(f'Task{n} sleeping for: {i} seconds')
    await asyncio.sleep(i)
    random_day = random.choice(DAYS)
    print(f"Returning day{n}: {random_day}.")
    return random_day

async def choose_food(day) -> str:
    i = random.randint(0, 10)
    print(f'Thinking of choice for {day} for: {i} seconds')
    await asyncio.sleep(i)
    random_food = random.choice(MENU[day])
    return random_food

async def chain(n: int) -> None:
    start = time.perf_counter()
    chosen_day = await choose_day(n)
    chosen_food = await choose_food(chosen_day)
    end = time.perf_counter() - start
    print(f"{chosen_day} => {chosen_food} (took {end:0.2f} seconds).")

async def main(n):
    await asyncio.gather(*(chain(i) for i in range(n)))

if __name__ == "__main__":
    import sys
    n = 3 if len(sys.argv) == 1 else int(sys.argv[1])
    start = time.perf_counter()
    asyncio.run(main(n))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")