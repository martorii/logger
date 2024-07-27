from utils.logging import start_logger
from utils.functions import add_one

logger = start_logger(__name__)

logger.debug("Debugging")
logger.info("Informing")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")

add_one(2)