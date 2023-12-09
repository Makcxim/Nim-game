
def last_not_pressed_btn(dct: dict, heaps_count: int):
    answer = {i: 0 for i in range(1, heaps_count + 1)}
    for key, value in dct.items():
        if value == 0:
            answer[int(key[0])] += 1
    return answer


def get_position_parity(b: list):
    max_value = len(str(max([int(i) for i in b])))
    c = {i: 0 for i in range(1, max_value + 1)}
    for i in b:
        for j in range(1, len(i) + 1):
            if i[-j] == "1":
                c[j] += 1

    flag = 0
    for i in c.values():
        if i % 2 == 1:
            flag = 1
            break

    return bool(flag)
    # True - current position - odd - нечетная
    # False - current position - even - четная


def find_best_step(dct: dict, heaps_count: int):
    a = last_not_pressed_btn(dct, heaps_count)
    main_b = [bin(i)[2:] for i in a.values()]
    heaps_sum = sum([value for value in a.values()])

    # if current position - odd:
    # search max even position to make game harder
    # if current position - even:
    # search min odd position to win

    odd_positions = []
    even_positions = []

    for key, i in a.items():
        for j in range(1, i + 1):
            changed_position = a.copy()
            changed_position[key] -= j
            b = [bin(i)[2:] for i in changed_position.values()]
            changes = (key, j)

            if get_position_parity(b):
                odd_positions.append([changed_position, changes, heaps_sum - j])
            else:
                even_positions.append([changed_position, changes, heaps_sum - j])

    odd_positions.sort(key=lambda x: x[2], reverse=True)
    even_positions.sort(key=lambda x: x[2])

    if get_position_parity(main_b):
        new_btn_pos = {key: (1 if not even_positions[0][0][int(key[0])] >= int(key[1]) else 0) for key in dct}
        return new_btn_pos
    else:
        new_btn_pos = {key: (1 if not odd_positions[0][0][int(key[0])] >= int(key[1]) else 0) for key in dct}
        return new_btn_pos
