from typing import List
import unittest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if (nums[i] != nums[j]):
                i+=1
                nums[i] = nums[j]
        return i+1
    
class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = Solution()
        # testcase 1
        list1 = [1,1,2]
        output_list1 = solution.removeDuplicates(list1)
        self.assertEqual(output_list1, 2)
        
        # testcase 2
        list2 = [0,0,1,1,1,2,2,3,3,4]
        output_list2 = solution.removeDuplicates(list2)
        self.assertEqual(output_list2, 5)
        
if __name__ == "__main__":
    unittest.main()