class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        
        min_diff = arr[1] - arr[0]
        result = []

        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]

            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                result = result + [[arr[i], arr[i+1]]]

        return result
        