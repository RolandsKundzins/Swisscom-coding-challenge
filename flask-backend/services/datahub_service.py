from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph 

config = DatahubClientConfig(server="https://api.datahub.richert.li")
graph = DataHubGraph(config)

# If it is needed to process more than 10000 entities, then should use scrollAcrossEntities which seems to allow pagination
def fetch_dataset_entities():    
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
    
    entity_list = []
    for item in results.get("search", {}).get("searchResults", []):
        entity = item["entity"]

        entity_list.append({
            "urn": entity["urn"],
            "type": entity["type"],
            "name": entity["name"],
            "description": entity["description"] if entity["description"] else "No description",
            "platform": entity["platform"]["name"].upper()
        })
    
    return entity_list