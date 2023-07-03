from fastapi.testclient import TestClient

from main import app


def test_root_returns_json():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    assert response.json() == {'message': 'Hello World'}


def test_trim_and_uppercase_initials():
    client = TestClient(app)
    # start by clearing out existing high scores
    response = client.put('/clear')
    assert response.status_code == 200

    # add one higher score
    response = client.put('/addscore?initials=Brendon&score=120000')
    assert response.status_code == 200
    res = response.json().pop()
    assert res['score_list'] == [["BRE", 120000]]


def test_addscore_score_but_no_initials():
    client = TestClient(app)
    response = client.put('/addscore?initials=BCC')
    assert response.status_code == 422  # unprocessable content


def test_addscore_initials_but_no_score():
    client = TestClient(app)
    response = client.put('/addscore?score=120000')
    assert response.status_code == 422  # unprocessable content


def test_three_highscores_returns_sorted():
    client = TestClient(app)
    # start by clearing out existing high scores
    response = client.put('/clear')
    assert response.status_code == 200

    # add one higher score
    response = client.put('/addscore?initials=AMC&score=12000')
    assert response.status_code == 200
    res = response.json().pop()
    assert res['score_list'] == [['AMC', 12000]]

    # add one lower score and make sure scores are sorted descending
    response = client.put('/addscore?initials=BCC&score=10000')
    assert response.status_code == 200
    res = response.json().pop()
    assert res['score_list'] == [['AMC', 12000], ['BCC', 10000]]

    response = client.put('/addscore?initials=DMC&score=11000')
    assert response.status_code == 200
    res = response.json().pop()
    assert res['score_list'] == [['AMC', 12000], ['DMC', 11000], ['BCC', 10000]]


def test_add_eleven_highscores_check_for_top_ten():
    client = TestClient(app)
    # start by clearing out existing high scores
    response = client.put('/clear')
    assert response.status_code == 200

    for i in range(11):
        initials = chr(65+i) * 3
        score = 10000 * (i + 1)
        response = client.put(f'/addscore?initials={initials}&score={score}')
        assert response.status_code == 200

    res = response.json().pop()
    assert res['score_list'] == [['KKK', 110000], ['JJJ', 100000], ['III', 90000],
                                 ['HHH', 80000], ['GGG', 70000], ['FFF', 60000],
                                 ['EEE', 50000], ['DDD', 40000], ['CCC', 30000],
                                 ['BBB', 20000]]


def test_clear_returns_empty_list():
    client = TestClient(app)
    response = client.put('/clear')

    assert response.status_code == 200
    assert response.json() == []
