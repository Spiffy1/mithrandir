from typing import List
import asyncio  # noqa
import pytest  # noqa
import pytest_asyncio.plugin  # noqa
from mithrandir.monad import Monad, MonadSignatures

pytestmark = pytest.mark.asyncio


@pytest.fixture(scope="function")
async def setup():
    pass


async def test_01():
    def inc_by_2(n: int):
        return n + 2

    def multiply_by_2(n: int):
        return n * 2

    def only_more_than_15(n: int):
        return n > 15

    res = Monad([3, 9])

    data = res \
        .map(inc_by_2) \
        .map(multiply_by_2, model=int) \
        .filter(only_more_than_15)

    assert data.unwrap() == [22]
    

    
async def test_async():
    async def inc_by_2(n: int):
        return n + 2

    async def multiply_by_2(n: int):
        return n * 2

    def only_more_than_15(n: int):
        return n > 15

    async def only_more_than_30(n: int):
        return n > 30

    async def to_range(n: str):
        return list(range(int(n)))

    res = Monad([3, 9])

    data = res \
        .map(inc_by_2, model=int) \

    assert isinstance(data, Monad)
    # assert data.__cb
    assert res.unwrap() == [3, 9]
    # assert not res.cb

    data = await res \
        .map(inc_by_2, model=int) \
        .resolve()

    assert res.unwrap() == [3, 9]
    assert data.unwrap() == [5, 11]

    data = await res \
        .map(inc_by_2, model=int) \
        .map(multiply_by_2, model=int) \
        .resolve()

    assert res.unwrap() == [3, 9]
    assert data.unwrap() == [10, 22]

    data = await res \
        .map(inc_by_2, model=int) \
        .map(multiply_by_2, model=int) \
        .filter(only_more_than_15, model=int) \
        .resolve()

    # print(data.cb)
    assert data.unwrap() == [22]

    data = await res \
        .map(inc_by_2, model=int) \
        .map(multiply_by_2, model=int) \
        .filter(only_more_than_15, model=int) \
        .filter(only_more_than_30, model=int) \
        .resolve()

    assert data.unwrap() == []

