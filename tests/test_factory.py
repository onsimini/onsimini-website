from website import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
    assert not create_app().debug
    assert create_app({'DEBUG': True}).debug


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
