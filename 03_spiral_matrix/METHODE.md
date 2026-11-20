# 54. Spiral Matrix : méthode

## Le problème
Parcourir une matrice en **spirale** (vers la droite, vers le bas, vers la gauche, vers le haut, puis on recommence plus à l'intérieur) et renvoyer les valeurs dans l'ordre.

```
1 2 3
4 5 6   →  [1, 2, 3, 6, 9, 8, 7, 4, 5]
7 8 9
```

## L'idée à retenir : 4 bornes qui rétrécissent
> On garde 4 variables : `haut`, `bas`, `gauche`, `droite`. On parcourt le **bord** du rectangle, puis on rétrécit le rectangle d'une couche.

Mnémotechnique : **→ ↓ ← ↑** (droite, bas, gauche, haut), et après chaque côté on rapproche la borne correspondante :

| côté parcouru | direction | borne qu'on rétrécit |
|---|---|---|
| ligne du haut | → | `haut += 1` |
| colonne de droite | ↓ | `droite -= 1` |
| ligne du bas | ← | `bas -= 1` |
| colonne de gauche | ↑ | `gauche += 1` |

## Le code expliqué ligne par ligne

```python
haut, bas = 0, len(matrix) - 1
gauche, droite = 0, len(matrix[0]) - 1
```
Au départ, le rectangle = toute la matrice.

```python
while haut <= bas and gauche <= droite:
```
Tant qu'il reste au moins une case dans le rectangle.

```python
for j in range(gauche, droite + 1):
    resultat.append(matrix[haut][j])
haut += 1
```
**→** On lit la ligne du haut de gauche à droite. Puis on la "mange" : `haut += 1`.

```python
for i in range(haut, bas + 1):
    resultat.append(matrix[i][droite])
droite -= 1
```
**↓** On descend la colonne de droite (on commence à `haut`, déjà incrémenté, pour ne pas relire le coin). Puis `droite -= 1`.

```python
if haut <= bas:
    for j in range(droite, gauche - 1, -1):
        resultat.append(matrix[bas][j])
    bas -= 1
```
**←** On lit la ligne du bas de droite à gauche (`range(..., -1)` pour reculer ; `gauche - 1` car la borne de fin est exclue). Le `if` est **indispensable** : si la matrice n'a plus de ligne à ce stade (ex. une seule ligne), on relirait la même ligne à l'envers.

```python
if gauche <= droite:
    for i in range(bas, haut - 1, -1):
        resultat.append(matrix[i][gauche])
    gauche += 1
```
**↑** On remonte la colonne de gauche. Le `if` empêche de relire la même colonne dans le cas d'une seule colonne.

## Pourquoi les deux `if` ?
Après avoir rétréci `haut` et `droite`, le rectangle peut être vide ou réduit à une ligne / colonne. Sans ces tests, on duplique des valeurs.
Exemple `[[1,2,3]]` : sans le `if`, on obtiendrait `[1,2,3,2,1]`.

## Exemple pas à pas (3×3)
1. → : 1 2 3, haut=1
2. ↓ : 6 9, droite=1
3. ← : 8 7, bas=1
4. ↑ : 4, gauche=1
5. Le rectangle est maintenant la case centrale : → : 5. Fin.

## Complexité
- Temps O(m × n), mémoire O(1) hors résultat.

## Pièges
- Oublier les deux `if` (bug sur une ligne ou colonne seule).
- `range(droite, gauche - 1, -1)` : le `-1` après `gauche` est classique à oublier.
