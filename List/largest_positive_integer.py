from typing import List
import unittest

class Solution:
    # BruteForce Approch
    # def findMaxK(self, nums: List[int]) -> int:
    #     ans = []
    #     for i in range(len(nums)):
    #         if -nums[i] in nums:
    #             ans.append(nums[i])
    #     return -1 if len(ans) == 0 else max(ans)
    
    # Optimal Approch
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_num = -1
        for n in nums:
            if -n in nums_set:
                max_num = max(max_num, n)
        return max_num
    
    
class TestSolution(unittest.TestCase):
    def test_findMaxK(self):
        solution = Solution()
        # test case 1
        nums = [-1,2,-3,3]
        output = solution.findMaxK(nums)
        self.assertEqual(output, 3)
        # test case 2
        nums1 = [-1,10,6,7,-7,1]
        output1 = solution.findMaxK(nums1)
        self.assertEqual(output1, 7)
        # test case 3
        nums2 = [-10,8,6,7,-2,-3]
        output2 = solution.findMaxK(nums2)
        self.assertEqual(output2, -1)
        
        
if __name__ == "__main__":
    unittest.main()