class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        result=[[0]*n for i in range(n)]
        temp=[]
        for i in range(1,((n**2)+1)):
            temp.append(i)
        t=0
        l=0
        bo=n-1
        ri=n-1
        count=0
        while t<=bo and l <=ri:
            for i in range (l,ri+1):
                result[l][i]=temp[count]
                count+=1
            t+=1

            for j in range(t,bo+1):
                result[j][ri]=temp[count]
                count+=1
            ri-=1

            for k in range(ri,l-1,-1):
                result[bo][k]=temp[count]
                count+=1
            bo-=1

            for m in range(bo,t-1,-1):
                result[m][l]=temp[count]
                count+=1
            l+=1

        return result



