from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

from app.api.v1 import api_router
from app.core.config import settings
from app.core.logging import configure_logging
import sentry_sdk


# Initialize logging and observability
configure_logging()

# Initialize Sentry if configured
if settings.SENTRY_DSN:
    sentry_sdk.init(dsn=settings.SENTRY_DSN, traces_sample_rate=0.1)

app = FastAPI()

# Simple Prometheus metric
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint", "http_status"])


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        try:
            REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path, http_status=str(response.status_code)).inc()
        except Exception:
            pass
        return response


if settings.METRICS_ENABLED:
    app.add_middleware(MetricsMiddleware)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hepatitis B Adherence System API"}


@app.get("/metrics")
def metrics():
    """Prometheus metrics endpoint."""
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)