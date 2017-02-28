
## http://pyparsing.wikispaces.com/HowToUsePyparsing
## http://infohost.nmt.edu/tcc/help/pubs/pyparsing/web/index.html
## https://pythonhosted.org/pyparsing/
## Examples / Cookbook:
## http://www.ptmcg.com/geo/python/confs/pyCon2006_pres2.html
## http://wiki.scipy.org/Cookbook/Reading_Custom_Text_Files_with_Pyparsing
## http://www.onlamp.com/pub/a/python/2006/01/26/pyparsing.html?page=1
## http://pyparsing-public.wikispaces.com/FAQs

import os
import glob
import itertools
import logging
log = logging.getLogger(__name__)

from pyparsing import *       
## OR:
# import pyparsing as PP
## character classes:
# from pyparsing import printables, nums, alphanums, alphas
## Literals:
# from pyparsing import Literal, CaselessLiteral, oneOf
# from pyparsing import Keyword, CaselessKeyword
## Words:
# from pyparsing import Word, CharsNotIn
## Combinations:
# from pyparsing import Group, Optional, Combine
# from pyparsing import OneOrMore, ZeroOrMore
## + ^ & | operators; + and | match in order, ^ and & do not.
# from pyparsing import And, Or, Each, MatchFirst,  
## ~ operator; NotAny is the negative of FollowedBy
# from pyparsing import NotAny, FollowedBy
# Whitespaces
# from pyparsing import White  
## Quoted strings:
# from pyparsing import QuotedString, dblQuotedString, QuotedString, removeQuotes
## Lists:
# from pyparsing import delimitedList, commaSeparatedList
## Comments:
# from pyparsing import cStyleComment, cppStyleComment, restOfLine
# from pyparsing import stringEnd, StringEnd, LineEnd
## Advanced:
# from pyparsing import Regex
# from pyparsing import Dict, dictOf, Upcase
## Recursive grammar (use with << operator):  
# from pyparsing import Forward
# from pyparsing import ParseException
# from pyparsing import ParserElement, ParseResults

def parse(parser, input_):
    import view3d.parse as vp
    try:
        print parser.parseString(input_, parseAll=True).dump()  #.asList()
    except ParseException as err:
        msg = vp._ParseException_msg(err, input_) 
        print msg

def scan(parser, input_):
    for tokens, start, end in parser.scanString(input_):
        print "tokens: {} start: {} end: {}".format(tokens, start, end)
        
### Pyparsing Grammar --------------------------------------------------------

# parser.setDebug()
# (there is a trace method for parse actions)

## Literals:
# def makeLiteral(s,val):
    # """ """
    # ret = CaselessLiteral(s).setName(s)
    # return ret.setParseAction( replaceWith(val) )

## Character sets:
quoted_exclude = '\\:/|"<>'
unquoted_exclude = quoted_exclude + ",;#"  
unquoted_set = set(printables) - set(unquoted_exclude)
unquoted_chars = ''.join(unquoted_set)

nondigits = ''.join(set(printables) - set(nums))

## Words:
# excludeChars
Word(p.printables, excludeChars = r'\"' + "':/|<>,;#")

# Word that has at least one non-digit character
Combine(Optional(Word(nums)) + Word(alphas, alphanums))
# or: Combine(Optional(Word(nums + specials)) + Word(alphas + specials, printables, excludeChars=exclude)

## Regex 
# Word that has at least one non-digit character 
r = Regex("[0-9]*[a-z][a-z0-9]+")
# more complex regex
allowed_special_chars = "!@$%^&()-_+={}[]"
allowed_chars_regex = "[a-zA-Z0-9" + allowed_special_chars + "]+"
nondigits_regex = "[a-zA-Z" + allowed_special_chars + "]"
r2 = Regex(allowed_chars_regex + nondigits_regex + allowed_chars_regex)

# Lookahead:
# matches 61 but not 6a6
pat = Word(nums) + ~Word(alphas) + Word(nums) 

# SkipTo:
unwanted = SkipTo('#'|lineEnd)("unwanted") 
# see also: restOfLine


### Example Parse Actions .....................................................

# decimalNumber = Word(nums, nums+",") + Optional("." + OneOrMore(Word(nums)))

# convert_int = Word(nums).setParseAction( lambda tokens : int(tokens[0]) )
# joinTokens = lambda tokens : "".join(tokens)
# stripCommas = lambda tokens : tokens[0].replace(",", "")
# convertToFloat = lambda tokens : float(tokens[0])
# decimalNumber.setParseAction( joinTokens )
# decimalNumber.addParseAction( stripCommas )
# decimalNumber.addParseAction( convertToFloat )

# def validateDateString(tokens):
    # """
    # >>> date.setParseAction(validateDateString)
    # """
    # try
        # time.strptime(tokens[0], "%m/%d/%Y")
    # except ValueError,ve:
        # raise ParseException("Invalid date string (%s)" % tokens[0])

# def convert_prop_to_dict(tokens):
    # """ """
    # prop_dict = {}
    # for token in tokens:
        # prop_dict[token.property_key] = token.property_value
    # return prop_dict