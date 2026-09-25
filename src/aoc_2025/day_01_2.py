from operator import add, sub

OPERATIONS = {'L': sub, 'R': add}
STEPS = {'L': -1, 'R': 1}

def day_01(filepath: str) -> int:
    count = 0
    current = 50

    with open(filepath, 'r') as file:
        lines = file.readlines()

    for line in lines:
        operation = line[0]
        value = int(line[1:])
        step = STEPS[operation]

        for _ in range(value):
            current = (current + step) % 100
            if current == 0:
                count += 1

    return count

if __name__ == "__main__":
    print(day_01("inputs/input_01.txt"))