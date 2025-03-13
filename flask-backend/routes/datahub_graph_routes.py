import logging
from flask import Blueprint, jsonify, request
from services.datahub_service import fetch_dataset_entities

log = logging.getLogger(__name__)
datahub_bp = Blueprint("data", __name__)  # Define Blueprint

@datahub_bp.route("/dataset_entities_list", methods=["GET"])
def get_data():
    """
    Fetch dataset entities from DataHub with optional pagination.

    Query Parameters:
        scrollId (str, optional): Token for fetching the next page.

    Returns:
        JSON with:
        - next_scroll_id (str): Token for the next batch.
        - entity_list (list): List of dataset entities.

    Example:
        GET /api/dataset_entities_list?scrollId=abc123
    """
    scroll_id = request.args.get("scrollId")
    return fetch_dataset_entities(scroll_id)




# The task:
'''
Use the DataHubGraph client to fetch all entities of type "dataset" from DataHub
https://datahubproject.io/docs/python-sdk/clients/#datahub.ingestion.graph.client.DataHubGraph
The required dependency is listed in the requirements.txt file
Use https://api.datahub.richert.li as the DataHub server (no authentication required)
'''