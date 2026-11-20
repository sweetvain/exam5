# 127. Word Ladder : méthode

## Le problème
On part de `beginWord`, on veut arriver à `endWord`. À chaque étape on change **une seule lettre**, et le nouveau mot doit être dans `wordList`.
On renvoie le **nombre de mots** de la plus courte chaîne (0 si impossible).

Exemple : `hit → hot → dot → dog → cog` = **5** mots.

## L'idée à retenir : BFS (parcours en largeur)
> "Plus court chemin" + "chaque étape coûte 1" = **BFS** avec une **file**.

Imagine que chaque mot est une ville, et que deux mots sont reliés s'ils diffèrent d'une lettre. On cherche le chemin le plus court : on explore **tous les voisins à distance 1**, puis **tous ceux à distance 2**, etc. Le premier moment où on tombe sur `endWord`, c'est forcément le plus court chemin.

## Les 5 réflexes (à refaire de tête)
1. `mots = set(wordList)` : un set permet de tester `in` en O(1).
2. Si `endWord` n'est pas dans `mots` → `return 0`.
3. `file = deque([(beginWord, 1)])` : on stocke le mot **et** la longueur du chemin.
4. Boucle : on sort un mot, si c'est `endWord` → on renvoie sa longueur.
5. Sinon on génère tous les voisins (chaque position × 26 lettres), et si le voisin est dans `mots`, on le **retire** (= "visité") et on l'ajoute à la file avec `longueur + 1`.

## Le code expliqué ligne par ligne

```python
mots = set(wordList)
```
Transforme la liste en set pour des recherches rapides.

```python
if endWord not in mots:
    return 0
```
Si le mot final n'existe pas dans la liste, aucune chaîne n'est possible.

```python
file = deque([(beginWord, 1)])
mots.discard(beginWord)
```
`deque` = file efficace (`popleft` en O(1)). On démarre à longueur 1 (le mot de départ compte). `discard` ne plante pas si `beginWord` n'est pas dans le set.

```python
while file:
    mot, longueur = file.popleft()
    if mot == endWord:
        return longueur
```
On prend le plus ancien mot de la file (FIFO = largeur). Si c'est la cible : fini, c'est le chemin le plus court.

```python
for i in range(len(mot)):
    for lettre in "abcdefghijklmnopqrstuvwxyz":
        nouveau = mot[:i] + lettre + mot[i + 1:]
```
On remplace la lettre à la position `i` par chaque lettre de l'alphabet. `mot[:i]` = avant, `mot[i+1:]` = après. Exemple : `hit`, i=1, lettre `o` → `h` + `o` + `t` = `hot`.

```python
        if nouveau in mots:
            mots.remove(nouveau)
            file.append((nouveau, longueur + 1))
```
Si le mot existe : on le retire du set (pour ne **jamais** le revisiter, ce qui évite les boucles infinies) et on l'ajoute à la file avec un pas de plus.

```python
return 0
```
La file est vide et on n'a jamais trouvé `endWord` → impossible.

## Pourquoi retirer du set et non garder un `visited` ?
C'est la même chose, mais plus court : le set `mots` joue à la fois le rôle de dictionnaire et de "pas encore visité".

## Complexité
- Temps : O(N × L × 26) avec N = nb de mots, L = longueur d'un mot.
- Mémoire : O(N).

## Pièges
- Oublier de renvoyer **0** si `endWord` est absent.
- Compter les **mots** et non les **transformations** : on démarre à `1`.
- Oublier de marquer les mots comme visités → boucle infinie.
