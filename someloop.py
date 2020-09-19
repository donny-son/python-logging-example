import logging

logger = logging.getLogger(__name__)

logger.info('this is from the someloop')

def foo():
    for i in range(3):
        logger.info(f'the number is {i}')
        if i == 1:
            try:
                1/0
            except Exception:
                logger.exception('some exception happened')
