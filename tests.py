from application import app

# @pytest.fixture
# def client():
#     with application.test_client() as client:
#         yield client

# def test_index(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.data == b'Web Application with Python Flask!'
# def test1():
#     response = application.test_client().get('/')
#     assert response.status_code == 200
#     assert b"Web Application with Python Flask!" in response.data


def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Web Application with Python Flask!'