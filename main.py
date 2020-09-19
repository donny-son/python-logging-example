import logging_config
import logging
import someloop

logger = logging.getLogger(__name__)

logger.info('this is from main')

logger.info('calling foo from someloop.py')
someloop.foo()

