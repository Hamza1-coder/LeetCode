from typing import List
import unittest
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)
        taken = 0
        i = 0
        z = 0
        while k > 0:
            if i != 0: happiness[i] = happiness[i] - i
            if happiness[i] > 0:
                taken += happiness[i]
                i+=1
            k-=1

        return taken
    
class TestSolution(unittest.TestCase):
    def test_maximumHappinessSum(self):
        solution = Solution()
        # testcase 1
        happiness, k = [1,2,3], 2
        output = solution.maximumHappinessSum(happiness, k)
        self.assertEqual(output, 4)
        
        # testcase 2
        happiness, k = [2,3,4,5], 1
        output = solution.maximumHappinessSum(happiness, k)
        self.assertEqual(output, 5)
        
        #testcase 3
        happiness, k = [1,1,1,1], 2
        output = solution.maximumHappinessSum(happiness, k)
        self.assertEqual(output, 1)
        
if __name__ == "__main__":
    unittest.main()