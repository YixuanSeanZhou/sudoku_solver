import Sudoku as S

sudoku = [[5,6,1,8,4,7,9,2,3]]

sudoku.append([3,0,9,0,0,0,6,0,0])

sudoku.append([4,2,8,9,6,3,1,7,5])

sudoku.append([0,1,0,0,8,0,0,4,0])

sudoku.append([7,9,0,6,0,2,0,1,8])

sudoku.append([0,5,0,0,3,0,0,9,0])

sudoku.append([9,3,5,4,7,8,2,6,1])

sudoku.append([1,4,6,2,9,5,8,3,7])

sudoku.append([2,8,7,3,1,6,0,5,9])

sudoku = [[5,3,0,0,7,0,0,0,0]]

sudoku.append([6,0,0,1,9,5,0,0,0])
sudoku.append([0,9,8,0,0,0,0,6,7])
sudoku.append([8,0,0,0,6,0,0,0,3])
sudoku.append([4,0,0,8,0,3,0,0,1])
sudoku.append([7,0,0,0,2,0,0,0,6])
sudoku.append([0,6,0,0,0,0,2,8,4])
sudoku.append([0,0,0,4,1,9,0,0,5])
sudoku.append([0,0,0,0,8,0,0,7,9])

for i in range (0,9):
    print(sudoku[i])


print()

# sudoku_1 = S.check_num(sudoku)
# for i in range (0,9):
#     print(sudoku_1[i])
# print()
#

soduku_tryFill = S.fill_in(sudoku)

for i in range(0, len(soduku_tryFill)):
    print(soduku_tryFill[i])




# print(soduku_tryFill)
# #print(sudoku[1][1])


#
# def test_r(x):
#     n = x
#     print(n)
#     if x == 0 :
#         return x
#     else :
#         print(x)
#         a = test_r(x-1) + 1
#         print(x)
#         return a
#
# test_r(2)
