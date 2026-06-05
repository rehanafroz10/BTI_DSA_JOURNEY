class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        mid =n//2
        if n==1:
            return nums
        left_arr=nums[:mid]
        right_arr=nums[mid:]
        left_sorted=self.sortArray(left_arr)
        right_sorted=self.sortArray(right_arr)
        return self.mergetwoarray(left_sorted,right_sorted)

    def mergetwoarray(self,left,right):
        a=len(left)
        b=len(right)
        result=[]
        i,j=0,0
        while i<a and j<b:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<a:
            result.append(left[i])
            i+=1
        while j<b:
            result.append(right[j])
            j+=1
        
        return result


        