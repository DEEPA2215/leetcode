class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans=[]
        for i in range(len(s)):
            min_dist=float('inf')
            for j in range(len(s)):
                if s[j]==c:
                    min_dist=min(min_dist,abs(i-j))
            ans.append(min_dist)
        return ans                

        