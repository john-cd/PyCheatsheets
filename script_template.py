#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on May 23, 2014
@author: Sylvain
"""

import argparse
import sys

# import logging


class Script(object):
    """
    Script argument processing
    0) -h for help, -v for version
    1) Arguments should be a list of .ibw files
    1) Arguments that start with @ will be treated as (text) files, and will be replaced by their contents
    (use when storing a list of files in a text file)
    """

    log_level = 0

    def __init__(self):
        filetype = "IGOR Binary Wave (.ibw) file"
        self.parser = argparse.ArgumentParser(
            description="open Igor .ibw files and display as superposed 3D perspectives",
            # allow / as a prefix for optional argument
            # prefix_chars='-/',
            fromfile_prefix_chars="@",
            version="%(prog)s 0.1",
        )
        # positional argument
        self.parser.add_argument(
            "infiles",
            metavar="FILE",
            nargs="+",  # one or more file arguments allowed
            # open the listed files
            type=argparse.FileType("rb"),
            # default=sys.stdin, # default if no file is
            # standard input (use with nargs='*')
            help="input {}".format(filetype),
        )

    # optional arguments
    # self.parser.add_argument('-o', metavar='IMAGE_FILE',
    # type=argparse.FileType('wb'),
    # default=sys.stdout,
    # help='output image'
    #           )
    # self.parser.add_argument('-V', '--verbose', action='count', default=0, help='increment verbosity')

    def run(self, *args, **kwargs):
        args = self.parser.parse_args(*args, **kwargs)
        print(args)
        # if args.verbose > 1:
        # log_level = self.log_levels[min(args.verbose-1, len(self.log_levels)-1)]
        # logging.setLevel(log_level)
        # self._run(args)

    def _run(self, args):
        raise NotImplementedError()


def main():
    script = Script()
    script.run()


if __name__ == "__main__":
    main()
