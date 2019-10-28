def decorate(f):
    print("in decorator")

    def wrapper(*args):
        print("in wrapper")
        return f(*args)

    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper


@decorate
def g():
    print("in g")
    return True


class A(object):
    @staticmethod
    def f():
        print("in f")
        return True

    @decorate
    def h(self):
        print("in h")
        return True


def test_A_f():
    a = A()
    assert a.f()
    assert A.f()


def test_g():
    assert g()


def test_A_h():
    a = A()
    assert a.h()
