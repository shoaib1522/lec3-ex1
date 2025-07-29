from app import app
# this is the test case
def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"Hello World! \n from: M. Shoaib Ahmad"