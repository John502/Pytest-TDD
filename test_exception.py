from pytest import raises


# Test that an execption has occured
def raisesValueException():

    raise ValueError

def test_exception():
    with raises(ValueError):
        raisesValueException()