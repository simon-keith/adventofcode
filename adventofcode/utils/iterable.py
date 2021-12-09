import collections
from itertools import islice
from typing import Generator, Iterable, Tuple


def sliding_window(iterable: Iterable, n: int) -> Generator[Tuple, None, None]:
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)
