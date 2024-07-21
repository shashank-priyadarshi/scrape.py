from ..service.service import Service
from .endpoints import new as new_endpoint


class API:
    def __init__(self, service: Service):
        self.v1routes = new_endpoint(service)


def new(service: Service) -> API:
    return API(service)
