import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


def capital_case(x):
    return x.capitalize()


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s

    print(f"{__file__} execute d in {elapsed:0.2f} seconds.")
