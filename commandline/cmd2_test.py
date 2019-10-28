#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A template for a Cmd2-derived command processor.

See the package documentation in PyPI.
"""
import cmd2


class App(cmd2.Cmd):
    # multilineCommands = ['orate']
    # Cmd.shortcuts.update({'*': 'sneeze', '~': 'squirm'})
    # maxrepeats = 3
    # Cmd.settable.append('maxrepeats')

    # def __init__(self):
    #   cmd2.Cmd.__init__(self)
    # prompt = "->"
    # continuation_prompt = ">"
    # define more shortcuts
    # self
    # self.echo = True
    # default_to_shell= False
    # debug = True
    # app.multilineCommands

    # cmd2 passes arg to a do_ method (or default`) as a ParsedString,
    # a subclass of string that includes an attribute parsed.
    # parsed is a pyparsing.ParseResults object produced by applying a
    # pyparsing grammar applied to arg.
    def do_parsereport(self, arg):
        self.stdout.write(arg.parsed.dump() + "\n")

    # print output calls:
    # self.poutput('output'), self.pfeedback('message'), and
    # self.perror('errmsg')

    # options
    # @options([make_option('-p', '--piglatin', action="store_true", help="atinLay"),
    # make_option('-s', '--shout', action="store_true", help="N00B EMULATION MODE"),
    # make_option('-r', '--repeat', type="int", help="output [n] times")
    # ])
    # def do_speak(self, arg, opts=None):
    # """Repeats what you tell me to."""
    # arg = ''.join(arg)
    # if opts.piglatin:
    # arg = '%s%say' % (arg[1:].rstrip(), arg[0])
    # if opts.shout:
    # arg = arg.upper()
    # repetitions = opts.repeat or 1
    # for i in range(min(repetitions, self.maxrepeats)):
    # self.stdout.write(arg)
    # self.stdout.write('\n')

    # select - presents a numbered menu to the user.
    # def do_eat(self, arg):
    # sauce = self.select('sweet salty', 'Sauce? ')
    # result = '{food} with {sauce} sauce, yum!'
    # result = result.format(food=arg, sauce=sauce)
    # self.stdout.write(result + '\n')

    help = """
Commands:
?
  help
quit, q, exit

!
  shell: run as OS-level command
history [arg]
    Lists past commands issued
    no arg: list all
    arg is integer: list one history item, by index
    arg is string: string search
    arg is /enclosed in forward-slashes/: regular expression search
list [arg]
    Lists last command issued
    no arg -> list most recent command
    arg is integer -> list one history item, by index
    a..b, a:b, a:, ..b -> list spans from a (or start) to b (or end)
    arg is string -> list all commands matching string search
    arg is /enclosed in forward-slashes/ -> regular expression search
run [arg]
    Re-runs an earlier command
    no arg -> run most recent command
    arg is integer -> run one history item, by index
    arg is string -> run most recent command by string search
    arg is /enclosed in forward-slashes/ -> run most recent by regex
load
    Runs script of command(s) from a file or URL.
@
    Load script file
@@
    load script file; filename is relative to current script location
save [N] [filename.ext]
    Saves command from history to file.
    N => Number of command (from history), or *; most recent command if omitted
edit
    ed: edit most recent command in text editor
    ed [N]: edit numbered command from history
    ed [filename]: edit specified file name
    Commands are run after editor is closed
set edit (program-name)
    Control which editing program is used
set --long
    Print a list of all user-settable parameters, with brief comments
py
    Run its arguments as a Python command.
    Entered without arguments, it enters an interactive Python session
pause
    Displays the specified text then waits for the user to press RETURN.

By default, all command names are case-insensitive.

The command line will accept shortened command names so long as there is no ambiguity.

Comments are omitted from the argument list.
By default, both Python-style and C-style comments are recognized: # and /* */

As in a Unix shell, output of a command can be redirected:
    sent to a file with >, as in mycommand args > filename.txt
    piped (|) as input to operating-system commands, as in mycommand args | wc
    sent to the paste buffer, ready for the next Copy operation, by ending with a bare >, as in mycommand args >.. Redirecting to paste buffer requires software to be installed on the operating system, pywin32 on Windows or xclip on *nix.

You can send commands to your app as you invoke it by including them as extra arguments to the main program.
Each argument is interpreted as a separate command, so you should enclose each command in quotation marks if it is more than a one-word command.
"""


def main():
    a = App()
    a.cmdloop()


if __name__ == "__main__":
    main()
