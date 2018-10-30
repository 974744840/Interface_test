import logging
import os.path
import time

'''获取绝对路径'''
cur_path=os.path.dirname(os.path.realpath(__file__))
log_path=os.path.join(os.path.dirname(cur_path),'logs')
if not os.path.exists(log_path):os.mkdir(log_path)

class Logger(object):

    def __init__(self,logger):
        '''新建logger对象，并设置日志级别,文件重命名'''
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.logname=os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d_%H_%M'))

        '''创建要输出的日志对象'''
        fh=logging.FileHandler(self.logname,encoding='utf-8',mode='a+')
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.INFO)
        '''
         format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
         %(levelno)s: 打印日志级别的数值
         %(levelname)s: 打印日志级别名称
         %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
         %(filename)s: 打印当前执行程序名
         %(funcName)s: 打印日志的当前函数
         %(lineno)d: 打印日志的当前行号
         %(asctime)s: 打印日志的时间
         %(thread)d: 打印线程ID
         %(threadName)s: 打印线程名称
         %(process)d: 打印进程ID
         %(message)s: 打印日志信息
        '''

        '''设置输出格式'''
        formatter=logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        '''将设置好的格式的对象添加'''
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        '''提供调用方法'''
    def getlog(self):
        return self.logger