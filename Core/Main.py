import os
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
    # del_list()
    case_path = _path(r"TapiAut\testCase")
    result_path = _path(r"report\result")
    html_path = _path(r"report\html")
    allure_path = _path(r"allure-2.13.7\bin")
    pytest.main(["-s", "-n", "4", case_path, "--alluredir", result_path])
    command_str = fr"{allure_path}\allure generate {result_path} -o {html_path} --clean"
    os.system(command_str)

if __name__ == "__main__" :
    Creat_Template()
    runMain()
