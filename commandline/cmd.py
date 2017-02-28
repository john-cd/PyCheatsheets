
import cmd
import sys
import os

## Minimum implementation of a Cmd-derived command line processor:
# class Command(cmd.Cmd):

    # def do_greet(self, line):
        # print line

    # def do_q(self, line):
        # return True

# if __name__ == '__main__':
    # Command().cmdloop()            

#-------------------------------------------------------------------------------

class HelloWorld(cmd.Cmd):
    """Simple command processor with line completion."""
    
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    
    def do_greet(self, person):
        "Greet the person"
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = 'hello'
        print greeting
    
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions
    
    def do_q(self, line):
        return True

def main(): 
    HelloWorld().cmdloop()
    
if __name__ == '__main__':
    main()
    