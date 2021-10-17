# created by stipo
# 13.10.21

def backward(steps, digit):
    for i in range(steps - 2):
        digit -= 1
        if digit > 9:
            print(digit % 10)
        else:
            print(digit, end=' ')


def make_triangle(user_input):
    counter = 1
    temp = 0
    steps = 0

    for row in range(1, user_input + 1):
        digit = row
        for column in range(counter):
            while digit <= counter:
                if digit > 9:
                    print(digit % 10, end=' ')
                else:
                    print(digit, end=' ')
                digit += 1

            if counter == column + 1 and column + 1 > 1:
                steps += 1
                temp += 1

                if column > 9:
                    print(column % 10, end=' ')
                else:
                    print(column, end=' ')

                if steps + temp != column:
                    if column - temp > 9:
                        print((column-temp) % 10, end=' ')
                    else:
                        print(column - temp, end=' ')
                    if steps > 2:
                        backward(steps, column - temp)
                    temp += 1
        print("\n")
        counter += 2


n = int(input("Enter n: "))

make_triangle(n)