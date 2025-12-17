import sys
import logging
import structlog
from .config import settings


def configure_logging() -> None:
    """Initialize stdlib logging + structlog configuration."""
    level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

    # Basic stdlib logging config
    logging.basicConfig(stream=sys.stdout, level=level, format="%(message)s")

    # Structlog processors
    processors = [
        structlog.stdlib.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt="iso"),
    ]

    # Choose JSON renderer for production-like setups, otherwise console dev renderer
    if settings.LOG_JSON:
        processors.append(structlog.processors.JSONRenderer())
    else:
        processors.append(structlog.dev.ConsoleRenderer())

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(level),
        cache_logger_on_first_use=True,
    )


__all__ = ["configure_logging"]
