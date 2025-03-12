import logging
import os
from flask import Flask
from flask_cors import CORS
from routes.datahub_graph_routes import datahub_bp  # Import Blueprint


app = Flask(__name__)
CORS(app)
log = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL") or "INFO")


app.register_blueprint(datahub_bp, url_prefix="/api")  # Register Blueprint

log.info("Flask app initialized")