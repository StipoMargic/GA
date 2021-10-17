# created by stipo
# 13.10.21

def is_pitagora(a, b, c):
    if c * c == a * a + b * b:
        return True
    return False


while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    if a > 0 and b > 0 and c > 0:
        if is_pitagora(a, b, c):
            print("It is pitagora")
        else:
            print("It is not pitagora")
    else:
        break
