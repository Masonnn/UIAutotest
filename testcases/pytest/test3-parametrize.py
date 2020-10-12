import pytest

data = ['123', '456']


@pytest.mark.parametrize('pwd', data)
def test1(pwd):
    print(pwd)


data2 = [
    (1, 2, 3),
    (4, 5, 6),
]


@pytest.mark.parametrize('a,b,c', data2)
def test2(a, b, c):
    print(a, b, c)


data3 = (
    {'user': 1,
     'pwd': 2},
    {'user': 13,
     'pwd': 24},
)


@pytest.mark.parametrize('dic', data3)
def test3(dic):
    print(dic)


data4 = [
    pytest.param(1, 2, 3, id="(a+b):pass"),  # id的值可以自定义，只要方便理解每个用例是干什么的即可
    pytest.param(2, 4, 5, id="(a+b):pass"),
]


def add(a, b):
    return a + b


class TestParametrize(object):
    @pytest.mark.parametrize('a,b,expect', data4)
    def test_parametrize_1(self, a, b, expect):
        assert add(a, b) == expect
