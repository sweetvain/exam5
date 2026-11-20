# exam5

6 exercices d'examen en Python, chacun dans son dossier avec :
- le **code** (simple, commenté par des noms de variables clairs, avec ses tests en bas du fichier) ;
- un fichier **`METHODE.md`** qui explique la méthode et le code ligne par ligne.

| # | Exercice | Technique à retenir | Dossier |
|---|---|---|---|
| 1 | LeetCode 127 – Word Ladder | BFS (file) | `01_word_ladder` |
| 2 | LeetCode 443 – String Compression | 2 pointeurs lecture/écriture | `02_string_compression` |
| 3 | LeetCode 54 – Spiral Matrix | 4 bornes qui rétrécissent | `03_spiral_matrix` |
| 4 | py_graph_cycle_detector | DFS avec 3 états | `04_py_graph_cycle_detector` |
| 5 | py_meeting_room_scheduler | tri + glouton | `05_py_meeting_room_scheduler` |
| 6 | py_prism_detector | tableau de 8 directions | `06_py_prism_detector` |

## Lancer les tests
Chaque fichier contient des `assert` sous `if __name__ == "__main__":`

```
python 01_word_ladder/word_ladder.py
```
