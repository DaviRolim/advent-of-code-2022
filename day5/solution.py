all_crates = [
    list('LNWTD'),
    list('CPH'),
    list('WPHNDGMJ'),
    list('CWSNTQL'),
    list('PHCN'),
    list('THNDMWQB'),
    list('MBRJGSL'),
    list('ZNWGVBRT'),
    list('WGDNPL')
]


def get_move_information_from_row(row):
    # Example row move 3 from 5 to 2
    row_items = row.split(' ')
    quantity = int(row_items[1])
    _from = int(row_items[3])
    to = int(row_items[5])
    return quantity, _from - 1, to - 1


def execute_move(quantity, from_, to):
    # Move crates from one crate to another
    # Solution 1
    # for _ in range(quantity):
    #     crate = all_crates[from_].pop()
    #     all_crates[to].append(crate)
    # End solution 1
    # Solution 2
    # Move crates from one crate to another maintaining order
    all_crates[to] = all_crates[to] + all_crates[from_][-quantity:]
    # Remove crates from the original crate
    all_crates[from_] = all_crates[from_][:-quantity]
    # End Solution 2


with open('input.txt') as f:
    for row in f.readlines():
        row = row.strip()
        moves = get_move_information_from_row(row)
        execute_move(*moves)

last_crates = [crate.pop() for crate in all_crates]
print(''.join(last_crates))
