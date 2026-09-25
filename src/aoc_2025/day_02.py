def day_02(filepath: str) -> int:
    count = 0
    
    with open(filepath, 'r') as f:
        values = f.readline().split(',')
        
    for value in values:
        index = value.find('-')
        for i in range(int(value[:index]), int(value[index + 1:])):
            id = str(i)
            middle = len(id) // 2
            if(id[:middle] == id[middle:]):
                count += i

    return count

if __name__ == "__main__":
    print(day_02("inputs/input_02.txt"))