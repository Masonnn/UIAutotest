from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure


class TestUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    def test_login_failure_with_wrongUser(self):
        user = 'helloWA'
        pwd = '123'
        excepted = '用户名不正确。'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(user)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 3).until(EC.alert_is_present())

        actual = self.driver.switch_to.alert

        assert excepted == actual.text
        sleep(1)
        actual.accept()

    def test_login_failure_with_wrongPwd(self):
        user = '123'
        pwd = '1234564567'
        excepted = '用户名或密码不正确'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(user)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 3).until(EC.alert_is_present())

        actual = self.driver.switch_to.alert

        assert excepted == actual.text
        actual.accept()

    def test_login_success(self):
        user = 'admin'
        pwd = '123456'
        excepted = '用户中心'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(user)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 3).until(EC.title_contains('用户中心'))

        sleep(1)

        assert self.driver.title == excepted

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['test_user_login', '-sv'])
