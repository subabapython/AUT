# import pytest, requests, json
# from  Core.BaseApi import ApiRequest
#
#
# @pytest.fixture(scope='session' ,autouse=True)
# def action_test_Api():
#     print("---------------------开始----------------------")
#     request = ApiRequest()
#     login(request)
#     yield
#     print("-------------------end-------------------------")
#     request.close()
# def login(request):
#
#     url = "https://dty.dev.jianbolive.com/mer/login"
#     data = {"account": "13371676215", "password": "123654", "key": "1608114602.77435fd9e1aabd0a49.68946548",
#             "code": "6666"}
#     if "Token" not in request.headers:
#         res = request.send_request("POST", url=url, data=data)
#     assert (res["status"] == 200)
#     assert (res["message"] == "success")
#     request.headers["X-Token"] = res["data"]["token"]

