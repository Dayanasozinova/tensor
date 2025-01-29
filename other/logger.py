import logging


class Logger:

    def __init__(self):
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('\n %(asctime)s - %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
