
import pytest

#two methods of pass teardwown code

@pytest.fixture()
def setup1():
    print("\n Setup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture()
def setup2(request):

    print("\n Setup 2")

    def teardown_a():
        print("Teadown A")

    def teardown_b():
        print("Teardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing test1!")
    assert True

def test2(setup2):
    print("Executing test2!")
    assert True