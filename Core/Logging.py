import logging.config
import os
from Core.common import yaml_load,_path

def initlogging():
    log_conf_path = _path('Config/Config.yaml')
    log_flie_path = _path("LogFiles")
    if os.path.exists(log_flie_path):
        pass
    else:
        os.mkdir(log_flie_path)
    logging.config.dictConfig(yaml_load(log_conf_path)("loggings"))
initlogging()
def get_logger(name):
    logger = logging.getLogger(name)
    return logger
logger = get_logger(__file__)



