# Argument Injection --------------------------------------------------------

from decorator import decorator


@decorator
def inject(func, *args, **kw):
    # if not present, pass to "func" an "added" argument
    if "added" not in kw:
        kw.update({"added": 1})
    return f(*args, **kw)


# Usage:
# @inject
# def dosomething(arg):
# print arg
# or:
# @inject
# def dosomething(**kw):
# print kw["wavesdict"]
# dosomething()

# Variable function argument manipulation ------------------------------------


def f(func, *args, **kw):
    # first expected argument is "self", a class instance.
    if len(args) >= 1:
        self_arg, self_defined = args[0], True
    elif "self" in kw:
        self_arg, self_defined = kw["self"], True
    else:
        self_arg, self_defined = None, False
    # second expected argument is "line", a string which can be empty.
    if len(args) >= 2:
        line_arg, line_defined = args[1], True
    elif "line" in kw:
        line_arg, line_defined = kw["line"], True
    else:
        line_arg, line_defined = None, False

    new_args = []
    if self_defined:
        new_args.append(self_arg)
    if line_defined:
        if isinstance(line_arg, str):
            tokens = []  # lex tokens here: tokens = lex(line_arg)
            new_args.extend(tokens)
        else:
            new_args.append(line_arg)
    if len(args) >= 3:
        new_args.extend(args[2:])
    new_kw = {k: v for k, v in kw.items() if k not in ("self", "line")}
    return func(*new_args, **new_kw)
