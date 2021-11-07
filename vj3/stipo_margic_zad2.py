def check(line):
    line[5] = line[5].replace("\n", "")
    if line[2].isnumeric() and int(line[2]) > 50:
        score = calculate_score(line)
        line.append(str(score) + "\n")
        return line
    else:
        line.append("NOPP\n")
        return line


def calculate_score(line):
    ex = line[2]
    k1 = line[3]
    k2 = line[4]
    i = line[5].replace("\n", "")

    if k1.isnumeric() and int(k1) >= 40 and k2.isnumeric() and int(k2) >= 40:
        return 0.2 * float(ex) + 0.4 * float(k1) + 0.4 * float(k2)
    elif i.isnumeric() and int(i) >= 40:
        return 0.2 * float(ex) + 0.8 * float(i)
    else:
        return "NOPP\n"


def write_to_file(scoreboard):
    string_from_arr = ", ".join(scoreboard)

    file = open("new_file.csv", "a")
    file.write(string_from_arr)
    file.close()


def read_file(filename="evidencija.csv"):
    with open("evidencija.csv") as file:
        next(file)
        for line in file:
            scoreboard = check(line.split(","))
            write_to_file(scoreboard)


read_file()
