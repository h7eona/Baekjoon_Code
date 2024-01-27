while True:
    try:
        ones = 1
        num = int(input())
        while True:
            if ones % num > 0:
                ones = str(ones) + '1'
                ones = int(ones)
            else:
                break
        print(len(list(str(ones))))
    except EOFError:
        break
