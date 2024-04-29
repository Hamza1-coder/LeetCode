import unittest

class Solution:
    
    """
        #   More easy and readable solution
    """
    # def maxDepth(self, s: str) -> int:
    #     counter, max_counter = 0, 0
    #     for c in s:
    #         if c == "(":
    #             counter += 1
    #             max_counter = max(max_counter, counter)
    #         elif c == ")":
    #             counter -= 1
    #     return max_counter
    
    """
        #   Short-cut way: play with binary:
        True - False = 1
        True - True = 0
        False - True = -1
        False - False = 0
    """
    def maxDepth(self, s: str) -> int:
        counter , max_counter = 0, 0
        for c in s:
            counter += (c=="(") - (c==")")
            max_counter = max(counter, max_counter)
        return max_counter
    
class TestSolution(unittest.TestCase):
    def test_maxDepth(self):
        solution = Solution()
        # test case 1
        s1 = "(1+(2*3)+((8)/4))+1"
        output1 = solution.maxDepth(s1)
        self.assertEqual(output1, 3)
        
        # test case 2
        s2 = "(1)+((2))+(((3)))"
        output2 = solution.maxDepth(s2)
        self.assertEqual(output2, 3)
        
if __name__ == "__main__":
    unittest.main()