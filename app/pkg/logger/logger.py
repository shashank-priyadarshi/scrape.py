import logging
import logging.config
import os
import sys
from threading import Lock

import yaml


class LoggerSingleton:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    config_path = os.getenv('LOGGING_CONFIG_PATH', 'default_logging.yaml')
                    cls._initialize_logging(config_path)
                    cls.logger = logging.getLogger('sampleLogger')
        return cls._instance

    @classmethod
    def _initialize_logging(cls, config_path):
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
        except Exception as e:
            print(f"Failed to load configuration file: {e}", file=sys.stderr)
            sys.exit(1)

    def get_logger(self):
        return self.logger
