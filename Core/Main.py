import os
import sys
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_path)
print(sys.path)
from Core.common import _path
import shutil
import pytest
from Core.CaseTemplate import CreateTemplate
def del_list():
    filepath = _path("report/result")
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
def Creat_Template(path = "TapiAut/CaseFile/H5.yaml" ):
    """ 传入 要呗生成方法的yanl 文件 生成 def 方法"""
    yamllist = []
    path = _path(path)
    if os.path.isdir(path):
        files = os.listdir(_path(path))
        for i in files:
            if "yaml" in i:
                yamllist.append(os.path.join(path, i))

    elif os.path.isfile(path):
        yamllist.append(path)
    else:
        print("it's a special file(socket,FIFO,device file)")
    if yamllist:
        for j in yamllist:
            template = CreateTemplate(yamlfilepath=j)
            template.runCreatTemplate()

def runMain():
    """ 通过模拟命令行运行 TemplateCase 生成单个的方法函数
        再运行pytest
        allure 命令行进行运行生成报告"""
    del_list()
    case_path = _path(r"TapiAut/testCase")
    result_path = _path(r"result")
    html_path = _path(r"report/html")
    allure_path = _path(r"allure-2.13.7/bin")
    pytest.main(["-s", "-n", "auto", case_path, "--alluredir", result_path])
    command_str = fr"{allure_path}/allure generate {result_path} -o {html_path} --clean"
    command_server = fr"{allure_path}/allure serve {result_path}"
    os.system(command_str)
    #os.system(command_server)

if __name__ == "__main__":
    runMain()

