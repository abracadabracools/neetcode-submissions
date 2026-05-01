class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dic_s = {}
            dic_t = {}

            for i in range(len(s)):
                if s[i] not in list(dic_s.keys()):
                    dic_s[s[i]]=1
                else:
                    dic_s[s[i]]=dic_s[s[i]] + 1

                if t[i] not in list(dic_t.keys()):
                    dic_t[t[i]]=1
                else:
                    dic_t[t[i]]=dic_t[t[i]] + 1
            
            if dic_s == dic_t:
                return True
            else:
                return False
            
        else:
            return False
                