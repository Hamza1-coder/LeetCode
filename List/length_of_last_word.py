import unittest

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.strip().split(" ")[-1])

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        l = 0
        for i in range(n, 0, -1):
            if s[i] != " ":
                l += 1
            elif s[i] == " " and l != 0:
                break 
        return l 
                
      


class TestSolution(unittest.TestCase):
   def test_lengthOfLastWord(self):
      solution = Solution()
      # testcase 1
      s1 = "Hello World"
      output_1 = solution.lengthOfLastWord(s1)
      self.assertEqual(output_1, 5)

      # testcase 2
      s2 = "   fly me   to   the moon  "
      output_2 = solution.lengthOfLastWord(s2)
      self.assertEqual(output_2, 4)

if __name__ == "__main__":
    unittest.main()