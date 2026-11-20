# py_graph_cycle_detector : méthode

## Le problème
Dire si un **graphe orienté** (donné en liste d'adjacence) contient un **cycle**.

```python
{0: [1], 1: [2], 2: [0]}   # 0 → 1 → 2 → 0  : cycle  → True
{0: [1], 1: [2], 2: []}    # pas de cycle            → False
{0: [0]}                   # boucle sur soi-même     → True
{}                         # graphe vide             → False
```

## L'idée à retenir : DFS avec 3 états
> On explore en profondeur. Si, en suivant un chemin, on retombe sur un nœud **encore en cours d'exploration**, on a bouclé : cycle.

Chaque nœud est dans un de 3 états (comme les couleurs d'un feu) :

| état | signification | variable |
|---|---|---|
| jamais vu | pas encore visité | (dans aucun set) |
| **en cours** | sur le chemin actuel | `en_cours` |
| **terminé** | exploré entièrement, aucun cycle trouvé par lui | `termine` |

Règle d'or :
- on rencontre un nœud **en cours** → **cycle** (`True`)
- on rencontre un nœud **terminé** → rien à faire, on sait déjà qu'il est sûr (`False`)

## Pourquoi 2 sets et pas un seul `visited` ?
Avec un seul `visited`, le graphe `0→1, 0→2, 1→3, 2→3` (en losange) donnerait un faux cycle : on arrive sur 3 deux fois, mais **ce n'est pas un cycle**, car 3 est déjà **terminé** et ne revient pas vers nous. Il faut donc distinguer "sur le chemin actuel" de "déjà fini".

## Le code expliqué ligne par ligne

```python
en_cours = set()
termine = set()
```
Les deux ensembles d'états.

```python
def dfs(noeud):
    if noeud in en_cours:
        return True
    if noeud in termine:
        return False
```
Cas d'arrêt. Retomber sur un nœud du chemin actuel = cycle. Retomber sur un nœud fini = inutile de re-explorer.

```python
    en_cours.add(noeud)
    for voisin in graph.get(noeud, []):
        if dfs(voisin):
            return True
```
On entre dans le nœud (on l'ajoute au chemin) et on explore chaque voisin. `graph.get(noeud, [])` évite une erreur si un voisin n'est pas une clé du dictionnaire. Si un voisin trouve un cycle, on remonte `True` immédiatement.

```python
    en_cours.remove(noeud)
    termine.add(noeud)
    return False
```
Tous les voisins sont OK : on **quitte** le chemin (retrait de `en_cours`) et on marque le nœud terminé. C'est le fameux "backtracking".

```python
for noeud in graph:
    if dfs(noeud):
        return True
return False
```
Le graphe peut être non connexe : on lance un DFS depuis **chaque** nœud. Graphe vide → la boucle ne tourne pas → `False`.

## Les cas particuliers de l'énoncé
- **Self-loop** `{0: [0]}` : on entre dans 0 (`en_cours`), le voisin est 0, déjà `en_cours` → `True`. Aucun code spécial nécessaire.
- **Graphe vide** `{}` : `False` naturellement.
- **Nœuds sans arêtes** `{0: [], 1: []}` : `False`.

## Exemple pas à pas : `{0:[1], 1:[2], 2:[0]}`
`dfs(0)` → en_cours={0} → `dfs(1)` → en_cours={0,1} → `dfs(2)` → en_cours={0,1,2} → voisin 0 est dans `en_cours` → **True**.

## Complexité
- Temps O(V + E), mémoire O(V) (pile de récursion incluse).

## Pièges
- Utiliser un seul `visited` (faux positifs sur les losanges).
- Oublier de **retirer** le nœud de `en_cours` après son exploration.
- Oublier de lancer le DFS depuis tous les nœuds.
