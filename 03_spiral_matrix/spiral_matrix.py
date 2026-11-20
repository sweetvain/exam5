def spiralOrder(matrix):
    resultat = []
    haut, bas = 0, len(matrix) - 1
    gauche, droite = 0, len(matrix[0]) - 1

    while haut <= bas and gauche <= droite:
        for j in range(gauche, droite + 1):
            resultat.append(matrix[haut][j])
        haut += 1

        for i in range(haut, bas + 1):
            resultat.append(matrix[i][droite])
        droite -= 1

        if haut <= bas:
            for j in range(droite, gauche - 1, -1):
                resultat.append(matrix[bas][j])
            bas -= 1

        if gauche <= droite:
            for i in range(bas, haut - 1, -1):
                resultat.append(matrix[i][gauche])
            gauche += 1

    return resultat


if __name__ == "__main__":
    assert spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiralOrder([[1]]) == [1]
    assert spiralOrder([[1, 2, 3]]) == [1, 2, 3]
    assert spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    print("spiral_matrix : OK")
