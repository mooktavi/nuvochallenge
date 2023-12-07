import requests
import pytest

base_url = "https://petstore.swagger.io/v2"

def get_pets_by_status(status):
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": status})
    return response

@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status_success(status):
    """Test that the endpoint returns a 200 status code and a list of pets for valid statuses."""
    response = get_pets_by_status(status)
    assert response.status_code == 200
    assert isinstance(response.json(), list), "The response should be a list of pets."

@pytest.mark.parametrize("status", ["", "invalid", None])
def test_find_pets_by_status_invalid(status):
    """Test that the endpoint handles invalid statuses appropriately."""
    response = get_pets_by_status(status)
    assert response.status_code == 400, "Invalid status should result in a 400 error."
  
def test_find_pets_by_status_content_type():
    """Test that the response content type is JSON."""
    status = "available"
    response = get_pets_by_status(status)
    assert response.headers["Content-Type"] == "application/json"

def test_find_pets_by_status_data_schema():
    """Test that the response data follows the expected schema."""
    status = "available"
    response = get_pets_by_status(status)
    pets = response.json()
    for pet in pets:
        # Here we would validate all required fields and their types
        # For example:
        assert "id" in pet, "ID is missing from pet data."
        assert "name" in pet, "Pet name is missing."
        assert "status" in pet and pet["status"] == status, "Status is incorrect."