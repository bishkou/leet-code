def wordPattern(pattern: str, s: str) -> bool:
    tab = s.split()
    if (len(pattern) != len(tab)):
        return False
    obj = {}
    word = {}
    i = 0
    for elt in pattern:

        if elt not in obj and tab[i] not in word:
            print('aaaa')
            obj[elt] = tab[i]
            word[tab[i]] = elt
        else:
            if elt in obj:
                if obj[elt] != tab[i]:
                    return False
            if tab[i] in word:
                if word[tab[i]] != elt:
                    return False

        i += 1
    return True


wordPattern('abba', "dog dog dog dog")
