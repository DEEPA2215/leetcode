class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=0
        c1=0
        
        for i in range(len(word)):
            
            if word[i]>='A' and word[i]<='Z':
                count+=1
            if word[i]>='a' and word[i]<='z':
                c1+=1    

        if count==len(word):
            return True
        elif c1==len(word):
            return True    
        elif word[0]>='A' and word[0]<='Z' and c1==len(word)-1:
            return True    
            
        else:
            return False    