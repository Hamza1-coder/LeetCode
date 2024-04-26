from typing import List
import unittest

# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         if nums == sorted(nums):
#             return True
#         k = 1
#         n = len(nums)
#         while k < n:
#             arr = nums[n - k :] + nums[: n - k]
#             if arr == sorted(nums):
#                 return True
#             k+=1
#         return False


class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        nums_double = nums + nums
        n = len(nums)
        for i in range(n):
            if nums_double[i:i+n] == sorted_nums:
                return True
        return False

class TestSolution(unittest.TestCase):
    def test_check(self):
        solution = Solution()
        # testcase 1
        list1 = [3,4,5,1,2]
        output_list1 = solution.check(list1)
        self.assertEqual(output_list1, True)
        
        # testcase 2
        list2 = [2,1,3,4]
        output_list2 = solution.check(list2)
        self.assertEqual(output_list2, False)
        
if __name__ == "__main__":
    unittest.main()