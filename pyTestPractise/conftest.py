import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed at last")

def test_kal(setup):
    print("i will execute steps in kal method")

