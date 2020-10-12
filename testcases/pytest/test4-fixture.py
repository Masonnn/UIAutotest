import pytest


@pytest.fixture(scope='function', autouse=True)
def init():
    print('init...')
    return 1


@pytest.fixture(scope='function', autouse=True)
def after():
    print('after...')
    return 2

    # class lei1(object):
    # @pytest.mark.usefixtures('init')


def test1():
    print('test1')


# @pytest.mark.usefixtures('init')
def test2():
    print('test2')


# class lei2(object):
# @pytest.mark.usefixtures('init')
def test3():
    print('test3')


# @pytest.mark.usefixtures('init')


def test4():
    print('test4')


if __name__ == '__main__':
    pytest.main(['-sv', 'test4-fixture.py'])
