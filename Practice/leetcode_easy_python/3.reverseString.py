from typing import List

class Solution:
    def reverseString(self, s: List[str])->None:
        left = 0
        right = len(s)-1
        while left < right:
            hold=s[left]
            s[left]=s[right]
            s[right]=hold

            left+=1
            right-=1
            print(s)

if __name__=="__main__":
    sol=Solution()
    str=["h","e","l","j"]
    sol.reverseString(str)
