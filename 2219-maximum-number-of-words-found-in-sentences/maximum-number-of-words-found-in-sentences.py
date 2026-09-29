class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_count = 0

        for i in sentences:
            count = len(i.split())

            if count > max_count:
                max_count = count

        return max_count
        