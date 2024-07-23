from ..logger.logger import LoggerSingleton
from ..service.service import Service
from .endpoints import new as new_endpoint


class API:
    def __init__(self, logger: LoggerSingleton, service: Service):
        self.v1routes = new_endpoint(logger, service)


def new(logger: LoggerSingleton, service: Service) -> API:
    return API(logger, service)
