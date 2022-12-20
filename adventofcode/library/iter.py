import collections
import collections.abc
from itertools import islice
from typing import Callable
from typing import Collection
from typing import Iterable
from typing import Iterator
from typing import Tuple
from typing import TypeVar

_T_co = TypeVar("_T_co", covariant=True)


def iter_chunks(
    iterable: Iterable[_T_co],
    size: int,
    collect: Callable[[Iterator[_T_co]], Collection[_T_co]] = tuple,
) -> Iterator[Collection[_T_co]]:
    it = iter(iterable)
    while True:
        chunk = collect(islice(it, size))
        if len(chunk) == 0:
            return
        yield chunk


def iter_sliding_windows(
    iterable: Iterable[_T_co],
    size: int,
) -> Iterator[Tuple[_T_co, ...]]:
    it = iter(iterable)
    window = collections.deque(islice(it, size), maxlen=size)
    if len(window) == size:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)
