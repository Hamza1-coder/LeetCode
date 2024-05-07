from typing import List
import unittest
class Solution:
    # straight forward way to solve this problem
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if not nums[j]:
                nums.append(nums[j])
                nums.pop(j)
            else:
                j+=1
        return nums
    
    # swap the zeros value with non-zeors values and move the zeros in the end of the list
    """  
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
    """
    
class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()
        # testcase 1
        nums = [0,1,0,3,12]
        output_list = solution.moveZeroes(nums)
        self.assertEqual(output_list, [1,3,12,0,0])
        
        # testcase 2
        nums1 = [0]
        output_list1 = solution.moveZeroes(nums1)
        self.assertEqual(output_list1, [0])
        
if __name__ == "__main__":
    unittest.main()