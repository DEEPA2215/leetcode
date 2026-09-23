class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        def backtrack(i, j, k):

            # Invalid check
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            # Character check
            if board[i][j] != word[k]:
                return False

            # Word completed
            if k == len(word) - 1:
                return True

            # Mark visited
            temp = board[i][j]
            board[i][j] = '#'

            # Directions
            found = (
                backtrack(i + 1, j, k + 1) or
                backtrack(i - 1, j, k + 1) or
                backtrack(i, j + 1, k + 1) or
                backtrack(i, j - 1, k + 1)
            )

            # Backtrack
            board[i][j] = temp

            return found

        # Start from every cell
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False