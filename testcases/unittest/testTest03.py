import os
import unittest


class ThirdCase03(unittest.TestCase):

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    def test03(self):
        print('test03')


class ThirdCase04(unittest.TestCase):

    def test05(self):
        print('test04')

    def test06(self):
        print('test05')

    def test07(self):
        print('test06')


if __name__ == '__main__':
    # 实例化
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # testcase    # 方法一： 通过测试用例类进行加载
    # suite.addTest(loader.loadTestsFromTestCase(ThirdCase03))
    # suite.addTest(loader.loadTestsFromTestCase(ThirdCase04))
    # module    # 方法二： 通过测试用例模板去加载
    # suite.addTest(loader.loadTestsFromModule(ThirdCase03))
    # suite.addTest(loader.loadTestsFromModule(ThirdCase04))

    # 方法三：通过路径加载
    path = os.path.dirname(os.path.abspath(__file__))
    print('============')
    print(path)
    suite.addTest(loader.discover(path))

    runner = unittest.TextTestRunner()
    runner.run(suite)
