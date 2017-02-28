
## shlex example: see http://pymotw.com/2/shlex/  
## simple lexer (e.g. for command-line utilities)
         
import shlex

def test_shlex():
    text = """ stuff much # comment"""
    print 'ORIGINAL:', repr(text)
    print
    print 'TOKENS:'
    print shlex.split(text)

##
def test_shlex2():
    text = """a,b source more.txt # comment"""
    lexer = shlex.shlex(text)  # consider posix=True
    lexer.wordchars += '.'     # '.' is not a delimiter. In some situations, add ._-\ 
    lexer.source = 'source'    # Since the source property of the lexer is set to “source”, when the keyword is encountered the filename appearing in the next title is automatically included.
    lexer.whitespace += ','   # control the whitespace characters used to split words. 
    print 'TOKENS:'
    try:
        for token in lexer:
            print repr(token)
    except ValueError as err:
        first_line_of_error = lexer.token.splitlines()[0]
        print 'ERROR:', lexer.error_leader(), str(err), 'following "' + first_line_of_error + '"'

