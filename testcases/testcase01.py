from time import sleep

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains


def test1():
    print('first test case run')


def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')
    driver.maximize_window()
    elem = driver.find_element_by_id('agree')
    rect = elem.rect
    print(rect)
    pyautogui.click(rect['x'] + 10, rect['y'] + 130)
    sleep(3)

    # agree = ActionChains(driver).move_to_element(elem).click().perform()

    sleep(3)
