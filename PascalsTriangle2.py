from typing import List
import unittest

class Solution:        
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        lst = [1]
        res = 1
        for i in range(1, rowIndex):
            res *= (rowIndex - i)
            res //= i
            lst.append(res)
        return lst 
             
        
class TestSolution(unittest.TestCase):
    def test_generate(self):
        solution = Solution()
        numRows = 3
        output_list = solution.getRow(numRows)
        print(output_list)
        
if __name__ == "__main__":
    unittest.main()