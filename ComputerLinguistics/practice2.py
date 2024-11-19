import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP
    V -> 'принес' | 'saw'
    NP -> 'masha' | 'петя' | Det N
    Det -> 'с'
    N -> 'пес'
""")
sent = list('петя принес пес с masha'.split())
print(sent)
parser = nltk.ChartParser(grammar)
trees = parser.parse(sent)
for tree in trees:
    print(tree)