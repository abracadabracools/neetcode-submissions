class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max=-1
        res=[None]*len(arr)

        for i in range(len(arr)-1,-1,-1):
            if i == len(arr)-1:
                res[i] = max
                max = arr[i]
            else:
                res[i] = max
                if max<arr[i]:
                    max = arr[i]

        return res