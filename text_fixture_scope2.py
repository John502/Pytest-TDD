import pytest

#Rus
@pytest.fixture(scope="module", autouse=True)
def setup_module2():
    print("Setup module2")

@pytest.fixture(scope="class", autouse=True)
def setup_class2():
    print("setup_class2")

@pytest.fixture(scope="function", autouse=True)
def setup_function2():
    print("setup_function2")

class TestClass:

    def test_it(self):
        print("TestIt")
        assert True

    def test_it2(self):
        print("Testit2")
        assert True