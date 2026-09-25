from operator import add, sub

OPERATIONS = {'L': sub, 'R': add}

def day_01(filepath: str) -> int:
    count = 0
    current = 50

    with open(filepath, 'r') as file:
        lines = file.readlines()

    for line in lines:
        operation = line[0]
        value = int(line[1:])
        current = OPERATIONS[operation](current, value)

        while current > 99:
            current -= 100
        while current < 0:
            current += 100

        if current == 0:
            count += 1

    return count

print(day_01("inputs/input_01.txt"))