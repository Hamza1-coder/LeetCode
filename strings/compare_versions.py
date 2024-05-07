import unittest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = [int(x) for x in version1.split(".")] + [0] * (len(version2) - len(version1))
        j = [int(y) for y in version2.split(".")] + [0] * (len(version1) - len(version2))

        for x, y in zip(i, j):
            if x != y:
                if x < y: return -1
                if x > y: return 1
        return 0
    

class TestSolution(unittest.TestCase):
    def test_compareVersion(self):
        solution = Solution()
        # testcase 1
        version1 = "1.01"
        version2 = "1.001"
        output = solution.compareVersion(version1, version2)
        self.assertEqual(output, 0)
        
        # testcase 2
        version1 = "0.1"
        version2 = "1.1"
        output = solution.compareVersion(version1, version2)
        self.assertEqual(output, -1)
        
        # test case 3
        version1 = "1.0"
        version2 = "1.0.0"
        output = solution.compareVersion(version1, version2)
        self.assertEqual(output, 0)
        
if __name__ == "__main__":
    unittest.main()