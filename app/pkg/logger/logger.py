import logging
import logging.config
import os
import sys
from threading import Lock

import yaml
import coloredlogs


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
                    cls.logger = logging.getLogger(os.getenv('LOGGER_NAME', 'application'))
        return cls._instance

    @classmethod
    def _initialize_logging(cls, config_path):
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)

                if 'coloredlogs' in config:
                    coloredlogs_config = config['coloredlogs']
                    coloredlogs.install(
                        level=coloredlogs_config.get('level', 'DEBUG'),
                        fmt=coloredlogs_config.get('fmt',
                                                   '[%(pathname)s:%(lineno)d] %(asctime)s %(name)-15s %(levelname)-8s '
                                                   '%(message)s'),
                        datefmt=coloredlogs_config.get('datefmt', '%Y-%m-%d %H:%M:%S'),
                        level_styles=coloredlogs_config.get('level_styles', {}),
                        field_styles=coloredlogs_config.get('field_styles', {})
                    )
        except Exception as e:
            print(f"Failed to load logger configuration file: {e}", file=sys.stderr)
            sys.exit(1)

    def get_logger(self):
        return self.logger
