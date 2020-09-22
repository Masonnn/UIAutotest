import os
import pickle
import string
from time import time, strftime, localtime
import random

from PIL import Image

from lib.ShowapiRequest import ShowapiRequest


def get_code(driver, id):
    # t = time.time()
    t = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
    # 获取验证码图片
    path = os.path.dirname(os.path.dirname(__file__)) + '/screenshots'
    picture_name1 = path + '/' + str(t) + '.png'

    driver.save_screenshot(picture_name1)

    ce = driver.find_element_by_id(id)

    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    # 解决retina屏无法定位的问题
    dpr = driver.execute_script('return window.devicePixelRatio')

    # print(dpr)
    im = Image.open(picture_name1)
    img = im.crop((left * dpr, top * dpr, right * dpr, height * dpr))

    st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))

    picture_name2 = path + '/' + st + '.png'

    img.save(picture_name2)  # 截取的验证码图片

    r = ShowapiRequest("http://route.showapi.com/184-4", "371786", "30d2c30a5c6c40cb82e45f0dba552fff")
    r.addFilePara("image", picture_name2)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()

    text = res.json()['showapi_res_body']
    code = text['Result']
    return code


def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
