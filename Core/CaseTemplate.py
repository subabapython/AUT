
import os
import sys
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_path)
from string import Template
from Core.common import yaml_load, _path
import_code = """import pytest
import allure
import requests
from Core.BaseApi import ApiRequest
from Core.Logging import logger
import json
from Core.common import yaml_load, _path
"""
class CreateTemplate():
    """ 创建pytest 的模板数据def方法 """
    def __init__(self,yamlfilepath):
        self.reqkeys = ['method', 'url','data', 'headers', 'cookies', 'files', 'auth', 'timeout', 'allow_redirectsTrue',
                        'proxies', 'hooks', 'stream', 'verify', 'cert', 'json']
        self.import_string = Template(import_code).substitute()
        self.yaml_path = yamlfilepath
        self.file_path = _path(yamlfilepath)


    def runCreatTemplate(self):
        """ 模板创建的方法run方法"""
        yamlfilepath = self.file_path
        codefilename = os.path.basename(yamlfilepath).split(".")
        codefilepath = _path(f"TapiAut/testCase/test_{codefilename[0]}.py")
        requestdata = yaml_load(yamlfilepath)()
        class_Remarks = requestdata.get("Remarks")
        with open(_path(codefilepath),"w+",encoding="UTF-8")as f:
            f.write(self.import_string)
            class_any = self.code_class_Create(yamlfilepath,class_Remarks)
            f.write(class_any)
            for k in requestdata:
                if "api" in k:
                    def_any = self.code_def_Create(k,requestdata[k])
                    f.write(def_any)
            f.write("""
if __name__=="__main__":
    pytest.main(["-sq",__file__])"""
                    )
    def reqstr(self,TestCase):

        reqlist = []
        for key, value in TestCase.items():
            if isinstance(value, dict):
                b = f"{key} = {value}"
            elif isinstance(value, str) :
                b = f"{key} = '{value}'"
            elif value is None:
                b = f"{key} = None"
            reqlist.append(b)
        reqstr = "\n        ".join(reqlist)
        return reqstr
    # 动态生成单个测试用例对象字符串
    def code_class_Create(self,yaml_flie_path,dict_Remarks):
        class_name = os.path.basename(yaml_flie_path).split(".")[0]
        feature = dict_Remarks.get("feature")
        Remarks = dict_Remarks.get("remark")
        code =Template("""
@allure.feature("${feature}")
class Test$classname:   
    '''${Remarks}'''
    req = ApiRequest()
    Yaml_data_path = _path(r'${yaml_flie_name}')
    YamlConfig = yaml_load(_path(r"Config/ApiConfig.yaml"))
    testCase = yaml_load(Yaml_data_path)()
        """)
        string = code.substitute(classname=class_name,Remarks=Remarks,feature=feature,yaml_flie_name=self.yaml_path)
        return string
    # 动态生成单个测试用例函数字符串
    def code_def_Create(self, dictkey,Casedict):
        code = Template('''
    @allure.story("${remark}")
    def test_${name}(self):
        u"""${remark} """
        Case = self.testCase.get('${name}')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        ''')
        data_key =None
        name = dictkey
        remark = Casedict.get("ramark")
        string = code.substitute(data_key=data_key,name=name,remark=remark)
        return string
        # 动态生成单个测试用例函数字符串  目前没用

    def code_parametrize_Create(self, dictkey, Casedict):
        code = Template('''
       @pytest.mark.parametrize("${data_key}", testCase.get('${casename}').get("${data_key}"))
       def test_${casename}(self, ${data_key}):
           u"""${remark} """
           Case = self.testCase.get('${casename}')
           Case['${data_key}'] = ${data_key}
           logger.info(f"请求数据：{Case}")
           res = request.ApiSend(**Case)
           request.AssertExamine(res, **Case)
           logger.info(f"相应数据 ：{res.text}")
           ''')
        None_parametrize_code = Template('''  
       def test_${casename}(self):
           u"""${remark} """
           Debug_Data = ${Debug_Data}
           Case = self.testCase.get('${casename}')
           logger.info(f"请求数据：{Case}")
           res = request.ApiSend(**Case)
           request.AssertExamine(res,**Case)
           logger.info(f"相应数据 ：{res.text}")
           ''')
        data_key = None
        name = dictkey
        remark = Casedict.get("ramark")
        for key in Casedict.keys():
            if key in ["data", "json"]:
                data_key = key
        if data_key:
            data_list = Casedict.get(data_key)
            string = code.substitute(data_key=data_key, data_list=data_list, casename=name, remark=remark,
                                     Debug_Data=Casedict)
        else:
            string = None_parametrize_code.substitute(casename=name, remark=remark, Debug_Data=Casedict)
        return string


if __name__ == "__main__":
    Ypath = "TapiAut/CaseFile/H5.yaml"
    Tp = CreateTemplate(Ypath)
    Tp.runCreatTemplate()