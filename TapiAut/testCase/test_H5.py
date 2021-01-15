import pytest
import allure
import requests
from Core.BaseApi import ApiRequest
from Core.Logging import logger
import json
from Core.common import yaml_load

@allure.feature("测试用例集备注说明")
class TestH5:   
    '''xxxxsdsadasdxxxxxxxxxxxxx'''
    req = ApiRequest()
    Yaml_data_path = r'C:\Users\67091\Desktop\MCAutTest\TapiAut/CaseFile/H5.yaml'
    YamlConfig = yaml_load(r"C:\Users\67091\Desktop\MCAutTest\Config\ApiConfig.yaml")
    testCase = yaml_load(Yaml_data_path)()
        
    @allure.story("用户注册")
    def test_api_user_regist(self):
        u"""用户注册 """
        Case = self.testCase.get('api_user_regist')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding='UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_sharing_uid(self):
        u"""None """
        Case = self.testCase.get('api_sharing_uid')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_coin_coinTransfer(self):
        u"""None """
        Case = self.testCase.get('api_coin_coinTransfer')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_coin_userCoin(self):
        u"""None """
        Case = self.testCase.get('api_coin_userCoin')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_balance_withdraw_info(self):
        u"""None """
        Case = self.testCase.get('api_balance_withdraw_info')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_balance_withdraw_check(self):
        u"""None """
        Case = self.testCase.get('api_balance_withdraw_check')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_balance_withdraw_launch(self):
        u"""None """
        Case = self.testCase.get('api_balance_withdraw_launch')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_new_task_commodity(self):
        u"""None """
        Case = self.testCase.get('api_new_task_commodity')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_balance_balance_redeem(self):
        u"""None """
        Case = self.testCase.get('api_balance_balance_redeem')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_task_game_balanceAndCoin(self):
        u"""None """
        Case = self.testCase.get('api_task_game_balanceAndCoin')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_new_task_callback_ad_reward(self):
        u"""None """
        Case = self.testCase.get('api_new_task_callback_ad_reward')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_new_task_callback_ad_taskInfo_withdrawViewVideo(self):
        u"""None """
        Case = self.testCase.get('api_new_task_callback_ad_taskInfo_withdrawViewVideo')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_new_task_ad_taskInfo_withdrawViewVideo(self):
        u"""None """
        Case = self.testCase.get('api_new_task_ad_taskInfo_withdrawViewVideo')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_new_task_spin_info(self):
        u"""None """
        Case = self.testCase.get('api_new_task_spin_info')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
    @allure.story("None")
    def test_api_new_task_spin(self):
        u"""None """
        Case = self.testCase.get('api_new_task_spin')
        logger.info(f"请求数据：{Case}")
        name, remark, examine, method, url, kwargs, kwargs_json = self.req.Set_req_data(**Case)
        with allure.step(f'name: {remark}'):
            res = self.req.request(method, url, **kwargs)
            allure.attach(kwargs_json, f"请求数据")
            allure.attach(json.dumps(json.loads(res.text, encoding = 'UTF-8'), sort_keys=True, indent=2), f"响应数据")
        self.req.AssertExamine(res, examine)
        logger.info(f"相应数据 ：{res.text}")
        return res
        
if __name__=="__main__":
    pytest.main(["-sq",__file__])