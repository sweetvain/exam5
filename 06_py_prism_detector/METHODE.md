# py_prism_detector : méthode

## Le problème
Trouver toutes les occurrences d'un mot (`pattern`) dans une grille de lettres, dans les **8 directions**, et renvoyer `(ligne, colonne, code_direction)` du point de départ.

```python
prism_detector(["ABC","DEF","GHI"], "ADG")  →  [(0, 0, "V")]
```

## L'idée à retenir : un tableau de directions
> Une direction = un pas `(dr, dc)` = "de combien je bouge en ligne et en colonne à chaque lettre".

| code | (dr, dc) | sens |
|---|---|---|
| `H` | (0, 1) | → |
| `H-` | (0, -1) | ← |
| `V` | (1, 0) | ↓ |
| `V-` | (-1, 0) | ↑ |
| `D1` | (1, 1) | ↘ |
| `D1-` | (-1, -1) | ↖ |
| `D2` | (1, -1) | ↙ |
| `D2-` | (-1, 1) | ↗ |

**On écrit ce tableau une fois, dans l'ordre de l'énoncé**, et on n'a plus qu'à faire 3 boucles imbriquées : ligne → colonne → direction. L'ordre du résultat (ligne, colonne, direction) est alors automatiquement le bon.

Astuce pour retenir : `D1` = les deux pas ont le même signe, `D2` = signes opposés ; le `-` inverse les deux pas.

## Le code expliqué ligne par ligne

```python
if not grid or not pattern:
    return []
```
Grille vide ou motif vide → aucune occurrence.

```python
resultat = []
utilisees = set()
```
`resultat` = les réponses. `utilisees` = les cases déjà prises par un résultat (voir plus bas).

```python
for r in range(len(grid)):
    for c in range(len(grid[r])):
        for code, dr, dc in DIRECTIONS:
```
On essaie chaque case comme départ, dans chaque direction.

```python
cases = []
for k in range(len(pattern)):
    rr = r + dr * k
    cc = c + dc * k
```
La k-ième lettre est à `départ + k × pas`.

```python
    if not (0 <= rr < len(grid) and 0 <= cc < len(grid[rr])):
        break
    if grid[rr][cc] != pattern[k]:
        break
    cases.append((rr, cc))
```
Si on sort de la grille, ou si la lettre ne correspond pas : on abandonne cette direction (`break`). Sinon on mémorise la case.

```python
if len(cases) == len(pattern) and not utilisees & set(cases):
    resultat.append((r, c, code))
    utilisees.update(cases)
```
Si toutes les lettres ont correspondu, on a une occurrence. Elle n'est gardée que si **aucune de ses cases n'a déjà servi** dans un résultat précédent.

## Pourquoi `utilisees` ? (point important)
L'exemple de l'énoncé :

```python
prism_detector(["HELLO", "WORLD"], "LL")  →  [(0, 2, "H")]   # un seul résultat
```
Pourtant, « LL » existe aussi en lisant `HELLO` de droite à gauche depuis `(0,3)`, en diagonale `(0,2)→(1,3)` et en vertical vers le haut `(1,3)→(0,3)`. Comme l'énoncé n'en veut qu'un, la règle déduite est :

> **Une case ne peut appartenir qu'à un seul résultat.** Comme on parcourt dans l'ordre (ligne, colonne, direction), la première occurrence trouvée "réserve" ses cases.

⚠️ Cette règle est **déduite de l'exemple** (l'énoncé ne la dit pas explicitement). Si ta vraie consigne d'examen demande *toutes* les occurrences, même chevauchantes, il suffit de supprimer `utilisees` : la condition devient simplement `if len(cases) == len(pattern):`. Mais l'exemple `LL` ne passerait alors plus.

## Exemple pas à pas : `["XYZ","ABC","DEF"]`, `"XBF"`
Départ (0,0) `X`, direction `D1` (1,1) :
- k=0 → (0,0) = `X` ✔
- k=1 → (1,1) = `B` ✔
- k=2 → (2,2) = `F` ✔
→ `(0, 0, "D1")`.

## Complexité
- O(lignes × colonnes × 8 × len(pattern)).

## Pièges
- Tester les bornes **avant** d'accéder à `grid[rr][cc]` (sinon `IndexError`, ou pire : un index négatif Python qui "revient" de l'autre côté sans erreur).
- Respecter l'ordre des directions du tableau.
- Penser aux cas vides (`[]` et `""`).
