from asyncio import countasync


# def capital_case(x):
#     return x.capitalize()


def test_capital_case() -> None:
    assert countasync.capital_case('semaphore') == 'Semaphore'
