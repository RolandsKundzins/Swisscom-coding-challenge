def validate_response(response):
    """Helper function to validate API response structure"""
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()

    assert isinstance(data, dict)
    assert "next_scroll_id" in data
    assert "entity_list" in data
    assert isinstance(data["entity_list"], list)

    if data["entity_list"]:
        entity = data["entity_list"][0]
        assert isinstance(entity, dict)
        assert all(key in entity for key in ["urn", "type", "name", "description", "platform"])

    return data


def test_get_dataset_entities_list(client):
    """Test the API call to /dataset_entities_list with and without scroll_id"""

    # First request without scroll_id
    data = validate_response(client.get("/api/dataset_entities_listz"))

    # Use the next_scroll_id from the first response to request the next page
    if data["next_scroll_id"]:
        response2 = client.get(f"/api/dataset_entities_list?scroll_id={data['next_scroll_id']}")
        validate_response(response2)
