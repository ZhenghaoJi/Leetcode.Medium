class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in sorted(nums):
            result += [i+[num] for i in result if i+[num] not in result]
        return result

