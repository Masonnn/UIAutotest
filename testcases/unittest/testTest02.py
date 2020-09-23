import unittest
from time import sleep

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # super().setUpClass()
        print('setUpClass...')
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.baidu.com/")
        cls.driver.maximize_window()

    def setUp(self) -> None:
        # super().setUp()
        print('setup...')

    def tearDown(self) -> None:
        # super().tearDown()
        print('tearDown...')

    def test01(self):
        print('test01...')
        self.driver.find_element_by_id('kw').send_keys('极客时间')
        sleep(1)

    def test02(self):
        print('test02...')
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test03(self):
        print('test03...')
        self.assertEqual(1, 1)
        self.assertIn(1, [2, 3], '不包含')

    @classmethod
    def tearDownClass(cls) -> None:
        # super().tearDownClass()
        print('tearDownClass...')
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
