import pytest


@pytest.fixture(scope="session")
def preSetUpWork():
    print("I setup browser instance")