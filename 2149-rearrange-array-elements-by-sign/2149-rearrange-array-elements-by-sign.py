class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        positive_idx,negative_idx=0,1

        for i in range(0,n):
            if nums[i]>0:
                result[positive_idx]=nums[i]
                positive_idx+=2
            else:
                result[negative_idx]=nums[i]
                negative_idx+=2
        return result
        