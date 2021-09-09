from fastapi.testclient import TestClient
from index import app
import pytest

client = TestClient(app)


@pytest.mark.order(1)
@pytest.mark.dependency()
def test_write_data():
    pytest.short_url = ""
    pytest.long_url = "https://www.tech.gov.sg/"

    response = client.post(
        "/url",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={"long_url": pytest.long_url},
    )

    assert response.status_code == 200
    assert response.json() != None
    assert response.json()["long_url"] != None
    assert response.json()["short_url"] != None

    pytest.short_url = response.json()["short_url"]


@pytest.mark.order(2)
@pytest.mark.dependency(depends=['test_write_data'])
def test_read_data():
    response = client.get(
        "/url/" + pytest.short_url,
        headers={"accept": "application/json"})
    assert response.status_code == 200
    assert response.json() == {"long_url": pytest.long_url,
                               "short_url": pytest.short_url}
