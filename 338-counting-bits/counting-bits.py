class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(n+1):
            count=0
            x=i
            while x:
                if x%2==1:
                    count+=1
                x=x//2
            result.append(count)
        return result        

        