#Fixtures

import pytest

#Function which can be excuted in each test
# which can be passed as an argument

#
# all functions in executure setup prior to running
#
# @pytest.fixture(autouse=True)
#
@pytest.fixture()
def setup():

    print("\nSetup\n")

    #Teardown code each with yield
    # or request.addfinalizer(teardown)
    yield
    print("Teardown_from_setup")

#bothtests call fixture
def test1_fixturearg1(setup):

    print("\nExecuting test1_fixture_arg1!")
    assert True


@pytest.mark.usefixtures("setup")
def test2_fixture_arg2():

    print("Executing test2_fixture_arg2!")

#not call fixture
def test1_no_fixture():

    print("\nExecuting test1_no_fixture!")
    assert True

