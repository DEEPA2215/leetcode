class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        happy=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                happy+=customers[i]
        window=0
        max_window=0
        for i in range(len(customers)) :
            if grumpy[i]==1:
                window+=customers[i]
            if i>=minutes:
                if grumpy[i-minutes]==1:
                    window-=customers[i-minutes]
            max_window=max(max_window,window)
        return happy+max_window   