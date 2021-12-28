import collections
import collections.abc
from itertools import islice
from typing import Callable, Collection, Generator, Iterable, Iterator, Tuple, TypeVar

_T_co = TypeVar("_T_co", covariant=True)


def iter_chunks(
    iterable: Iterable[_T_co],
    size: int,
    collect: Callable[[Iterator[_T_co]], Collection[_T_co]] = tuple,
) -> Generator[Collection[_T_co], None, None]:
    it = iter(iterable)
    while True:
        chunk = collect(islice(it, size))
        if len(chunk) == 0:
            return
        yield chunk


def iter_sliding_windows(
    iterable: Iterable[_T_co],
    size: int,
) -> Generator[Tuple[_T_co], None, None]:
    it = iter(iterable)
    window = collections.deque(islice(it, size), maxlen=size)
    if len(window) == size:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)
