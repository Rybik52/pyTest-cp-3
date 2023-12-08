import pytest
import requests

BASE_URL = "https://dog.ceo/api"

@pytest.fixture
def random_dog_img():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    data = response.json()
    return data.get('message')

def test_get_rand_dog_img_code():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200

def test_get_all_dog_img_code():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200

def test_dog_url(random_dog_img):
    assert random_dog_img is not None
    assert random_dog_img.startswith("https://images.dog.ceo")

def test_get_spec_breed():
    breed = "Boxer"
    response = requests.get(f"{BASE_URL}/breed/{breed}/images")
    data = response.json()

    assert "message" in data
    assert len(data["message"]) > 0

def test_format():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    data = response.json()

    assert "message" in data
    img_url = data["message"]

    assert img_url.endswith(".jpg")

