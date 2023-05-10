def colorFill1D(lst, x, old_color, new_color):
    '''
    This function does fill an area with another color in a 1D list
    Args:
        lst: list of int on which we work
        x: possition of the current item of interest
        old_color: color we want to change
        new_color: color by which we would like to replace the old_color
        Note 1: This function does not return anything since we modify the list
        Note 2: "return" can be used alone!! Even if you return nothing 
        It is an important note to let you know how to exit the recursion for base cases!!
    '''
    ...

def colorFill2D(matrix, x, y, old_color, new_color):
    '''
    This function does fill an area with another color in a 2D matrix
    Args:
        matrix: matrix of int on which we work
        x: vertical possition of the current item of interest
        y: horizontal possition of the current item of interest
        old_color: color we want to change
        new_color: color by which we would like to replace the old_color
    '''
    ...

def printMatrix(matrix):
    '''
    Just a tiny function to print a matrix
    Args:
        matrix: matrix to print
    '''
    for row in matrix:
        print(row)

def main():

    #########################
    # TASK 1: fill area in 1D
    #########################

    lst = [0,0,0,0,1,1,1,1,2,2,2,2]
    pixel_coord = 5
    old_color = lst[pixel_coord] 
    new_color = 25
    colorFill1D(lst, pixel_coord, old_color, new_color)
    print(lst)

    #########################
    # TASK 2: fill area in 2D
    #########################

    matrix =[[0, 0, 0, 0, 0, 0, 0, 3, 3, 3],
             [3, 3, 3, 0, 0, 0, 0, 0, 0, 1],
             [3, 3, 3, 0, 0, 0, 1, 1, 1, 1],
             [3, 3, 3, 3, 3, 0, 1, 1, 1, 1],
             [4, 4, 3, 0, 0, 0, 0, 1, 1, 1],
             [4, 4, 3, 2, 2, 0, 0, 0, 0, 1],
             [0, 0, 2, 2, 2, 2, 0, 0, 0, 0],
             [0, 0, 0, 2, 2, 4, 0, 5, 5, 5],
             [1, 1, 0, 0, 0, 4, 0, 5, 5, 5],
             [1, 0, 0, 0, 4, 4, 4, 4, 4, 0]]

    x = 2
    y = 4
    old_color = matrix[y][x] # coordinates in this order --> y, x
    new_color = 8
    colorFill2D(matrix, x, y, old_color, new_color)
    printMatrix(matrix)

main()

