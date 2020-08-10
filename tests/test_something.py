import pytest
from projectname.something import run


def test_run():
    assert run('World') == {'Hello': 'World'}