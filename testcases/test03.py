# # python3.6.5
# # 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
# from lib.ShowapiRequest import ShowapiRequest
#
# r = ShowapiRequest("http://route.showapi.com/184-4", "371786", "30d2c30a5c6c40cb82e45f0dba552fff")
# r.addFilePara("image", "../screenshots/2020-09-20-16-01-50.png")
# r.addBodyPara("typeId", "34")
# r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
# res = r.post()
# reselt = res.text  # 返回信息
# print(reselt)
#
# body = res.json()['showapi_res_body']
# print(body['Result'])
#
# # if __name__ == '__main__':
