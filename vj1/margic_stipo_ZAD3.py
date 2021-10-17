# created by stipo
# 13.10.21

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(4))