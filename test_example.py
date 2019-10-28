# Example test module for nose

# run with: nosetests -v
# or: nosetests -s


# Simple test functions first:
def test_ok():
    print("test_ok")


# def fail_test():
# print "fail_test: will always fail"
# assert False

# Private functions are however not recognized:


def _test_notseen():
    print("_test_notseen")
    assert False


def _notseen_test():
    print("_notseen_test")
    assert False


# The following is reported as an ERROR (should have zero params):
# def test_notreally(something):
#    assert False

# test generators


def test_evens():
    for i in range(0, 5, 2):
        yield check_even, i


def check_even(n):
    assert n % 2 == 0


# test with setup, teardown methods


def setup_func():
    "set up test fixtures"


def teardown_func():
    "tear down test fixtures"


def test_with_setup():
    "test ... "


test_with_setup.setup = setup_func
test_with_setup.teardown = teardown_func
# or use decorator: @with_setup(setup_func, teardown_func)
# requires: from nose import with_setup


# module-level setup and teardown:
def setup_module(module):
    print("")  # this is to get a newline after the dots
    print("setup_module before anything in this file")


def teardown_module(module):
    print("teardown_module after everything in this file")


# test class
class TestA:
    def setup(self):
        print("TestA:setup() before each test method")

    def teardown(self):
        print("TestA:teardown() after each test method")

    @classmethod
    def setup_class(cls):
        print("setup_class() before any methods in this class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class() after any methods in this class")

    def test_numbers_5_6(self):
        print("test_numbers_5_6()")
        assert 5 * 6 == 30

    def test_strings_b_2(self):
        print("test_strings_b_2()")
        assert "b" * 2 == "bb"


# Optional API for cleaner output:

# from nose.tools import assert_equal
# from nose.tools import assert_not_equal
# from nose.tools import assert_raises
# from nose.tools import raises

# Nose finds and runs unittests with no problem, and with no extra steps.
# Nose can run doctests
