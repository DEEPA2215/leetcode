class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq=[]
        for i in set(tasks):
            freq.append(tasks.count(i))
        max_count=max(freq)
        same=freq.count(max_count)
        intervals=(max_count-1)*(n+1)+same
        return max(len(tasks),intervals)