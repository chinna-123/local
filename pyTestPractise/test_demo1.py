import pytest


@pytest.mark.smoke
def test_example(setup):
    print("hello")
    # assert 1 + 1 == 2
def test_add(setup):
    print("gud morning")
def test_sun(setup):
    a = 10
    b = 20
    assert a == b

@pytest.mark.smoke
def test_credit(setup):
    a = 10
    b = 10
    print(a)
    assert a == b
