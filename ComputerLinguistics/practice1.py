vowels = list('аеиоуыэюя')
PERFECTIVE_GERUND_1 = ('в', 'вши', 'вшись')
PERFECTIVE_GERUND_2 = ('ив', 'ивши', 'ившись', 'ыв', 'ывшись', 'ыв')
ADJECTIVE = ('ее', 'ие', 'ые', 'ое', 'ими', 'ыми', 'ей', 'ий', 'ый',
             'ой', 'ем', 'им', 'ым', 'ом', 'его', 'ого', 'ему', 'ому',
             'их', 'ых', 'ую', 'юю', 'ая', 'яя', 'ою', 'ею')
PARTICIPLE_1 = ('ем', 'нн', 'вш', 'ющ', 'щ')
PARTICIPLE_2 = ('ивш', 'ывш', 'ующ')
REFLEXIVE = ('ся', 'сь')
VERB_1 = ('ла', 'на', 'ете', 'йте', 'ли', 'ий',
          'л', 'ем', 'н', 'ло', 'но', 'ет',
          'ют', 'ны', 'ть', 'ешь', 'нно')
VERB_2 = ('ила', 'ыла', 'ена', 'ейте', 'уйте', 'ите', 'или', 'ыли', 'ей', 'уй',
          'ил', 'ыл', 'им', 'ым', 'ен', 'ило', 'ыло', 'ено', 'ят', 'ует',
          'уют', 'ит', 'ыт', 'ены', 'ить', 'ыть', 'ишь', 'ую', 'ю')
NOUN = ('а', 'ев', 'ов', 'ие', 'ье', 'е', 'иями', 'ями', 'ами',
        'еи', 'ии', 'и', 'ией', 'ей', 'ой', 'ий', 'й', 'иям',
        'ем', 'ам', 'ом', 'о', 'у', 'ах', 'иях', 'ях', 'ы',
        'ь', 'ию', 'ью', 'ю', 'ия', 'ья', 'я', 'ям', 'ием')
SUPERLATIVE = ('ейш', 'ейше')
DERIVATIONAL = ('ост', 'ость')


def porterAlg(word):
    RV, R1, R2 = '', '', ''
    for i in range(len(word) - 1):
        if word[i] in vowels:
            if not RV:
                RV = word[i+1:]
            if word[i + 1] not in vowels:
                if not R1:
                    R1 = word[i+2:]
                    break
    for i in range(len(R1) - 1):
        if R1[i] in vowels and R1[i+1] not in vowels:
            R2 = R1[i+2:]
            break
    return (RV, R1, R2)


def removeSuffix(word, suffixes, letters: tuple=('', )):
    found = []

    for end in suffixes:
        if word.endswith(end):
            # print(end, word[-len(end)-1:-len(end)])
            if not letters[0]:
                found.append(end)
            elif word[-len(end)-1:-len(end)] in letters:
                found.append(end)

    if found:
        # print(found)
        max_length = max([len(suf) for suf in found])
        # print(max_length)
        return word[:-max_length]
    return word


def rootSearch(rv: str):
    root = rv
    length = len(rv)
    root = removeSuffix(root, PERFECTIVE_GERUND_1, ('а', 'я'))
    root = removeSuffix(root, PERFECTIVE_GERUND_2)
    if len(root) != length:
        return root

    root = removeSuffix(root, REFLEXIVE)

    root = removeSuffix(root, ADJECTIVE)
    root = removeSuffix(root, PARTICIPLE_2)
    root = removeSuffix(root, PARTICIPLE_1, ('а', 'я'))
    length = len(root)
    if len(root) != length:
        return root
    root = removeSuffix(root, VERB_2)
    root = removeSuffix(root, VERB_1, ('а', 'я'))
    if len(root) != len(rv):
        return root
    root = removeSuffix(root, NOUN)

    return root


def deleteOtherSuffixes(root, r2):
    if root.endswith('и'):
        root = root[:-1]

    suffixes = []
    for suffix in DERIVATIONAL:
        if r2.endswith(suffix):
            suffixes.append(suffix)

    if suffixes:
        max_length = max([len(suffix) for suffix in suffixes])
        root = root[:-max_length]

    if root.endswith('нн'):
        root = root[:-1]

    root = removeSuffix(root, SUPERLATIVE)

    if root.endswith('нн'):
        root = root[:-1]

    if root.endswith('ь'):
        root = root[:-1]

    return root


def main():
    with open('words.txt', encoding='utf8') as file:
        words = file.read().lower().split('\n')

    test_word = 'противоестественным'
    for word in words:
        RV, R1, R2 = porterAlg(word)
        root = deleteOtherSuffixes(rootSearch(word), R2)
        print(root)


if __name__ == '__main__':
    main()