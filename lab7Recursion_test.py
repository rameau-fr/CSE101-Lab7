import csv
import unittest
from Lab7Recursion import *

class Testing(unittest.TestCase):
    def test_colorFill1D1(self):
        # Test 1: middle of the list
        lst = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        x = 4
        old_color = lst[x] 
        new_color = 10
        colorFill1D(lst, x, old_color, new_color)
        lst_res = [1, 1, 1, 10, 10, 10, 3, 3, 3, 4, 4, 4]
        self.assertListEqual(lst_res, lst)

    def test_colorFill1D2(self):
        # Test 2: end of the list
        lst = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        x = 10
        old_color = lst[x] 
        new_color = 10
        colorFill1D(lst, x, old_color, new_color)
        lst_res = [1, 1, 1, 2, 2, 2, 3, 3, 3, 10, 10, 10]
        self.assertListEqual(lst_res, lst)

    def test_colorFill1D3(self):
        # Test 3: single element beginning of list
        lst = [5, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        x = 0
        old_color = lst[x] 
        new_color = 10
        colorFill1D(lst, x, old_color, new_color)
        lst_res = [10, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        self.assertListEqual(lst_res, lst)
    
    def test_colorFill2D1(self):
        # Test 1: middle of the matrix
        matrix =[[0, 0, 5, 0, 2],
                 [3, 3, 1, 0, 2],
                 [3, 3, 1, 1, 2],
                 [3, 3, 1, 3, 2],
                 [4, 4, 3, 0, 2]]
        x = 2
        y = 2
        old_color = matrix[y][x]
        new_color = 8
        matrix_res =[[0, 0, 5, 0, 2],
                     [3, 3, 8, 0, 2],
                     [3, 3, 8, 8, 2],
                     [3, 3, 8, 3, 2],
                     [4, 4, 3, 0, 2]]
        colorFill2D(matrix, x, y, old_color, new_color)
        self.assertListEqual(matrix_res, matrix)

    def test_colorFill2D2(self):
        # Test 2: side of the matrix
        matrix =[[0, 0, 5, 0, 2],
                 [3, 3, 1, 0, 2],
                 [3, 3, 1, 1, 2],
                 [3, 3, 1, 3, 2],
                 [4, 4, 3, 0, 2]]
        x = 4
        y = 3
        old_color = matrix[y][x]
        new_color = 8
        matrix_res =[[0, 0, 5, 0, 8],
                     [3, 3, 1, 0, 8],
                     [3, 3, 1, 1, 8],
                     [3, 3, 1, 3, 8],
                     [4, 4, 3, 0, 8]]
        colorFill2D(matrix, x, y, old_color, new_color)
        self.assertListEqual(matrix_res, matrix)

    def test_colorFill2D3(self):
        # Test 3: single element side of list
        matrix =[[1, 0, 5, 0, 2],
                 [3, 3, 1, 0, 2],
                 [3, 3, 1, 1, 2],
                 [3, 3, 1, 3, 2],
                 [4, 4, 3, 0, 2]]
        x = 0
        y = 0
        old_color = matrix[y][x]
        new_color = 8
        matrix_res =[[8, 0, 5, 0, 2],
                     [3, 3, 1, 0, 2],
                     [3, 3, 1, 1, 2],
                     [3, 3, 1, 3, 2],
                     [4, 4, 3, 0, 2]]
        colorFill2D(matrix, x, y, old_color, new_color)
        self.assertListEqual(matrix_res, matrix)

if __name__ == '__main__':
    unittest.main()