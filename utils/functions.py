from utils.logging import start_logger


logger = start_logger(__name__)

def add_one(x: int) -> int:
    logger.info(f'Adding one to {x}')
    return x + 1