import pytest
from src import user_db


@pytest.fixture
def test_db():
    db = user_db.UserDb("tests/artifacts/pytest_test.db")
    yield db
    db.execute("delete from users")
    db.close()
