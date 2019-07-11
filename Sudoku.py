from array import *
from copy import copy, deepcopy
LIST = [1,2,3,4,5,6,7,8,9]
BOX_SIZE = 3
NOTDOABLE = -1
results = []



def check_row (possible_list, row, col, sudoku):
    """
    Inputs:
        possible_list - the list of all the possible
        this element can have
        row - the row index of the element
        col - the col index of the element
        sudoku - the sudoku we want to solve
    Output:
        returns a list containing all the possible number
        that this position can have given the current condition
        of the row
    """
    remove_list = []
    for i in range(0,len(sudoku)):
        for k in range(0,len(possible_list)):
            if (sudoku[row][i] == possible_list[k]):
                remove_list.append(possible_list[k])
    for i in range(0,len(remove_list)):
        possible_list.remove(remove_list[i])
    return possible_list

def check_col (possible_list, row, col, sudoku):
    """
    Inputs:
        possible_list - the list of all the possible
        this element can have
        row - the row index of the element
        col - the col index of the element
        sudoku - the sudoku we want to solve
    Output:
        returns a list containing all the possible number
        that this position can have given the current condition
        of the row
    """
    remove_list = []
    for i in range(0,len(sudoku[0])):
        for k in range(0,len(possible_list)):
            if (sudoku[i][col] == possible_list[k]):
                    remove_list.append(possible_list[k])
    for i in range(0,len(remove_list)):
        possible_list.remove(remove_list[i])
    return possible_list

def check_block(possible_list, row, col, sudoku):
    """
    Inputs:
        possible_list - the list of all the possible
        this element can have
        row - the row index of the element
        col - the col index of the element
        sudoku - the sudoku we want to solve
    Output:
        returns a list containing all the possible number
        that this position can have given the current condition
        of the row
    """
    remove_list = []
    boxRow = int(row / 3) * 3
    boxCol = int(col / 3) * 3
    boxRowEnd = boxRow + BOX_SIZE
    boxColEnd = boxCol + BOX_SIZE

    for i in range(boxRow, boxRowEnd):
        for j in range(boxCol, boxColEnd):
            for k in range(0, len(possible_list)):
                if(sudoku[i][j] == possible_list[k]):
                    remove_list.append(possible_list[k])
    for i in range(0,len(remove_list)):
        possible_list.remove(remove_list[i])
    return possible_list

def check_num(sudoku):
    """
    Inputs:
        sudoku - the sudoku needs to be resolved, the unfilled places are all
        represented by 0
    Output:
        returns the sudoku with all the entries that need to be filled Output
        with a list of possible number
        if it is not doable return -1
    """
    sudoku_copy = sudoku.copy()
    for i in range(0, len(sudoku)):
        for j in range(0, len(sudoku[0])):
            if (sudoku[i][j] == 0 or type(sudoku[i][j]) == list):
                possible_list = LIST.copy()
                possible_list = check_row(possible_list, i, j, sudoku_copy)
                possible_list = check_col(possible_list, i, j, sudoku_copy)
                possible_list = check_block(possible_list, i, j, sudoku_copy)
                if (len(possible_list) == 0):
                    return NOTDOABLE
                sudoku_copy[i][j] = possible_list
    return sudoku_copy

def check_filled(sudoku):
    for item in sudoku():
        if (type(item) == list):
            return False
    return True

def fill_in(sudoku):
    """
    Inputs:
        sudoku - the sudoku that all the unfilled places are substituted by the
        possible_list
    Outputs:
        the sudoku or a list of sudoku that is filled
    """

    sudoku_with_possible_list = check_num(sudoku)

    # This supposed to be a recursive function

    length_list = []
    index_list = []

    # Find all the length of the possible_lists in each place of the Sudoku,
    # put them all in a list

    if (sudoku_with_possible_list == NOTDOABLE):
        return NOTDOABLE

    for i in range(0, len(sudoku_with_possible_list)):
        for j in range(0, len(sudoku_with_possible_list[0])):
            if (type(sudoku_with_possible_list[i][j]) == list):
                length_list.append(len(sudoku_with_possible_list[i][j]))
                index_list.append((i,j))

    # The base case of it which everything has been filled in
    if (len(index_list) == 0):
        results.append(sudoku_with_possible_list)
        return sudoku_with_possible_list

    else:
        result_list = []
        min_length = 0
        min_length = min(length_list)
        min_index = length_list.index(min_length)
        # Fill in a num for the possible_list that has min_length
        for i in range(0, min_length):
            row = index_list[min_index][0]
            col = index_list[min_index][1]
            sudoku_copy = deepcopy(sudoku_with_possible_list)
            sudoku_copy[row][col] = sudoku_with_possible_list[row][col][i]
            sudoku_copy = fill_in(sudoku_copy)
        return sudoku_copy
