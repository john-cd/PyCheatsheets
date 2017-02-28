"""Quick code snippets for embedding IPython into other programs.
"""

### See "embed IPython in your code":
# http://ipython.org/ipython-doc/stable/interactive/reference.html#embedding-ipython

#---------------------------------------------------------------------------
# This code loads IPython but modifies a few things if it detects it's running
# embedded in another IPython session (helps avoid confusion)

# IPython, when running, injects get_ipython into builtins, so you can know if you have nested
# copies running.
try:
    get_ipython
except NameError:
    banner=exit_msg=''
else:
    banner = '*** Nested interpreter ***'
    exit_msg = '*** Back in main IPython ***'

# First import the embed function
from IPython.terminal.embed import InteractiveShellEmbed
# Now create the IPython shell instance. Put ipshell() anywhere in your code
# where you want it to open.
ipshell = InteractiveShellEmbed(banner1=banner, exit_msg=exit_msg)


def do_something():
    ipshell('*** call IPython.')
    
do_something()    