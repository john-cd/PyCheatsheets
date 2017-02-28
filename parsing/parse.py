"""
Example code for argument (command line) parsing and checking.
"""
# import utils
# import commandline
import os
import logging
log = logging.getLogger(__name__)


class ParseOptions(object):
    """
    A container for parsing options.
    """
    def __init__(self, has_argument, msg_arg, file_existence, msg_existence, default_ext):
        super(ParseOptions, self).__init__()
        self.has_argument = has_argument   # True if a non-empty 'line' argument must be provided."""
        self.msg_arg = msg_arg                         # The message to display if the "line" argument is empty("") but should not (or vice versa).
        self.file_existence = file_existence           # True if the argument is a file path and the file must exist, False if it must not exist, None if we don't care / not a file path
        self.default_ext = default_ext  # default extension of the file, if not provided

        ## Better require a non-empty argument before checking its existence as a file path.
        log.debug("ParseOptions: self.file_existence: %s", self.file_existence)
        log.debug("ParseOptions: self.has_argument: %s", self.has_argument)
        if self.file_existence is not None:
            assert self.has_argument

        ## Message defaults
        if self.msg_arg is None:
            if self.file_existence is None:
                self.msg_arg = "This command requires an argument." if self.has_argument else "This command takes no argument."
            else:
                self.msg_arg = "No file name or path was specified."

        default_msg_existence = "The file {0} does not exist." if self.file_existence else "The file {0} already exists."
        self.msg_existence = default_msg_existence if msg_existence is None else msg_existence

def parse(line, options):
    """Argument parsing and checking."""
    assert isinstance(options, ParseOptions)
   ## does it have an argument if needed? none if not needed?
    if (line is None or line == "") == options.has_argument:
        raise SyntaxError(options.msg_arg)
    ##
    args = []
    if isinstance(line, basestring):
        ## Separate command line into individual tokens and remove comments
        ## then parse tokens to proper type (e.g. int, float, str otherwise)
        tokens = [] 
        # TODO parse the command line e.g. utils.parse_str(token) for token in commandline.lex(line)]
        # Best implemented usig pyparsing rather than shlex + custom code
        
        if options.file_existence is not None:
            ## The argument should be file name / path(s)
            ## expand path and add extension if needed
            file_paths = [token for token in tokens] 
            # TODO utils.topath(token, default_ext=options.default_ext)
            for file_path in file_paths:
                if options.file_existence != os.path.exists(file_path):
                    raise SyntaxError(options.msg_existence.format(file_path))
            tokens = file_paths

        args.extend(tokens)
    else:
        ## Default behaviour: pass the line argument without transformation
        args.append(line)
    return args

### Decorators ----------------------------------------------------------------

import inspect
import functools

class parsecmd(object):
    """Decorator class that parses a single command line argument into multiple
    function arguments, optionally expanding file paths and checking for file existence."""
    def __init__(self, has_argument=True, msg_arg=None, file_existence=None, msg_existence=None, default_ext=".txt"):
        self._options = ParseOptions(has_argument, msg_arg, file_existence, msg_existence, default_ext)

    def __call__(self, func):
        """
        
        :param func: a function with signature (self, arg1, arg2...)
        :return: a function with signature (self, line) where 'line' is the command line to parse."""
        @functools.wraps(func)
        def wrapper(self2, line):
            try:
                args = parse(line, self._options)  # may throw SyntaxError

                ## Checks that the number of arguments match:
                argspec = inspect.getargspec(func)
                ## argspec is a namedtuple ArgSpec(args, varargs, keywords, defaults)
                if len(argspec.args) != len(args) + 1:
                    raise SyntaxError("Wrong number or wrong type of arguments in the command line.\nExpected {0}. Got: self, {1}".format(argspec.args, args))

                log.debug("parsecmd: func: %s", inspect.getcallargs(func, *args))
                ## debugging: getcallargs returns a dict containing args and kwds
                ## bound to the argument names, as if the function was called with them.

                ## finally, run the wrapped function:
                return func(self2, *args)
            except StandardError as err:
                ## MAIN EXCEPTION CATCH for commands.
                print err
                log.exception("parsecmd: exception: %s", err)
                ## FUTURE consider: e.args
                # if e.message:
                    # print e.message
                # else:
                    # print e
        ##~~~
        return wrapper

### testing code -------------------------------------------------------------
# from ..TODO import parsecmd

def test_parse():
    """Nose test  """
    @parsecmd()
    def f(self, firstarg):
        return self, " ", firstarg
    f("a class instance", "onearg")

    @parsecmd()
    def g(self, firstarg, secondarg):
        return " ".join([self, firstarg, str(secondarg)])
    g("a class instance", "first 2")
    ## the command line is split into two arguments, the latter converted to int
    ## TODO low pri test f("") - print error message:

