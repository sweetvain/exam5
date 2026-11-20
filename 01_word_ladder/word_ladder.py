from collections import deque


def ladderLength(beginWord, endWord, wordList):
    mots = set(wordList)
    if endWord not in mots:
        return 0

    file = deque([(beginWord, 1)])
    mots.discard(beginWord)

    while file:
        mot, longueur = file.popleft()
        if mot == endWord:
            return longueur

        for i in range(len(mot)):
            for lettre in "abcdefghijklmnopqrstuvwxyz":
                nouveau = mot[:i] + lettre + mot[i + 1:]
                if nouveau in mots:
                    mots.remove(nouveau)
                    file.append((nouveau, longueur + 1))
    return 0


if __name__ == "__main__":
    assert ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert ladderLength("a", "c", ["a", "b", "c"]) == 2
    print("word_ladder : OK")
