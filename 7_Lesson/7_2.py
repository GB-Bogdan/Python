def printOperationTable(operation, numRows=6, numColumns=6):
    for i in range(1, numRows + 1):
        for j in range(1, numColumns + 1):
            print(f'{operation(i, j):4}', end=' ')
        print()
printOperationTable(lambda x, y: x * y)