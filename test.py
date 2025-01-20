import asyncio

async def task_one():
    print("Task one started.")
    await asyncio.sleep(2)  # Simulates a delay (e.g., I/O operation)
    print("Task one finished.")

async def task_two():
    print("Task two started.")
    await asyncio.sleep(1)  # Simulates a shorter delay
    print("Task two finished.")

async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(task_one(), task_two())

# Run the async main function
asyncio.run(main())
