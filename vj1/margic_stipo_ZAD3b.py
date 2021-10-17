# created by stipo
# 13.10.21
import margic_stipo_ZAD3


def get_n_prime(n):
    counter = 0

    for i in range(3, 999999):
        if margic_stipo_ZAD3.is_prime(i):
            counter += 1
            print(i)
            if counter == n:
                return i


