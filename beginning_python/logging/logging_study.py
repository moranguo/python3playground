import logging
#默认生成的root logger的level是logging.WARNING,低于该级别的就不输出了
#级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
print("default log level is logging.WARNING")
logging.debug(u"debug message")
logging.info(u"info message")
logging.warning(u"warning message")
print("another warning message")
logging.error(u"error message")
logging.critical(u"critical message")

# there is no sequence between logging output and the print function call output
# the output order is dynamic
# default log level is logging.WARNING
# 2019-01-07 17:44:52,787 - logging_study.py[line:7] - DEBUG: debug message
# another warning message
# 2019-01-07 17:44:52,787 - logging_study.py[line:8] - INFO: info message
# 2019-01-07 17:44:52,787 - logging_study.py[line:9] - WARNING: warning message
# 2019-01-07 17:44:52,787 - logging_study.py[line:11] - ERROR: error message
# 2019-01-07 17:44:52,787 - logging_study.py[line:12] - CRITICAL: critical message
