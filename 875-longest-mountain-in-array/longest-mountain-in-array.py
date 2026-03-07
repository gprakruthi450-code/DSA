class Solution(object):
    def longestMountain(self, arr):
        n=len(arr)
        result=0

        for i in range(1,n-1): # i = 1 
           if arr[i-1]<arr[i]>arr[i+1]:
              l=i
              r=i
              while l>0 and arr[l]>arr[l-1]:
                  l-=1
              while r<n-1 and arr[r]>arr[r+1]:
                  r+=1

              result=max(result,r-l+1)

        return result