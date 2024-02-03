class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(arr)
        count=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if (i+j)%k==0:
                    count+=1
        if n/2 == count:
            return "true"
        else:
            return "false"
arr = [1,2,3,4,5,6]
k = 10
solution = Solution()
answer = solution.canArrange(arr,k)
print(answer)