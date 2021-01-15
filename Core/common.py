import os
import yaml
def _path(*args):
    '''
    获取任何目录
    :param args: 逐级目录名称
    :return:  返回给定目录路径
    '''
    any_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), *args)
    return any_path

def yaml_load(*args):
    path = _path(*args)
    with open(path, "rt",encoding="utf-8") as f:
        data = yaml.safe_load(f.read())
        def _data(name = None):
            if name:
                return data[name]
            else:
                return data
        return _data
def yaml_dump(path, data):
    with open(path, "w") as f:
        data = yaml.dump(data, f)
        return data






