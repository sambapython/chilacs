import logging
# default level logging.WARN

logging.info("INFO")# it will consider the default basicConfig
logging.warn("WARN BEFORE BASICCONFIG")
logging.basicConfig(level=logging.DEBUG)
logging.debug("debug")
logging.info("INFO")
logging.warn("WARN")
logging.error("ERROR")
logging.exception("EXCEPTION")
logging.critical("CRITICAL")