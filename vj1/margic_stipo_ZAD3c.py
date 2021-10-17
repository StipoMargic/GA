# created by stipo
# 13.10.21
import margic_stipo_ZAD3


def adjacent_prime_numbers(number):
    list_prime_numbers = []

    for i in range(2, number):
        if margic_stipo_ZAD3.is_prime(i):
            for j in range(i, number):
                if margic_stipo_ZAD3.is_prime(j):
                    if (j - i) == 2:
                        list_prime_numbers.append((i, j))
    return list_prime_numbers
