import os
import sys
from contextlib import contextmanager

if sys.version_info >= (3, 9):
    from collections.abc import Iterator
else:
    from typing import Iterator


@contextmanager
def chdir(path: str) -> Iterator[None]:
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)
