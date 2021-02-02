import logging.config
import os
from Core.common import yaml_load, _path

def initlogging():
    log_conf_path = _path('Config/Config.yaml')
    log_flie_path = _path("LogFiles")
    if os.path.exists(log_flie_path):
        pass
    else:
        os.mkdir(log_flie_path)
    dictconfig = yaml_load(log_conf_path)("loggings")
    dictconfig["handlers"]["info_file_handler"]["filename"] = _path("LogFiles/info.log")
    dictconfig["handlers"]["error_file_handler"]["filename"] = _path("LogFiles/errors.log")
    logging.config.dictConfig(dictconfig)

initlogging()
def get_logger(name):
    logger = logging.getLogger(name)
    return logger
logger = get_logger(__file__)



