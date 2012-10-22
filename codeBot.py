__author__ = 'gbin'

import requests
from errbot.botplugin import BotPlugin
from errbot import botcmd
from codepad import CodePad

class CodeBot(BotPlugin):

    @botcmd
    def python(self, mess, args):
        """ Execute the python expression """
        return CodePad(args).eval()

    @botcmd
    def c(self, mess, args):
        """ Execute the c expression """
        return CodePad(args, lang='C').eval()

    @botcmd
    def cpp(self, mess, args):
        """ Execute the c++ expression """
        return CodePad(args, lang='C++').eval()

    @botcmd
    def scheme(self, mess, args):
        """ Execute the scheme expression """
        return CodePad(args, lang='Scheme').eval()

    @botcmd
    def hs(self, mess, args):
        """ Evaluate the Haskell expression in ghci (tryhaskell.org) """
        r = requests.get("http://tryhaskell.org/haskell.json", params={'method':'eval', 'expr':args}).json
        if r.has_key('result'):
            return r['result'] + " :: " + r['type']
        else:
            return r['error']

    @botcmd
    def haskell(self, mess, args):
        """ Execute the Haskell module """
        return CodePad(args, lang='Haskell').eval()

# vim:expandtab
