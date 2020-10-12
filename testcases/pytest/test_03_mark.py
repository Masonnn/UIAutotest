import pytest


@pytest.mark.do
def test01():
    print('test01')


@pytest.mark.undo
def test02():
    print('test02')

# pytest -m do test_03_mark.py
