import logging
import configparser


class CustomFormatter(logging.Formatter):

    light_blue = "\x1b[36;20m"
    grey = "\x1b[36;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: light_blue + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logging_level():
    """
    Convert string to logging level
    """
    # Get logging level from env file
    config = configparser.ConfigParser()
    config.read('.env')
    level = config['LOGGING']['LEVEL']
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    assert level in levels, f"level must be one of {', '.join(levels)}"
    return eval(f"logging.{level.upper()}")


def start_logger(filename: str) -> logging.Logger:
    # Create logger for filename
    logger = logging.getLogger(filename)
    # Set logging level
    logger.setLevel(get_logging_level())
    # Create console handler
    ch = logging.StreamHandler()
    # Add formating to handler
    ch.setFormatter(CustomFormatter())
    # Add handler to logger
    logger.addHandler(ch)
    return logger