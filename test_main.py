import requests

def test_main():
    url = 'http://localhost:8000/helloworld'
    correct_json = {'message': 'Hello World'}
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == correct_json
