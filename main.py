# from testcases import testcase01,testcase02
from time import sleep

from testcases.basic import test_user_register, test_admin_login, test_category, test_article

if __name__ == '__main__':
    login = test_admin_login.TestAdminLogin()
    login.test_admin_login_code_ok()
    # case = test_category.TestCategory(login)
    # case = test_user_register.TestUserRegister()
    # case.test_register_code_error()
    # case.test_add_category_error()
    # case.test_add_category_success()

    case = test_article.TestArticle(login)
    case.test_add_article_success()
    case.test_delete_one_article_success()
    case.test_delete_all_article_success()
    sleep(2)
    case.login.driver.quit()
