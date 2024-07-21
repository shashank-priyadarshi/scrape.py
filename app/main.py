from builder import Builder
from fastapi import FastAPI

builder = Builder(
    db_type='inmem',  # Example: 'inmem', 'file', 'relational'
    notification_type='console',  # Example: 'console', 'email'
    scraper_type='basic',  # Example: 'basic', 'advanced'
)

app = FastAPI()

app.include_router(builder.routers, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
