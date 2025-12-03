import pytest
from app_home import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_quote(client):
    payload = {
        "coverages": {"dwelling": {"sum_insured": 500000, "year_built": 2000}},
        "insured": {"age": 45}
    }
    rv = client.post('/v1/quote', json=payload)
    assert rv.status_code == 200
    data = rv.get_json()
    assert 'premium' in data

def test_bind_policy(client):
    payload = {
        "coverages": {"dwelling": {"sum_insured": 500000, "year_built": 2000}},
        "insured": {"age": 45}
    }
    q = client.post('/v1/quote', json=payload).get_json()
    rv = client.post('/v1/policy/bind', json={'quote_id': q['quote_id']})
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['status'] == 'ACTIVE'
