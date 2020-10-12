import allure
import pytest


@pytest.fixture(scope='session')
def login():
    print('登录')


@allure.step('step 1 : click xxx')
def step1():
    print('111')


@allure.step('step 2 : click xxx')
def step2():
    print('222')


class TestEditPage():

    @allure.story("这是一个xxx的测试用例")
    def test_1(self, login):
        step1()
        step2()

        print('xxx')

    @allure.story("这是一个yyy的测试用例")
    def test_2(self, login):
        step1()
        step2()

        print('xxx')


if __name__ == '__main__':
    # pytest.main(['test6-allure.py', '-sv'])
    pytest.main(['--alluredir', './reports', 'test6-allure.py'])
