import logging
import os

from flask import Flask

app = Flask(__name__)
log = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL") or "INFO")

@app.route("/api")
def get_data():
    log.info("Handling GET request for /api")

    entity_list = []

    '''
    
    Use the DataHubGraph client to fetch all entities of type "dataset" from DataHub
    https://datahubproject.io/docs/python-sdk/clients/#datahub.ingestion.graph.client.DataHubGraph
    The required dependency is listed in the requirements.txt file
    Use https://api.datahub.richert.li as the DataHub server (no authentication required) 
    
    '''

    return entity_list