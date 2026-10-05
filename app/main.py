from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.errors import ApiError
from app.routers import tasks

app = FastAPI(title="TaskFlow", version="0.1.0")
app.include_router(tasks.router)


@app.exception_handler(ApiError)
async def api_error_handler(_: Request, exc: ApiError) -> JSONResponse:
    """Toutes les erreurs métier sortent au format {"error": {"code", "message"}}."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": exc.code, "message": exc.message}},
    )
