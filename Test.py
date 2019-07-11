import Sudoku as S

INSTRUCTION = 'Enter A list of the value in a Sudoku for one row, and press enter for the next row, use 0 to mark as those empty spaces, and use \',\' to seperate each column in this row.'

sudoku = []
print(INSTRUCTION)

for i in range(0,9):
    sudoku_int_row = []
    sudoku_row = input()
    row = sudoku_row.split(',')
    if(len(row) != 9):
        print('Wrong input for this row')
        exit()
    else:

        for num in row:
            if (int(num) > 9 or int(num) < 0):
                print('Error Number in a Sudoku')
                exit()
            else:
                sudoku_int_row.append(int(num))
        sudoku.append(sudoku_int_row)




for i in range (0,9):
    print(sudoku[i])


print()

soduku_tryFill = S.fill_in(sudoku)

for i in range(0, len(soduku_tryFill)):
    print(soduku_tryFill[i])
