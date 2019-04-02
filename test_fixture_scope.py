import pytest


#Runs when you run pytest from command line
#as you begin to run all unit tests
@pytest.fixture(scope="session", autouse=True)
def setup_session():
    print("\n Setup Session")

#Runs as the module setups (this file)
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    print("\n Setup module")

#Runs before each unit test
@pytest.fixture(scope="function", autouse=True)
def setup_function():
    print("\n Setup function")

def test1():
    print("Executing test 1")
    assert True

def test2():
    print("Executing test 2")
    assert True
