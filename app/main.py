from fastapi import FastAPI

from app.init.config import get_app_settings
from app.init.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    # App Setting
    settings = get_app_settings()
    application = FastAPI(**settings.fastapi_kwargs)

    # App Middleware

    # App Event Handler
    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings)
    )

    # App Exception Handler

    # App Routes

    return application

if __name__ == "__main__":
    app = get_application()