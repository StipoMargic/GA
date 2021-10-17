# created by stipo
# 13.10.21
import margic_stipo_ZAD3


def count_prime_between_two_decimal_numbers(num1, num2):
    counter = 0
    for i in range(int(num1), int(num2)):
        if margic_stipo_ZAD3.is_prime(i):
            counter += 1
    return counter
