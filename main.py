# from testcases import testcase01,testcase02
import os
from time import sleep

from testcases.unittest import test_user_register, test_user_login, test_admin_login, test_category, test_article
from lib.HTMLTestRunner import *
import unittest
import pytest
import allure

if __name__ == '__main__':
    preRunner = unittest.TextTestRunner()
    preRunner.run(test_admin_login.TestAdminLogin().test_admin_login_code_ok())
    # login = test_admin_login.TestAdminLogin()
    # login.test_admin_login_code_ok()
    # case = test_category.TestCategory(login)
    # case = test_user_register.TestUserRegister()
    # case.test_register_code_error()
    # case.test_add_category_error()
    # case.test_add_category_success()

    # case = test_article.TestArticle(login)
    # case.test_add_article_success()
    # case.test_delete_one_article_success()
    # case.test_delete_all_article_success()
    # sleep(2)
    # case.login.driver.quit()

    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'

    path = os.path.dirname(os.path.dirname(__file__)) + '/UIAutotest/reports/ExampleReport.html'
    print(path)

    testsuite = unittest.TestSuite()

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_user_register.TestUserRegister))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_user_login.TestUserLogin))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_admin_login.TestAdminLogin))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_category.TestCategory))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_article.TestArticle))

    with open(path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
