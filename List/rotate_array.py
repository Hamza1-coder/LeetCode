from typing import List
import unittest

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    
    
class TestSolution(unittest.TestCase):
    def test_rotate(self):
        solution = Solution()
        # testcase 1
        list1 = [1,2,3,4,5,6,7]
        k1 = 3
        output_list1 = solution.rotate(list1, k1)
        self.assertEqual(output_list1, [5,6,7,1,2,3,4])
        
        # testcase 2
        list2 = [-1,-100,3,99]
        k2 = 2
        output_list2 = solution.rotate(list2, k2)
        self.assertEqual(output_list2, [3,99,-1,-100])
        
if __name__ == "__main__":
    unittest.main()