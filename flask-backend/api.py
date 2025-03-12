import logging
import os
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph 
# TODO: instead of using "pip install <dependency>" localy, figure out how to use the dependecies that docker has (.devcontainers)

from flask import Flask

app = Flask(__name__)
log = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL") or "INFO")


config = DatahubClientConfig(server="https://api.datahub.richert.li")
graph = DataHubGraph(config)

@app.route("/api")
def get_data():
    log.info("Handling GET request for /api")

    entity_list = []

    # If it is needed to process more than 10000 entities, then should use scrollAcrossEntities which seems to allow pagination
    query = """
    {
        search(input: { type: DATASET, query: "*", start: 0, count: 10000 }) {
            searchResults {
                entity {
                    urn
                    type
                    ...on Dataset {  # different types contain different fields
                        name
                        description
                        platform {
                            name
                        }
                    }
                }
            }
        }
    }
    """

    results = graph.execute_graphql(query)
    
    for item in results.get("search", {}).get("searchResults", []):
        entity = item["entity"]

        entity_list.append({
            "urn": entity["urn"],
            "type": entity["type"],
            "name": entity["name"],
            "description": entity["description"],
            "platform": entity["platform"]["name"].upper()
        })


    '''
    Use the DataHubGraph client to fetch all entities of type "dataset" from DataHub
    https://datahubproject.io/docs/python-sdk/clients/#datahub.ingestion.graph.client.DataHubGraph
    The required dependency is listed in the requirements.txt file
    Use https://api.datahub.richert.li as the DataHub server (no authentication required) 
    '''

    return entity_list