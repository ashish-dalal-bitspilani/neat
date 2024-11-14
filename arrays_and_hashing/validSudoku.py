class Solution:

    def __init__(self, problem):
        self.problem = problem

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for row in range(9)]
        columns = [set() for column in range(9)]
        boxes = [set() for box in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box_index = (i // 3) * 3 + j // 3

                if num != ".":
                    if num in rows[i] or num in columns[j] or num in boxes[box_index]:
                        return False
                    else:
                        rows[i].add(num)
                        columns[j].add(num)
                        boxes[box_index].add(num)
        return True

if __name__ == "__main__":

    solution = Solution("validSudoku")
    print("===========================================")
    print(solution.isValidSudoku([["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]))
    print(solution.isValidSudoku([["1", "2", ".", ".", "3", ".", ".", ".", "."], ["4", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", "9", "1", ".", ".", ".", ".", ".", "3"], ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
     [".", ".", ".", "8", ".", "3", ".", ".", "5"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", ".", ".", ".", ".", ".", "2", ".", "."], [".", ".", ".", "4", "1", "9", ".", ".", "8"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print("===========================================")