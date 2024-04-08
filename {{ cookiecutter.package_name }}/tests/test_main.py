from contextlib import redirect_stdout
from io import StringIO

from {{ cookiecutter.package_name | replace('-', '_') }}._main import main


def test_main() -> None:
    with StringIO() as buffer, redirect_stdout(buffer):
        main()
        assert buffer.getvalue().strip() == 'Dummy main function'
