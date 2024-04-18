from typing import List
import unittest

class Solution:              
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for jj in range(m):
                        if matrix[i][jj] !=0:
                            matrix[i][jj] = -1
                        
                    for ii in range(n):
                        if matrix[ii][j] != 0:
                            matrix[ii][j] = -1
                        
        for x in range(n):
            for y in range(m):
                if(matrix[x][y] == -1):
                    matrix[x][y] = 0
                
        return matrix;
                
    
class TestSolution(unittest.TestCase):
    def test_setZeroes(self):
        solution = Solution()
        # testcase 1
        list1 = [[1,1,1],[1,0,1],[1,1,1]]
        output_list1 = solution.setZeroes(list1)
        self.assertEqual(output_list1, [[1,0,1],[0,0,0],[1,0,1]])
        # testcase 2
        list2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        output_list2 = solution.setZeroes(list2)
        self.assertEqual(output_list2, [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
        
if __name__ == "__main__":
    unittest.main()
        