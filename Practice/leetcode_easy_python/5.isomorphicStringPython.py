'''
Isomorphic string
Given two strings s and t, determine if they are isomorphic
{e: 'a', g: 'd'}
{a: 'e', d: 'g'}
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map={}
        t_map={}

        for i in range(len(s)):
            s_ch=s[i]
            t_ch=t[i]

            if s_ch not in s_map:
                s_map[s_ch]=t_ch
            if t_ch not in t_map:
                t_map[t_ch]=s_ch
            if t_map[t_ch] != s_ch or s_map[s_ch]!= t_ch:
                return False
        return True

class Solution1:
    def isIsomarphic(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        s_map={}
        t_map={}
        for i in range(len(s)):
            s_ch=s[i]
            t_ch=t[i]

            if s_ch not in s_map:
                s_map[s_ch] = t_ch
            if t_ch not in t_map:
                t_map[t_ch]=s_ch
            if s_map[s_ch]!=t_ch or t_map[t_ch]!=s_ch:
                return False
        return True
    
if __name__=="__main__":
    sol=Solution()
    sol1=Solution1()
    s="egge"
    t="adda"
    print(sol.isIsomorphic(s,t))
    print(sol1.isIsomarphic(s,t))