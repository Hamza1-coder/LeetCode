import unittest

class Solution:
    # using two maps
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     t_st = {}
    #     s_st = {}
    #     for i in range(len(s)):
    #         if s[i] not in t_st:
    #           t_st[s[i]] = t[i]
    #         if t[i] not in s_st:
    #           s_st[t[i]] = s[i]
            
    #         if t_st[s[i]] != t[i] or s_st[t[i]] != s[i]:
    #             return False
                
    #     return True

    # store ASCII values of characters
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     t_st = [-1] * 128
    #     s_st = [-1] * 128
    #     for i in range(len(s)):
    #         if s_st[ord(s[i])] == -1:
    #             s_st[ord(s[i])] = t[i]
    #         if t_st[ord(t[i])] == -1:
    #             s_st[ord(t[i])] = s[i]

    #         if s_st[ord(s[i])] != t[i] or t_st[ord(t[i])] != s[i]:
    #             return False
    #     return True


    # using built-in methods
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = len(set(zip(s,t)))
        b = len(set(s))
        c = len(set(t))
        return a==b==c
        
        
class TestSolution(unittest.TestCase):
    def test_isIsomorphic(self):
        solution = Solution()
        # testcase 1
        s = "egg" 
        t = "add"
        output_1 = solution.isIsomorphic(s, t)
        self.assertEqual(output_1, True)

        # testcase 2
        s1 = "foo"
        t1 = "bar"
        output_2 = solution.isIsomorphic(s1, t1)
        self.assertEqual(output_2, False)

        # testcase 3
        s2 = "aab"
        t3 = "aaa"
        output_3 = solution.isIsomorphic(s2, t3)
        self.assertEqual(output_3, False)

if __name__ == "__main__":
    unittest.main()