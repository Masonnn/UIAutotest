from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest

from testcases.unittest import test_admin_login


class TestArticle(unittest.TestCase):
    # def __init__(self, method, login):
    #     unittest.TestCase.__init__(self, method)
    #     self.login = login

    def __init__(self, login):
        self.login = login

    def test_add_article_success(self):
        title = '我的文章'
        content = '我的文章内容'
        expected = '文章保存成功。'

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        # sleep(1)
        # //*[@id="sidebar-menu"]/li[4]/ul/li[2]/a
        # /html/body/div/div/section[3]/div/div/div/div[1]/div/div/a
        # self.login.driver.find_element_by_xpath('/html/body/div/div/section[3]/div/div/div/div[1]/div/div/a').click()

        sleep(1)

        self.login.driver.find_element_by_id('article-title').send_keys(title)

        frame1 = self.login.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(frame1)

        sleep(1)

        # /html/body
        self.login.driver.find_element_by_xpath('/html/body').send_keys(content)

        self.login.driver.switch_to.default_content()
        # //*[@id="form"]/div/div[2]/div[1]/div/button[1]
        self.login.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()

        loc = (By.CSS_SELECTOR, ".toast-message")
        WebDriverWait(self.login.driver, 3).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected

    def test_delete_one_article_success(self):
        # 点击文章
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # //*[@id="sidebar-menu"]/li[4]/ul/li[1]/a
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)

        link = self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')
        ActionChains(self.login.driver).move_to_element(link).perform()

        sleep(1)
        # 删除前文章数
        article_num = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        print(article_num)

        #
        del_elem = self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[3]')
        del_elem.click()

        sleep(1)

        # 删除后文章数
        article_num2 = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        print(article_num2)

        assert article_num == article_num2 + 1

    def test_delete_all_article_success(self):
        # 点击文章
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)

        link = self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input')
        link.click()

        self.login.driver.find_element_by_id('batchDel').click()

        WebDriverWait(self.login.driver, 5).until(EC.alert_is_present())
        alert = self.login.driver.switch_to.alert
        alert.accept()

        sleep(1)

        # 删除后文章数
        artile_num = self.login.driver.find_elements_by_class_name('jp-actiontr')
        assert len(artile_num) == 0

    def runTest(self):
        self.test_add_article_success()
        self.test_delete_one_article_success()
        self.test_delete_all_article_success()


if __name__ == '__main__':
    login = test_admin_login.TestAdminLogin()
    login.test_admin_login_code_ok()
    case = TestArticle(login)
    unittest.main()
# login = test_admin_login.TestAdminLogin()
# login.test_admin_login_code_ok()
# case = test_article.TestArticle(login)
# case.test_add_article_success()
# case.test_delete_one_article_success()
# case.test_delete_all_article_success()
