from website.app import app


def test_index():
    print(f'hello')
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b'Hello World!'
