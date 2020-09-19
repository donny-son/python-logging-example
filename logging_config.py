import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s[%(levelname)s]%(name)s:%(message)s',
                    filename='testlog.log')
                    
logger = logging.getLogger(__name__)

logger.info('this is from the library')
