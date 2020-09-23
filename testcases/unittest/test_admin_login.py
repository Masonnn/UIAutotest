from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import util


class TestAdminLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:8080/jpress/admin/login')
        cls.driver.maximize_window()

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://localhost:8080/jpress/admin/login')
    #     self.driver.maximize_window()

    # @unittest.skip
    # 测试管理员登录验证码错误
    def test_admin_login_code_error(self):
        username = 'admin'
        pwd = '123456'
        captcha = '666'
        expected = '验证码不正确，请重新输入'

        self.driver.find_element_by_name('user').send_keys(username)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('captcha').send_keys(captcha)

        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # assert alert.text == expected
        self.assertEqual(alert.text, expected)

        alert.accept()

        sleep(1)

    # 测试登录成功
    def test_admin_login_code_ok(self):
        username = 'admin'
        pwd = '123456'

        expected = 'JPress后台'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        captcha = util.get_code(self.driver, 'captchaImg')
        self.driver.find_element_by_name('captcha').clear()

        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        assert expected == self.driver.title
        # self.assertEqual(self.driver.title, expected)

        sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
