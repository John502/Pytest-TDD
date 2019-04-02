

def test_AssertTrue():
     print("it's A test")
     assert True

def test_AssertFalse():
     print("it's another test!")
     assert True

#Xunit    Style Setup

#Called before each test
def setup_function(function):

     pass

#Called afer each unit test
def teardown_function(function):

     pass

# Called before any  test
def setup_module(function):
     print("\nSetup module")


# Called after each unit test
def teardown_module(function):
     print("\nTear down module")

#pytest -v -s