

# Doubles

# Dummy - objects that can be pased around as necessary but do not have any
#   type of test implementation and should never be used

# Fake - These object generally have a simplified functional implementation
#   of a particular interface that is adequate for testing but not for prod

# Stubs - These objects provide implementations with canned answers that are
#   suitable for the test

# Spies - These objects provide implementations that record the values that were
#   passed in so they can be used by the test

# Mocks - These objects are pre-programmed to expect specific calls and
#   parameters

#   assert_called - assert the mock was called
#   assert_called_once - assert the mock was called once
#   assert_called_with - assert the last call to the mock was with the specified
#       parameters
#   assert_called_once_with - Assert the mock was called once with the specified
#       parameters
#   assert_any_call - Assert the mock was ever called with the specified
#       parameters
#   assert

#   Magic Mock - derived from Mock but it has some of the default magic
#       functions from each class
#
#   Pytest Monkeypatch Test Fixture
#    dynamically replace
#       module and class attributes
#       Dictionary entries
#       Environment variables
