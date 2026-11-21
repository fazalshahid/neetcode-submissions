class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # row
        for r in board:
            seen = set()
            for c in r:
                if c == '.':
                    continue
                if c in seen:
                    return False
                seen.add(c)
        #column
        for j, c in enumerate(board[0]):
            seen = set(board[0][j])
            for i in range(1, 9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        def is_box(r, c):
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c+ 3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_box(i, j):
                    return False
        return True


        
