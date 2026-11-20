def compress(chars):
    ecriture = 0
    lecture = 0

    while lecture < len(chars):
        lettre = chars[lecture]
        debut = lecture

        while lecture < len(chars) and chars[lecture] == lettre:
            lecture += 1
        compte = lecture - debut

        chars[ecriture] = lettre
        ecriture += 1

        if compte > 1:
            for chiffre in str(compte):
                chars[ecriture] = chiffre
                ecriture += 1

    return ecriture


if __name__ == "__main__":
    c = list("aabbccc")
    n = compress(c)
    assert n == 6 and c[:n] == ["a", "2", "b", "2", "c", "3"]

    c = list("a")
    n = compress(c)
    assert n == 1 and c[:n] == ["a"]

    c = list("abbbbbbbbbbbb")
    n = compress(c)
    assert n == 4 and c[:n] == ["a", "b", "1", "2"]

    print("string_compression : OK")
