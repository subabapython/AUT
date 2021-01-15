import traceback
from Core.common import _path
from time import  sleep
from selenium.webdriver.remote.webelement import WebElement
import time
import allure
from Core.common import yaml_load
from selenium.webdriver import Chrome
from Core.Logging import logger
from selenium.common.exceptions import *
from selenium import webdriver
# 单例的装饰器
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

@Singleton
class WebChrome(Chrome):

    def __init__(self):
        Config_path = _path("Core", "Config.yaml")
        self.Congfig = yaml_load(Config_path)
        driver_path = f"{_path()}\\{ self.Congfig('driver_path')}\\chromedriver.exe"
        driver_options = yaml_load(Config_path)("driver_options")
        if driver_options :
            option = webdriver.ChromeOptions()
            for i in driver_options:
                option.add_argument(i)
        super().__init__(executable_path=driver_path,options=option)
        self.implicitly_wait(20)
        self.father_number = {0: 0}
        self.number = 0
        self.OUTIME = self.Congfig("outtime")
        self.POLL_FREQUENCY = self.Congfig("POLL_FREQUENCY")

    def __call__(self,operation,element_value, *args, **kwargs):
        try:
            web_element = self.wait(operation,element_value)
            logger.info(f"寻找元素成功 --value：{element_value} --Mothe ：{operation}")
        except Exception  :
            logger.error(f"寻找元素失败：--value：{element_value} --Mothe：{operation}  \n {traceback.format_exc()}")
            traceback.format_exc()

        return Element(web_element)

    def wait(self, operation,element_value ):
        stacktrace = None
        end_time = time.time() + self.OUTIME
        while True:
            try:
                web_element = self.find_element(operation, element_value)
                return web_element
            except Exception as exc:
                stacktrace = exc
            time.sleep(self.POLL_FREQUENCY)
            if time.time() > end_time:
                break
        raise stacktrace


    def switch_to_latest_window(self):
        _father = self.number
        self.number = len(self.window_handles) - 1
        self.father_number[self.number] = _father
        self.switch_to_window(self.window_handles[self.number])
        time.sleep(0.5)

    def switch_to_last_window(self):
        self.number = self.father_number[self.number]
        self.switch_to_window(self.window_handles[self.number])
        time.sleep(0.5)

class Element(WebElement):

    def __init__(self, _obj):
        super(Element, self).__init__(parent=_obj._parent, id_=_obj._id, w3c=_obj._w3c)

    def click(self,mgs=None):
        with allure.step(mgs):
            super(Element, self).click()
            time.sleep(0.5)

    def send_keys(self, text, mgs=None,keyborad=None):
        with allure.step(mgs):
            if keyborad:
                super(Element, self).send_keys(text, keyborad)
            else:
                super(Element, self).send_keys(text)
            time.sleep(0.5)
    def assert_text(self, text):
        assert text in self.text.encode("utf-8")
        time.sleep(0.5)

    def get_attribute(self, name, mgs=None):
        with allure.step(mgs):
            super(Element, self).get_attribute(name)


def select_element():
    data = yaml_load(page_path)
    element = data[page_title][element_name]



driver =WebChrome()









