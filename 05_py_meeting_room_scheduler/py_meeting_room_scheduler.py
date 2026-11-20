def meeting_room_scheduler(meetings: list[list[int]]) -> dict[str, any]:
    salles = []

    for reunion in sorted(meetings):
        debut = reunion[0]

        for salle in salles:
            if salle[-1][1] <= debut:
                salle.append(reunion)
                break
        else:
            salles.append([reunion])

    return {
        "rooms_needed": len(salles),
        "room_assignments": {i: salle for i, salle in enumerate(salles)},
    }


if __name__ == "__main__":
    assert meeting_room_scheduler([[0, 30], [5, 10], [15, 20]]) == {
        "rooms_needed": 2,
        "room_assignments": {0: [[0, 30]], 1: [[5, 10], [15, 20]]},
    }
    assert meeting_room_scheduler([[9, 10], [9, 12], [11, 13]]) == {
        "rooms_needed": 2,
        "room_assignments": {0: [[9, 10], [11, 13]], 1: [[9, 12]]},
    }
    assert meeting_room_scheduler([[1, 5], [8, 9], [8, 9]]) == {
        "rooms_needed": 2,
        "room_assignments": {0: [[1, 5], [8, 9]], 1: [[8, 9]]},
    }
    assert meeting_room_scheduler([]) == {"rooms_needed": 0, "room_assignments": {}}
    assert meeting_room_scheduler([[1, 2], [3, 4], [5, 6]]) == {
        "rooms_needed": 1,
        "room_assignments": {0: [[1, 2], [3, 4], [5, 6]]},
    }
    print("py_meeting_room_scheduler : OK")
