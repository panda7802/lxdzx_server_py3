# coding=utf-8

'''
日志
Created on 20161219

@author: pangt
'''

import logging
from logging.handlers import RotatingFileHandler

from tutils import tconf


class TLog :
    
    @staticmethod
    def init():
        LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        print("start init log " , tconf.BASE_DIR)
        # logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt='%Y-%m-%d %H:%M.%S',
                    )   
          
        # 定义个RotatingFileHandler，最多备5个日志文件，每个日志文件10M
        rthandler = RotatingFileHandler(tconf.BASE_DIR + '/log/tlog.log', maxBytes=10 * 1024 * 1024, backupCount=5)
        rthandler.setLevel(logging.INFO)
        formatter = logging.Formatter(LOG_FORMAT)
        rthandler.setFormatter(formatter)
        logging.getLogger('').addHandler(rthandler)
        print("start init log over")
    
if "__main__" == __name__ :
    TLog.init()
    try :
        logging.debug("panda debug")
        logging.info("info")
        logging.error("err panda")
        i = 6 / 0
    except Exception as e:
        logging.exception(e)
