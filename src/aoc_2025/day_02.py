def day_02(filepath: str) -> int:
    sum = 0
    
    with open(filepath, 'r') as f:
        values = f.readline().split(',')
        
    for value in values:
        index = value.find('-')
        for i in range(int(value[:index]), int(value[index + 1:]) + 1):
            id = str(i)
            middle = len(id) // 2
            if(id[:middle] == id[middle:]):
                sum += i

    return sum

if __name__ == "__main__":
    print(day_02("inputs/input_02.txt"))