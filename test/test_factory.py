from app import create_app


def test_config():
    assert not create_app().testing


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_admin(client):
    response = client.get('/admin/')
    assert response.status_code == 200
