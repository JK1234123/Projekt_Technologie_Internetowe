import requests
import json
import pytest

@pytest.mark.contract
def test_get_user_contract():
    expected_user_data = [{
    "userId": 1,
    "id": 1,
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    }]
    url = "http://127.0.0.1:5000/api"
    params = {"limit": int(1)}
    response = requests.get(url, params)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    user_data = response.json()
    assert user_data == expected_user_data
