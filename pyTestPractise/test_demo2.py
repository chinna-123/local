import pytest

@pytest.mark.xfail
def test_example(setup):
    msg = "hello"
    assert msg == "hye", "Test failed bcz the strings not matched"


@pytest.mark.smoke
# @pytest.mark.skip
@pytest.mark.xfail
def test_credit(setup):
    a = 10
    b = 20
    assert a == b

def test_kal(setup):
    print("i will execute steps in kal method")

