#fixtures
import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "fail"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup secondWork instance")
    yield #pause
    print("teardown validation")


@pytest.mark.smoke
def test_initialCheck(preWork,secondWork):
    print("This is first test")
    assert preWork =="fail"

@pytest.mark.skip
def test_SecondCheck(preWork,secondWork):
    print("This is second test")