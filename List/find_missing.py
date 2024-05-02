from typing import List
import unittest

class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     nums = sorted(nums)
    #     for i in range(len(nums)):
    #         if nums[i] != i:
    #             return i
    #     return len(nums)
    
    
    # Using Summation Formula 
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        return ((N * (N + 1)) // 2) - sum(nums)
    
    
class TestSolution(unittest.TestCase):
    def test_missingNumber(self):
        solution = Solution()
        # testcase 1
        nums = [3,0,1]
        output_list = solution.missingNumber(nums)
        self.assertEqual(output_list, 2)
        
        # testcase 2
        nums1 = [0,1]
        output_list1 = solution.missingNumber(nums1)
        self.assertEqual(output_list1, 2)
        
        # testcase 3
        nums2 = [9,6,4,2,3,5,7,0,1]
        output_list2 = solution.missingNumber(nums2)
        self.assertEqual(output_list2, 8)
        
        
if __name__ == "__main__":
    unittest.main()
    