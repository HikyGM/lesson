number_of_cells = int(input())
letter = ' ABCDEFGHI'
for i in range(number_of_cells, 0, -1):
    for j in range(1, number_of_cells + 1):
        print(letter[j] + str(i), end=' ')
    print('\n')
