def matrix(filename='matrica.txt'):
    sum_arr = []
    with open(filename) as file:
        for line in file:
            sum = 0
            for el in line.split():
                if el != " ":
                    sum += int(el)
            sum_arr.append(sum)
    return sum_arr


print(matrix())
