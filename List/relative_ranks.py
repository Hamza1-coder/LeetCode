from typing import List
import unittest

class Solution:
    # this solution in memory efficient but not good in runtime
    # def findRelativeRanks(self, score: List[int]) -> List[str]:
    #     so = sorted(score, reverse=True)
    #     for s in range(len(score)):
    #         if score[s] == so[0]:
    #             score[s] = "Gold Medal"
    #         elif score[s] == so[1]:
    #             score[s] = "Silver Medal"
    #         elif score[s] == so[2]:
    #             score[s] = "Bronze Medal"
    #         else:
    #             score[s] = str(so.index(score[s]) + 1)
    #     return score
    
    # this is another way to do the same problem
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_map = {}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        scores = sorted(score, reverse=True)
        for i, s in enumerate(scores):
            rank_map[s] = i + 1
        for i, s in enumerate(score):
            if rank_map[s] <= 3:
                score[i] = medals[rank_map[s] -  1]
            else:
                score[i] = str(rank_map[s])
        return score
        
        
    
    
class TestSolution(unittest.TestCase):
    def test_findRelativeRanks(self):
        solution = Solution()
        # testcase 1
        score = [5,4,3,2,1]
        output_list = solution.findRelativeRanks(score)
        self.assertEqual(output_list, ["Gold Medal","Silver Medal","Bronze Medal","4","5"])
        
        # testcase 2
        score = [10,3,8,9,4]
        output_list = solution.findRelativeRanks(score)
        self.assertEqual(output_list, ["Gold Medal","5","Bronze Medal","Silver Medal","4"])
        
if __name__ == "__main__":
    unittest.main()