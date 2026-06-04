class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:


        # nums1.extend([0]*n)
        for i in range(0,n):
            nums1[m+i]=nums2[i]
        nums1.sort()
        # print(nums1)
        