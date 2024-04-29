from typing import List
import unittest

class Solution:
    def dfs(self, r, c, word, wordIndex, board):
        # base case
        if wordIndex == len(word):
            return True
        # check out of bound
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return False
        # Invalid case
        if board[r][c] != word[wordIndex] or board[r][c] == "v":
            return False
        # mark as visited
        ch = board[r][c]
        board[r][c] = "v"
        # dfs calls
        if ( 
            self.dfs(r-1, c, word, wordIndex+1, board) #left
            or 
            self.dfs(r, c+1, word, wordIndex+1, board) # down
            or 
            self.dfs(r+1, c, word, wordIndex+1, board) # right
            or
            self.dfs(r, c-1, word, wordIndex+1, board) # up
            ):
            return True
        # backtracking
        board[r][c] = ch
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    found = self.dfs(r, c, word, 0, board)
                    if found:
                        return True
        return False
    

class TestSolution(unittest.TestCase):
    def test_exist(self):
        solution = Solution()
        # test case 1
        board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word1 = "ABCCED"
        output1 = solution.exist(board1, word1)
        self.assertEqual(output1, True)
        # test case 2
        board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word2 = "SEE"
        output2 = solution.exist(board2, word2)
        self.assertEqual(output2, True)
        # test case 3
        board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word3 = "ABCB"
        output3 = solution.exist(board3, word3)
        self.assertEqual(output3, False)

if __name__ == "__main__":
    unittest.main()