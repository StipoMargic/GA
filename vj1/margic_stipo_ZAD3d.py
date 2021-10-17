# created by stipo
# 13.10.21
import margic_stipo_ZAD3


def goldbach(number):
    for i in range(1, number):
        j = number - i
        if margic_stipo_ZAD3.is_prime(i) and margic_stipo_ZAD3.is_prime(j):
            print(f"{i} + {j} = {number}")