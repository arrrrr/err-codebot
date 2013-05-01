__author__ = 'gbin'

import requests
from errbot.botplugin import BotPlugin
from errbot.utils import get_sender_username
from errbot import botcmd
from codepad import CodePad

def trollguard(func):
    def helper(self, mess, args):
        output = func(self, mess, args)
        if len(output) > 8000:
            return "How appropriate, you code like a cow, {0}!".format(get_sender_username(mess))
        else:
            return output
    helper.__name__ = func.__name__ # hrrrgh!
    return helper

class CodeBot(BotPlugin):
    @botcmd
    @trollguard
    def python(self, mess, args):
        """ Execute the python expression """
        return CodePad(args).eval()

    @botcmd
    @trollguard
    def c(self, mess, args):
        """ Execute the c expression """
        return CodePad(args, lang='C').eval()

    @botcmd
    @trollguard
    def cpp(self, mess, args):
        """ Execute the c++ expression """
        return CodePad(args, lang='C++').eval()

    @botcmd
    @trollguard
    def scheme(self, mess, args):
        """ Execute the scheme expression """
        return CodePad(args, lang='Scheme').eval()

    @botcmd
    @trollguard
    def hs(self, mess, args):
        """ Evaluate the Haskell expression in ghci (tryhaskell.org) """
        r = requests.get("http://tryhaskell.org/haskell.json", params={'method':'eval', 'expr':args}).json()
        if 'result' in r:
            return "{0} :: {1}".format(r['result'], r['type'])
        else:
            return "{0}: {1}".format(*list(r.items())[0])

    @botcmd
    @trollguard
    def haskell(self, mess, args):
        """ Execute the Haskell module """
        return CodePad(args, lang='Haskell').eval()

# vim:expandtab
