from pytest import approx

#Floating point error
# Comparing a fracntional with flpast
#approx allows it to pass
def test_float():
    assert (0.1 + 0.2) == approx(0.3)