import logging
import logging.handlers

LOG_FILE = 'tst.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=50)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)  #
handler.setFormatter(formatter)  #

logger = logging.getLogger('tst')  #
logger.addHandler(handler)  #
logger.setLevel(logging.DEBUG)

logger.info('first info message')
logger.debug('first debug message')