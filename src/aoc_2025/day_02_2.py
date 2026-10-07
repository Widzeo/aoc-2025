def day_02(filepath: str) -> int:
    sum = 0
    
    with open(filepath) as f:
        values = f.readline().split(',')
        
    for value in values:
        index = value.find('-')
        for i in range(int(value[:index]), int(value[index + 1:]) + 1):
            id = str(i)
            length = len(id)

            '''
            Try for every size of part:
                for 123123 -> start with size of 1, compare 1 and 2, false,
                            then size of 2, compare 12 and 31, false,
                            finally size of 3, compare 123 and 123, true
            '''
            b = False
            j = 1
            while not b and j <= (length // 2):
                if length % j == 0:
                    b = True
                    for k in range(length // j - 1):
                        if(id[k*j:(k+1)*j] != id[(k+1)*j:(k+2)*j]):
                            b = False
                            break

                j += 1   

            if b:
                sum += i

    return sum

if __name__ == "__main__":
    print(day_02("inputs/input_02.txt"))