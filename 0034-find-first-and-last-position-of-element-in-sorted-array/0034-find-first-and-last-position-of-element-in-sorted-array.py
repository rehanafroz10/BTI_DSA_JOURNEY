class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def Lower_bound(nums, target):
            n = len(nums)
            l_b = -1
            low = 0
            high = n-1
            while high >= low:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid - 1
                    l_b = mid
                else:
                    low = mid + 1

            return l_b

        def Upper_bound(nums, target):
            n = len(nums)
            u_b = n
            low = 0
            high = n-1
            while high >= low:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                    u_b = mid
                else:
                    low = mid + 1

            return u_b

        lb = Lower_bound(nums, target)
        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        ub = Upper_bound(nums, target)

        return [lb, ub - 1]
