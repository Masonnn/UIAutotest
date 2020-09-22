# import os
#
# from PIL import Image
# import pytesseract
#
# from time import sleep, localtime, time, strftime
# from selenium import webdriver
#
#
# def test_screen_capture():
#     browser = webdriver.Chrome()
#     browser.get("http://localhost:8080/jpress/user/register")
#     browser.maximize_window()
#
#     # t = time.time()
#     st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
#     picture_name1 = st + '.png'
#     path = os.path.abspath("screenshots")
#     print(path)
#     file_path = path + '/' + picture_name1
#
#     browser.get_screenshot_as_file(file_path)
#
#     ce = browser.find_element_by_id('captchaimg')
#     print(ce.location)
#     print(ce.size)
#     left = ce.location['x']
#     top = ce.location['y']
#     right = ce.size['width'] + left
#     height = ce.size['height'] + top
#
#     # retina屏处理办法
#     dpr = browser.execute_script('return window.devicePixelRatio')
#     print(dpr)
#
#     im = Image.open(file_path)
#     img = im.crop((left * dpr, top * dpr, right * dpr, height * dpr))
#
#     sleep(1)
#
#     st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
#     picture_name2 = st + '.png'
#
#     img.save(path + '/' + picture_name2)
#     sleep(2)
#     browser.quit()
#
#
# def test2():
#     image1 = Image.open('../screenshots/WX20200920-160350.png')
#     str = pytesseract.image_to_string(image1)
#     print(str)
#
#
# if __name__ == '__main__':
#     test2()
