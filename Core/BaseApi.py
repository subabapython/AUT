from Core.Logging import logger
import pytest
from requests import Session
import json
import allure
import time
from Core.common import yaml_load, _path
error_code = {0: "",
            100001: "System error, please retry later",
            100010: "System error, please retry later"}
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton
@Singleton
class ApiRequest(Session):
    def __init__(self):
        super().__init__()
        time.sleep(1)
        self.Set_headers()
        self.timeout = 20
        self.reqkeys = ['params', 'data', 'headers', 'cookies', 'files', 'auth', 'timeout',
                        'allow_redirectsTrue', 'proxies', 'hooks', 'stream', 'verify', 'cert', 'json']
        self.reqstr = ['method', 'url', 'examine', 'params', 'data', 'headers', 'cookies',
                       'files', 'auth', 'timeout', 'allow_redirectsTrue', 'proxies',
                       'hooks', 'stream', 'verify', 'cert', 'json']

    def Set_headers(self):
        self.headers = {'Accept-Encoding': ', '.join(('gzip', 'deflate')), 'Accept': '*/*', }
        defaul_headers = yaml_load(_path("Config", "ApiConfig.yaml"))("headers")
        self.headers.update(defaul_headers)

    def Set_req_data(self, **YamlCasekwargs):
        kwargs = {}
        kwargs_json = {}
        method = YamlCasekwargs.get("method")
        url = YamlCasekwargs.get("url")
        headers = YamlCasekwargs.get("headers")
        name = YamlCasekwargs.get("name")
        remark = YamlCasekwargs.get("remark")
        t = YamlCasekwargs.get("json") or YamlCasekwargs.get("data")
        examine = YamlCasekwargs.get("examine")
        if headers:
            self.headers.update(headers)
        if t:
            for i in t:
                for j in self.headers:
                    if i == j:
                        self.headers[j] = t[i]
        YamlCasekwargs["headers"] = self.headers
        for k in YamlCasekwargs:
            if k in self.reqkeys:
                kwargs[k] = YamlCasekwargs[k]
            if k in self.reqstr:
                kwargs_json[k] = YamlCasekwargs[k]
        kwargs_json = json.dumps(kwargs_json, sort_keys=True, indent=2)
        return name, remark, examine, method, url, kwargs, kwargs_json

    def AssertExamine(self, req, examine):
        if isinstance(req.text, str):
            res = json.loads(req.text)
        assert req.ok == True
        try:
            assert res["code"] == 0
        except:
            logger.error(req.text)
            raise
        if examine:
            for i in examine:
                examine[i] == res[i]







"""

import requests ,json
req =requests.Session()
a = req.request("POST","https://showdoc.int.kuaiyin123.net/server/index.php?s=/api/user/login",json={'username': 'sujianghai',
'password': 'sujianghai',
'v_code':""})
response = req.request("POST","https://showdoc.int.kuaiyin123.net/server/index.php?s=/api/item/info",cookies=a.cookies,data={'item_id': 7,
'keyword': '',
'default_page_id': 0})
# response.headers={"Content-Type", "text/html;charset=UTF-8"}
response.encoding='utf-8'
st= response.text
# print(json.loads(st,encoding="utf-8"))
response= req.request("POST","https://showdoc.int.kuaiyin123.net/server/index.php?s=/api/page/info",cookies=a.cookies,data={"page_id":657})
st= response.text
da =json.loads(st,encoding="utf-8")
# print(json.loads(st,encoding="utf-8"))
ste= da["data"]["page_content"]
print(ste)
import re
pattern = re.compile("(http:)?(/*/*) $")
print(pattern.findall(ste))
"""

