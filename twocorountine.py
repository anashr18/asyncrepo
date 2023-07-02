import asyncio
import time
from util import delay

async def  hello_world() -> str:
    await delay(1)
    return "hello world"

async def add_ten(num:int) -> int:
    return num+10

# await pauses the main thread and starts the coroutine(async function)
# async makes a normal func to coroutine 
# this is a synchronous/sequiential implemenation 
# async def main() ->None:
#     message = await hello_world()
#     num = await add_ten(10)
#     print(f'result: {message} {num}')
# asyncio.run(main())

# creating tasks 
# async def main() ->None:
#     # it suspends the main thread for three seconds
#     # sleep_for_three = await delay(3) 
#     # it does not suspends the main thread for three seconds
#     sleep_for_three = asyncio.create_task(delay(3))
#     print(type(sleep_for_three))
#     result =   await sleep_for_three
#     print(result)
# asyncio.run(main())

# running multiple coroutines  
# async def main() -> None:
#     # create tasks with delays in it
#     # concurrently tasks are running. concurrency is achieved only when tasks(i/o bound) are created. asyncio uses event loop to switch among tasks
#     start = time.time()
#     sleep_for_three = asyncio.create_task(delay(3))
#     sleep_for_four = asyncio.create_task(delay(4))
#     sleep_for_five = asyncio.create_task(delay(5))

#     await sleep_for_three
#     await sleep_for_four
#     await sleep_for_five
#     end = time.time()
#     print(f'total timr taken {end-start}')
# asyncio.run(main())

# ruuning other codes while waiting
async def main() -> None:
    task_one = asyncio.create_task(delay(3))
    task_two = asyncio.create_task(delay(4))
    await 