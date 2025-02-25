import logging
from logging.handlers import RotatingFileHandler
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s->%(levelname)s->%(message)s",
#         filename="log.txt")


log_handler = RotatingFileHandler('my.log', maxBytes=10, backupCount=50)
formatter = logging.Formatter("%(asctime)s->%(levelname)s->%(message)s")
log_handler.setFormatter(formatter)  
logger = logging.getLogger(__name__)
logger.addHandler(log_handler)

try:
    logger.info("TRY INFOR")
    a=1000
    if a<2000:
        logger.DEBUG()
except Exception as err:
    logger.info("EXCEPTION BLOCK")

logger.debug("DEBUG")
logger.info("INFO")
logger.warn("WARN")
logger.error("ERROR")
logger.exception("EXCEPTION")
logger.critical("CRITICAL")
