import pytest
from flaskr import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True
    })

    yield app

@pytest.fixture
def client(app):
    yield app.test_client()

@pytest.fixture
def runner(app):
    yield app.test_cli_runner()