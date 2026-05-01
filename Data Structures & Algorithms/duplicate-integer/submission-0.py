class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}

        for i in nums:
            if i not in list(dic.keys()):
                dic[i]=1
            else:
                return True

        return False
        