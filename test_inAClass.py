import pytest

class TestClass:

    @classmethod
    def setup_class(cls):
        print("Setup TestClass!")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass!")


    #Executed only before each unit test 
    def setup_method(self, method):
        if method == self.test1:
            print("Setting up test1")
        elif method == self.test2:
            print("Setting up test2")
        else:
            print("Setting up unknown test!")

    #Executed only after any test is run
    def teardown_method(self, method):
        if method == self.test1:
            print("Tearing down test1")
        elif method == self.test2:
            print("Tearing down test2")
        else:
            print("Tearing down unknown test!")


    def test1(self):

        print("Executing test1!")
        assert True

    def test2(self):

        print("Executing test2!")
        assert True