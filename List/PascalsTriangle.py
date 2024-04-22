from typing import List
import unittest


# class Solution:
#     def  nCr(self, col, row):
#         res = 1
#         for i in range(row):
#             res = res * (col - i)
#             res = res // (i + 1)
#         return res
    
#     def generate(self, numRows: int) -> List[List[int]]:
#         outer_list = []
#         for i in range(1, numRows+1):
#             nested_list = []
#             for j in range(1,i+1):
#                 nested_list.append(self.nCr(i-1, j-1))
#             outer_list.append(nested_list)
#         return outer_list


class Solution:
    def  nCr(self, row) -> List[int]:
        res = 1
        colRow = [1]
        for x in range(1, row):
            res *= (row - x)
            res //= x
            colRow.append(res)
        return colRow
    def generate(self, numRows: int) -> List[List[int]]:
        outer_list = []
        for i in range(1, numRows+1):
            outer_list.append(self.nCr(i))
        return outer_list
    
                
    
    
class TestSolution(unittest.TestCase):
    def test_generate(self):
        solution = Solution()
        numRows = 5
        output_list = solution.generate(numRows)
        print(output_list)
        
if __name__ == "__main__":
    unittest.main()