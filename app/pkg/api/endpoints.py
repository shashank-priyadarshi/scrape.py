from fastapi import APIRouter
from pydantic import BaseModel

from ..entity.v1.common_pb2 import request
from ..service.service import Service

_router = APIRouter()


class Request(BaseModel):
    url: str
    proxy: str
    depth: int
    retry_duration: int


class ScrapeRouter:
    def __init__(self, service: Service):
        self.service = service

    @_router.post("/scrape")
    async def scrape_page(self, req_body: Request):
        r = request()

        r.url = req_body.url
        r.proxy = req_body.proxy
        r.depth = req_body.depth
        r.retryDuration = req_body.retry_duration

        return await self.service.scraper.scrape_and_save(request)


def new(service: Service) -> APIRouter:
    ScrapeRouter(service)

    return _router
