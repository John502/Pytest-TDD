import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    retVal = request.param
    print("\n Setup! retVal = {}".format(retVal))

def test1(setup):
    """
    test_fixture_return_params.py
    
     Setup! retVal = 1
    .
    setup = None

     Setup! retVal = 2
    .
    setup = None

     Setup! retVal = 3
    .
    setup = None


    :param setup: pytext fixture
    :return:
    """
    print("\nsetup = {}".format(setup))
    assert True