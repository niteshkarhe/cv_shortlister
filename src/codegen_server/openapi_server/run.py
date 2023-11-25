import connexion
import os
from flask_cors import CORS

from datetime import timedelta
from openapi_server.app_context import init_app, get_logger
from openapi_server.json_provider import CustomJSONProvider

logger = get_logger()

def create_app():
    app = connexion.App(__name__, specification_dir='./openapi/')
    CORS(app.app)
    app.app.json_provider_class = CustomJSONProvider
    app.app.json = CustomJSONProvider(app.app)
    app.add_api('openapi.yaml',
                arguments={"title": "CV Scanner"},
                pythonic_params=True
                )

    app.app.add_url_rule("/", view_func=get_status_check)
    app.app.add_url_rule("/api", view_func=get_status_check)

    app.app.config.update(
        CSRF_COOKIE_SAMESITE=None,
        SESSION_COOKIE_SAMESITE=None
    )

    init_app(app.app)

    return app.app

def get_status_check():
    return {"ContentType": "application/json"}

application = create_app()