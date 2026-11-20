# 443. String Compression : méthode

## Le problème
On reçoit une liste de caractères `chars`. On la compresse **sur place** : chaque groupe de lettres identiques consécutives devient `lettre + nombre` (le nombre seulement s'il est > 1). On renvoie la **nouvelle longueur**.

```
["a","a","b","b","c","c","c"]  →  ["a","2","b","2","c","3"]   (retourne 6)
```
Si le nombre est ≥ 10, il est écrit chiffre par chiffre : 12 → `"1","2"`.

## L'idée à retenir : 2 pointeurs (lecture / écriture)
> Un pointeur **lecture** qui avance pour compter, un pointeur **écriture** qui réécrit le résultat au début de la même liste.

Comme `ecriture` ne dépasse jamais `lecture`, on n'écrase jamais ce qu'on n'a pas encore lu.

## Les 4 étapes pour chaque groupe
1. Retenir la lettre et le point de départ du groupe.
2. Avancer `lecture` tant que c'est la même lettre.
3. `compte = lecture - debut`.
4. Écrire la lettre ; si `compte > 1`, écrire chaque chiffre de `str(compte)`.

## Le code expliqué ligne par ligne

```python
ecriture = 0
lecture = 0
```
Les deux pointeurs partent du début.

```python
while lecture < len(chars):
    lettre = chars[lecture]
    debut = lecture
```
Tant qu'il reste des caractères à lire. On note la lettre du groupe et où il commence.

```python
    while lecture < len(chars) and chars[lecture] == lettre:
        lecture += 1
    compte = lecture - debut
```
On avance jusqu'à la fin du groupe. Après la boucle, `lecture` pointe sur la **première lettre différente** (ou la fin). La taille du groupe est donc `lecture - debut`. L'ordre des conditions (`lecture < len` d'abord) évite une erreur d'index.

```python
    chars[ecriture] = lettre
    ecriture += 1
```
On écrit la lettre (toujours).

```python
    if compte > 1:
        for chiffre in str(compte):
            chars[ecriture] = chiffre
            ecriture += 1
```
Si le groupe fait plus d'une lettre, on écrit son nombre. `str(12)` = `"12"` → on parcourt `"1"` puis `"2"`, ce qui gère les nombres à plusieurs chiffres.

```python
return ecriture
```
`ecriture` = nombre de cases écrites = nouvelle longueur.

## Exemple pas à pas : `a a b b b`
| étape | lecture | lettre | compte | écrit | chars |
|---|---|---|---|---|---|
| groupe 1 | 0→2 | a | 2 | `a`,`2` | `a 2 b b b` |
| groupe 2 | 2→5 | b | 3 | `b`,`3` | `a 2 b 3 b` |
Retour : 4.

## Complexité
- Temps O(n), mémoire O(1) (on modifie la liste sur place).

## Pièges
- Ne pas écrire `1` quand le groupe n'a qu'une lettre.
- Écrire `"12"` en un seul élément : il faut **un chiffre par case**.
- Oublier de renvoyer `ecriture` (et pas `len(chars)`).
