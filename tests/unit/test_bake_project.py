import sys
from contextlib import contextmanager
from pathlib import Path
from shutil import rmtree
from typing import Any, Optional, Protocol

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from collections.abc import Iterator
else:
    from typing import Dict, Iterator


class Result(Protocol):
    project_path: Path
    exit_code: int
    exception: Optional[Exception]


class Cookies(Protocol):
    def bake(self, extra_context: Dict[str, Any]) -> Result: ...


@contextmanager
def bake_in_temp_dir(cookies: Cookies, context: Dict[str, Any] = {}) -> Iterator[Result]:
    result = cookies.bake(context)
    try:
        yield result
    finally:
        rmtree(result.project_path, ignore_errors=True)


def test_simple_bake(cookies: Cookies, package_name: str) -> None:
    with bake_in_temp_dir(cookies, {'package_name': package_name}) as result:
        assert result.project_path.is_dir()
        assert result.project_path.name == package_name
        assert result.exit_code == 0
        assert result.exception is None
