import logging
import os
from flask import Flask, request
from flask_cors import CORS
from routes.datahub_graph_routes import datahub_bp  # Import Blueprint


app = Flask(__name__)
CORS(app)
log = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL") or "INFO")

# Log requests and responses
@app.before_request
def log_request():
    log.info(f"📩 Request: {request.method} {request.path} - Params: {request.args} - Body: {request.get_data(as_text=True)}")

@app.after_request
def log_response(response):
    log.info(f"📤 Response: {response.status_code} - {response.get_data(as_text=True)}")
    return response

# Register Blueprint - api routes
app.register_blueprint(datahub_bp, url_prefix="/api")  

log.info("Flask app initialized")