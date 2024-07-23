from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..entity.v1.common_pb2 import request
from ..logger.logger import LoggerSingleton
from ..service.service import Service

_router = APIRouter()


class Request(BaseModel):
    url: str
    proxy: str
    depth: int
    retry_duration: int


class ScrapeRouter:
    def __init__(self, logger: LoggerSingleton, service: Service):
        self.logger = logger
        self.service = service
        self.router = _router
        self.router.post("/scrape")(self.scrape_page)

    async def scrape_page(self, req_body: Request):
        r = request()

        # TODO: Add request body validation
        # TODO: Migrate from Pydantic JSON to ProtoBuf
        try:
            r.url = req_body.url
            r.proxy = req_body.proxy
            r.depth = req_body.depth
            r.retryDuration = req_body.retry_duration
        except Exception as e:
            self.logger.error("Error setting protobuf fields: %s", str(e))
            raise HTTPException(status_code=500, detail="Internal server error")

        self.logger.info("Protobuf request object populated: %s", r)

        try:
            response = await self.service.scraper.scrape_and_save(r)
            return {"status": response.status_code, "message": response.message}
        except Exception as e:
            self.logger.error("Error in scrape_and_save: %s", str(e))
            raise HTTPException(status_code=500, detail="Internal server error")


def new(logger: LoggerSingleton, service: Service) -> APIRouter:
    router_instance = ScrapeRouter(logger, service)

    return router_instance.router
