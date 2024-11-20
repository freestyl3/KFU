import nltk
from nltk import CFG

grammar = CFG.fromstring("""
  S -> NP VP | VP NP | PP PP NP VP | PP PP VP NP
  NP -> Det Nom | PropN | Adj Nom | N | N VP | VP | Adj PropN
  Nom -> Adj Nom | N | PropN
  PP -> Det Nom | Nom
  VP -> V Nom | V Det Nom | V | V PP | V PP PP
  Det -> 'с' | 'во'
  N -> 'кот' | 'собака' | 'мячом' | 'телевизор' | 'дворе'
  V -> 'играет' | 'смотрит'
  Adj -> 'большой' | 'маленьким' | 'маленькая' | 'большим' | 'соседская'
  PropN -> 'Петя' | 'Маша'
""")

sentences = [
    'во дворе с мячом играет соседская Маша',
    # 'Петя смотрит телевизор',
    # 'большой кот играет с маленьким мячом',
    # 'маленькая собака играет с большим мячом',
    # 'Маша играет с мячом',
    # 'кот смотрит'
]
for sentence in sentences:
    sent = sentence.split()
    # print(sent)
    parser = nltk.ChartParser(grammar)
    trees = parser.parse(sent)
    for tree in trees:
        tree.draw()

    print()