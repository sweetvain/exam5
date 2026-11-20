# py_meeting_room_scheduler : méthode

## Le problème
Étant donné des réunions `[début, fin[` (fin **exclue**), trouver le **nombre minimum de salles** et dire quelle réunion va dans quelle salle.

```python
[[0,30],[5,10],[15,20]]  →  2 salles
    salle 0 : [0,30]
    salle 1 : [5,10], [15,20]
```

## L'idée à retenir : glouton (greedy)
> 1. **Trier** les réunions par heure de début.
> 2. Pour chaque réunion, la mettre dans la **première salle libre**. Si aucune n'est libre, **ouvrir une nouvelle salle**.

Le nombre de salles créées = le minimum nécessaire.

## Qu'est-ce qu'une salle "libre" ?
Une salle est libre pour une réunion si sa **dernière réunion se termine avant (ou pile quand)** la nouvelle commence :

```
fin_de_la_derniere_reunion <= debut_de_la_nouvelle
```
Le `<=` (et pas `<`) vient de "la fin est **exclue**" : `[1,2]` puis `[2,3]` peuvent partager la même salle.

## Pourquoi trier ?
Parce qu'on traite les réunions dans l'ordre du temps ; ainsi, dans chaque salle, les réunions sont déjà rangées chronologiquement et il suffit de regarder la **dernière** (`salle[-1]`).

## Le code expliqué ligne par ligne

```python
salles = []
```
Liste de salles ; chaque salle est elle-même une liste de réunions.

```python
for reunion in sorted(meetings):
    debut = reunion[0]
```
`sorted` sur des listes `[début, fin]` trie d'abord par début, puis par fin. On ne modifie pas la liste d'origine.

```python
    for salle in salles:
        if salle[-1][1] <= debut:
            salle.append(reunion)
            break
```
On teste chaque salle **dans l'ordre** (donc la première libre est choisie, ce qui donne la sortie attendue de l'énoncé). `salle[-1]` = dernière réunion de la salle, `[1]` = sa fin. Si elle est finie, on y place la réunion et `break`.

```python
    else:
        salles.append([reunion])
```
Le `else` d'un `for` s'exécute **uniquement si la boucle n'a jamais fait `break`**, donc si aucune salle n'était libre : on crée une nouvelle salle contenant cette réunion.

```python
return {
    "rooms_needed": len(salles),
    "room_assignments": {i: salle for i, salle in enumerate(salles)},
}
```
Nombre de salles = `len(salles)`. Le dictionnaire associe l'identifiant (0, 1, 2…) à chaque salle grâce à `enumerate`.

## Exemple pas à pas : `[[9,10],[9,12],[11,13]]`
| réunion | salle 0 | salle 1 | décision |
|---|---|---|---|
| [9,10] | – | – | nouvelle salle 0 |
| [9,12] | fin 10 > 9 ✗ | – | nouvelle salle 1 |
| [11,13] | fin 10 ≤ 11 ✓ | | salle 0 |

Résultat : 2 salles, `0: [[9,10],[11,13]]`, `1: [[9,12]]`. ✔ identique à l'énoncé.

## Cas limites
- `[]` → boucle vide → `0` salle et `{}`.
- Réunions identiques `[8,9],[8,9]` → la 2ᵉ ne peut pas aller dans la salle de la 1ʳᵉ (fin 9 > début 8) → nouvelle salle.

## Complexité
- Tri O(n log n) + placement O(n × salles).

## Pièges
- Utiliser `<` au lieu de `<=`.
- Oublier de trier.
- Oublier que le `else` du `for` sert précisément à "aucune salle libre".
