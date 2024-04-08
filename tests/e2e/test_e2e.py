import json
import subprocess
import sys
from collections import OrderedDict
from shutil import rmtree
from subprocess import Popen
from typing import Any

import pytest

from .. import chdir

if sys.version_info >= (3, 9):
    from collections import OrderedDict
    from collections.abc import Iterator
else:
    from typing import Iterator, OrderedDict


@pytest.fixture
def cleanup(package_name: str) -> Iterator[None]:
    try:
        yield
    finally:
        rmtree(package_name, ignore_errors=True)


@pytest.fixture
def cookiecutter_config() -> OrderedDict[str, Any]:
    with open('cookiecutter.json') as cookiecutter_file:
        return json.load(cookiecutter_file, object_pairs_hook=OrderedDict)


@pytest.mark.usefixtures('cleanup')
def test_e2e(package_name: str, cookiecutter_config: OrderedDict[str, Any]) -> None:
    with Popen('scripts/run.sh', stdin=subprocess.PIPE) as process:
        assert process.stdin is not None
        for input_name in cookiecutter_config:
            if input_name == 'package_name':
                process.stdin.write(package_name.encode())
            process.stdin.write(b'\n')
            process.stdin.flush()

    with chdir(package_name):
        for target in ('setup', 'lint', 'format', 'type-check', 'test', 'coverage', 'docs', 'clean'):
            subprocess.run(['make', target], check=True)
