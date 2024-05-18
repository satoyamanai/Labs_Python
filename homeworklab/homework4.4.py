def find_losing_child(n, m):
    current_cubes = m
    current_player = 1

    while True:
        cubes_to_take = 2 ** (current_player - 1)

        if cubes_to_take > 25:
            cubes_to_take = 25

        if cubes_to_take > current_cubes:
            return current_player

        current_player = (current_player % n) + 1
        current_cubes -= cubes_to_take


# example：
n = 7
m = 100
losing_child = find_losing_child(n, m)
print(losing_child,"is loser")

