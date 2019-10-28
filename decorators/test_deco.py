# http://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python

import sys
import io


def assert_output(func, desiredoutput):
    saved_stdout = sys.stdout
    try:
        sys.stdout = out = io.StringIO()
        res = func()
        output = out.getvalue().strip()
        print(output)
        assert output == desiredoutput
        return res
    finally:
        sys.stdout = saved_stdout


def test_catch():
    import decorators.deco

    @decorators.deco.catch
    def f():
        # this Exception should be caught and displayed.
        raise ValueError("some error")

    f()


# def test_no_arg():
# class A:
# @deco.no_arg
# def func(self, line):
# """some doc"""
# return "someval"
# a = A()
# assert a.func(None) == "someval"
# assert a.func([]) == "someval"
# assert a.func("") == "someval"
# assert a.func("not expected") == ""
# assert a.func.__doc__ == "some doc"


def main():
    test_catch()


if __name__ == "__main__":
    main()
