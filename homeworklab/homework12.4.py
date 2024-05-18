def count_routes_and_max_length(N, max_jump):
    if N <= 0:
        return 0, 0
    if N == 1:
        return 1, 1

    total_routes = 1
    max_length = N

    while max_jump > 1 and N > max_jump:
        N //= 2
        total_routes *= 2
        max_jump //= 2
        max_length += N

    return total_routes, max_length


N = 50  # example
max_jump = N // 2
routes, max_length = count_routes_and_max_length(N, max_jump)
print("Число всевозможных маршрутов мячика:", routes)
print("Максимально возможная длина лестницы N:", max_length)