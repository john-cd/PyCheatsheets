#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Created on June 2

@author: Sylvain
"""
# 
# http://pymotw.com/2/cmd/

import cmd
import readline  # to automatically inherit bash-like history-list editing

class CommandProcessor(cmd.Cmd):
    """Command processor."""
    
    ## Command prompt
    prompt = "3D View >"
    ## “Welcome” message printed at the start of the program
    intro = """3D View:

Type "help" (without quotes) for available commands.

Use the top/down/left/right arrows for command history and editing.
Control-P scrolls back to the last command, Control-N forward to the next one, Control-F moves the cursor to the right non-destructively, Control-B moves the cursor to the left non-destructively.

Hitting the tab key at an input prompt triggers completion. When multiple completions are possible, pressing tab twice prints a list of the options. 

Typing Ctrl-D or "q" will exit.

"""
    ## The header to issue if the help output has a section for documented commands.
    # doc_header = 'doc_header'
    ## The header to issue if the help output has a section for miscellaneous help topics (that is, there are help_*() methods without corresponding do_*() methods).
    # misc_header = 'misc_header'
    ## The header to issue if the help output has a section for undocumented commands
    # undoc_header = 'undoc_header'
    ## Character used to draw separator lines under the help-message headers.
    ruler = '-'
    
    # def do_greet(self, person):
        # if person:
            # print "hi,", person
        # else:
            # print 'hi'
    
    ## Alternative to docstring for help:
    # def help_greet(self):
        # print '\n'.join([ 'greet [person]',
                           # 'Greet the named person',
                           # ])
    
    # FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    ## Assemble a list of possible completions 
    # def complete_greet(self, text, line, begidx, endidx):
        # if not text:
            # completions = self.FRIENDS[:]
        # else:
            # completions = [ f
                            # for f in self.FRIENDS
                            # if f.startswith(text)
                            # ]
        # return completions

    def do_something(self, line):
        """Do something."""
        pass

    # mapped to ! command
    def do_shell(self, line):
        """Run a shell command (prefix your command with !)."""
        print "Running shell command:", line
        output = os.popen(line).read()
        print output
        self.last_output = output

    def do_q(self, line):
        """Exit."""
        return True

    # mapped to Ctrl + D
    def do_EOF(self, line):
        """Exit."""
        return True

    # def postloop(self):
        # print

        
## main() ###########################
def main():
    CommandProcessor().cmdloop()    
   
if __name__ == '__main__':
    main()