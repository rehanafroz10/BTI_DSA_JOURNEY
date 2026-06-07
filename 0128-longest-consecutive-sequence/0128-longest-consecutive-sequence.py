class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n =len(nums)
        count=0
        max=0
        last_smallest=float('-inf')
        nums.sort()
        for i in range(0,n):
            x=nums[i]
        #     count=1
        #     while x+1 in nums:
        #         count+=1
        #         x+=1
        #     if count>=max:
        #         max=count
        # return max
            if x-1==last_smallest:
                count+=1
                last_smallest=x
            elif x!=last_smallest:
                count=1
                last_smallest=x
            if count>max:
                max=count
        return max


        