import asyncio
import random
import time

# TODO: try to make it record the number of items processed! or the total amount of sleep time. How do you get returned items in a queue?
class Customer:
    def __init__(self):
        self.name = random.choice(['A', 'B', 'C', 'D', 'E', 'F']) + str(random.randint(0,10))
        self.items = random.randint(1,10)
    
    def __str__(self):
        return (f'{self.name} with {str(self.items)} items')

def make_customer() -> str:
    return Customer()

async def randsleep(caller=None) -> None:
    i = random.randint(0, 5)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)

async def customer_adder(name: int, q: asyncio.Queue) -> None:
    for i in range(5):
        await randsleep(caller=f"Producer {name}")  # waits for random seconds before making and adding customer to queue
        customer = make_customer()
        await q.put(customer)
        print(f'Producer {name} added <Customer {customer}> to queue.')
        print(f'{q.qsize()} customers in the queue.')

async def worker(name: int, efficiency: int, q: asyncio.Queue) -> None:
    while True:
        customer = await q.get()
        print(f"Worker {name} got element <{customer}>")
        print(f'{q.qsize()} customers in the queue.')
        time_to_process = customer.items//efficiency
        await asyncio.sleep(time_to_process)
        print(f'Worker {name} worked on customer {customer} for {time_to_process}s')
        q.task_done()
        # return items  # TODO: some how this doesn't really work!

async def main(customer_adders, workers):
    q = asyncio.Queue()
    customer_adders = [asyncio.create_task(customer_adder(n, q)) for n in range(customer_adders)]
    workers = [asyncio.create_task(worker(n, efficiency, q)) for n, efficiency in enumerate(workers)]
    await asyncio.gather(*customer_adders)
    await q.join()  # Implicitly awaits worker, too
    for c in workers:
        c.cancel()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--customer_adders", type=int, help='Pass in number of customer adders you want, each customer adder will add 10 customers each at random times.', default=2)
    parser.add_argument("-w", "--workers", nargs='+', type=int, help='Pass in efficiency of each worker you have/want. 0.5x means worker will take 2s to do 1 task.', default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(customer_adders=ns.customer_adders, workers=ns.workers))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")