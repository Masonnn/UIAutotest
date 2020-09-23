from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import util


class TestUserRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8080/jpress/user/register")
        cls.driver.maximize_window()

    # def setUp(self) -> None:
    #     super().setUp()
    #
    # def tearDown(self) -> None:
    #     super().tearDown()

    # def __init__(self):

    def test_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        excepted = '验证码不正确'

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        self.driver.find_element_by_name('captcha').send_keys(captcha)

        self.driver.find_element_by_class_name('btn').click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        sleep(1)
        # assert alert.text == excepted
        self.assertEqual(alert.text, excepted)
        alert.accept()

    def test_register_success(self):
        # print("start====")
        username = util.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = ''
        excepted = '注册成功，点击确定进行登录。'

        # print("find elem====")
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)

        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        captcha = util.get_code(self.driver, 'captchaimg')
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)

        # print("click ====")

        self.driver.find_element_by_class_name('btn').click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # print("verify ====")

        sleep(1)
        # assert alert.text == excepted
        self.assertEqual(alert.text, excepted)
        alert.accept()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
