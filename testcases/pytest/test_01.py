import pytest


class TestLoginCase(object):

    # 不能有init方法，报错信息如下
    # PytestCollectionWarning: cannot collect test class 'TestLoginCase'
    # because it has a __init__ constructor (from: test_01.py)
    # def __init__(self):
    #     print('init')

    def test01(self):
        print('==========test01=======')
        assert 1 == 1

    def test02(self):
        print('==========test02=======')
        assert 1 == 1

    def test03(self):
        print('==========test03=======')
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_01.py'])
