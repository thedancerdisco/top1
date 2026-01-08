# # многопоточность многопроцессорность
# import threading
# import time
# def print_numbers(name: str)->None:
#     for i in range (1, 11):
#         time.sleep(2)
#         print(f"thread: {name} number: {i}")


# thread_1 = threading.Thread(target=print_numbers, args = ("thread_1", ))

# thread_2 = threading.Thread(target=print_numbers, args = ("thread_2", ))
# thread_1.start()
# thread_2.start()
# print("potok zapushen")


# thread_1.join()
# thread_2.join()

# гонка за ресурсы
# import threading
# import time
# counter = 0
# locker = threading.Lock()
# def increment() ->None:
#     global counter
#     for _ in range(1000):
#         with locker:
#         # time.sleep(0.05)
#             counter +=1

# threads = [threading.Thread(target=increment) for _ in range (5)]


# for th in threads:
#     th.start()

# for th in threads:
#     th.join()

# print(f" counter: {counter}")


# асинхронное программирование

import asyncio
import time

async def task1()->str:
    await asyncio.sleep(2)
    return "task1 completed"

async def task2()->str:
    await asyncio.sleep(2)
    return "task2 completed"

async def task3()->str:
    await asyncio.sleep(2)
    return "task3 completed"

# async def main():
#     start = time.time()
#     await task1()
#     await task2()
#     await task3()
#     end = time.time()
#     print(f"time: {end-start}")

async def main():
    start = time.time()
    results = await asyncio.gather(task1(), task2(), task3())
    end = time.time()
    print(results)
    print(f"time: {end-start}")


def main(name: str):
    print(f"Process {name} started")
    asyncio.run(asyncio_main())
import multiprocessing

if __name__ == "__main__":

    process1 = multiprocessing.Process(target=main, args=("process1"))
    process1.start()
    main("main")
    process1.join()

# asyncio.run(main())
