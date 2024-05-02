from typing import List
import unittest

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_count = 0, 0
        for i in range(len(nums)):
            if nums[i]:
                count+=1
                max_count = max(count, max_count)
            else:
                count = 0
        return max_count
    
class TestSolution(unittest.TestCase):
    def test_findMaxConsecutiveOnes(self):
        solution = Solution()
        # test case 1
        nums = [1,1,0,1,1,1]
        output = solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(output, 3)
        # test case 2
        nums1 = [1,0,1,1,0,1]
        output1 = solution.findMaxConsecutiveOnes(nums1)
        self.assertEqual(output1, 2)