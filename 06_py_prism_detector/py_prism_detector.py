DIRECTIONS = [
    ("H", 0, 1),
    ("H-", 0, -1),
    ("V", 1, 0),
    ("V-", -1, 0),
    ("D1", 1, 1),
    ("D1-", -1, -1),
    ("D2", 1, -1),
    ("D2-", -1, 1),
]


def prism_detector(grid: list[str], pattern: str) -> list[tuple[int, int, str]]:
    if not grid or not pattern:
        return []

    resultat = []
    utilisees = set()

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            for code, dr, dc in DIRECTIONS:
                cases = []
                for k in range(len(pattern)):
                    rr = r + dr * k
                    cc = c + dc * k
                    if not (0 <= rr < len(grid) and 0 <= cc < len(grid[rr])):
                        break
                    if grid[rr][cc] != pattern[k]:
                        break
                    cases.append((rr, cc))

                if len(cases) == len(pattern) and not utilisees & set(cases):
                    resultat.append((r, c, code))
                    utilisees.update(cases)

    return resultat


if __name__ == "__main__":
    assert prism_detector(["ABC", "DEF", "GHI"], "ADG") == [(0, 0, "V")]
    assert prism_detector(["HELLO", "WORLD"], "LL") == [(0, 2, "H")]
    assert prism_detector(["XYZ", "ABC", "DEF"], "XBF") == [(0, 0, "D1")]
    assert prism_detector([], "ABC") == []
    assert prism_detector(["ABC"], "") == []
    assert prism_detector(["ABC", "DEF", "GHI"], "GDA") == [(2, 0, "V-")]
    assert prism_detector(["ABC", "DEF", "GHI"], "CEG") == [(0, 2, "D2")]
    assert prism_detector(["ABC", "DEF", "GHI"], "ZZ") == []
    print("py_prism_detector : OK")
