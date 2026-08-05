class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float(inf)
        low = 0
        high = n - 1

        while high >= low:
            mid = (low + high) // 2

            if low == mid == high:
                return min(nums[mid], mini)

            if nums[low] == nums[mid] == nums[high]:
                mini=min(mini,nums[low])
                low = low + 1
                high = high - 1
                continue

            if nums[mid] <= nums[high]:

                mini = min(nums[mid], mini)
                high = mid - 1

            else:
                mini = min(nums[low], mini)
                low = mid + 1
        return mini
