from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph
import logging

log = logging.getLogger(__name__)

config = DatahubClientConfig(server="https://api.datahub.richert.li")
graph = DataHubGraph(config)

def fetch_dataset_entities(scroll_id=None):
    scroll_id_value = "null" if scroll_id is None else f'"{scroll_id}"'

    query = """
    {
        scrollAcrossEntities(input: { types: [DATASET], query: "*", count: 5, scrollId: %s }) {
            nextScrollId
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
    """ % scroll_id_value

    results = graph.execute_graphql(query)

    next_scroll_id = results["scrollAcrossEntities"]["nextScrollId"]

    entity_list = []
    for item in results.get("scrollAcrossEntities", {}).get("searchResults", []):
        entity = item["entity"]

        entity_list.append({
            "urn": entity["urn"],
            "type": entity["type"],
            "name": entity["name"],
            "description": entity["description"] if entity["description"] else "No description",
            "platform": entity["platform"]["name"].upper()
        })
    log.info(f"Data from /dataset_entities_list: {entity_list}")

    return {
        "next_scroll_id": next_scroll_id,
        "entity_list": entity_list
    }