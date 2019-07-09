# recurse and may waste time too much.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        res=[]
        for i in range(0,len(nums)):
            res_list=self.permute(nums[0:i]+nums[i+1:])
            for res_list_ele in res_list:
                res+=[[nums[i]]+res_list_ele]
        return res

