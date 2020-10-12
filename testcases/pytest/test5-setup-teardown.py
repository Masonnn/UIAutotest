import pytest


def setup_module():
    print('==============================')
    print('setup_modele')


def teardown_module():
    print('==============================')
    print('teardown_modele')


def setup_function():
    print('------------')
    print('setup_function')


def teardown_function():
    print('------------')
    print('teardown_function')


class TestCase01(object):

    def setup(self):
        print('setup--------------====================================--------------')

    def teardown(self):
        print('teardown-------------====================================---------------')

    @classmethod
    def setup_class(cls):
        print('classclassclassclassclassclassclassclass')
        print('setup_class')

    def test333333333333(self):
        print('test3test3test3test3test3')

    def test444444444444(self):
        print('test444444444444test444444444444')

    @classmethod
    def teardown_class(cls):
        print('classclassclassclassclassclassclassclass')
        print('setup_class')

    def setup_method(self):
        print('setup_method---')

    def teardown_method(self):
        print('teardown_method---')


def test1():
    print('test1')


def test2():
    print('test2')


if __name__ == '__main__':
    pytest.main(['-sv', 'test5-setup-teardown.py'])
