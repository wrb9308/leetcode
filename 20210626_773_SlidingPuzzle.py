"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Input: board = [[3,2,4],[1,5,0]]
Output: 14
"""
from collections import deque
import copy
class Solution:
    def slidingPuzzle(self, board):
        target = [[1,2,3],[4,5,0]]
        if board == target:
            return 0

        def find_loc(board_temp):
            for i in range(2):
                for j in range(3):
                    if board_temp[i][j] == 0:
                        return i, j

        def neighbors(board_ego):
            i, j = find_loc(board_ego)
            result = []
            adjacency = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dx, dy in adjacency:
                if 0 <= (i + dx) < 2 and 0 <= j + dy < 3:
                    board_temp = copy.deepcopy(board_ego)
                    temp = board_temp[i+dx][j+dy]
                    board_temp[i + dx][j + dy] = board_temp[i][j]
                    board_temp[i][j] = temp
                    result.append(board_temp)
            return result

        q = deque([(board, 0)])
        seen = []
        seen.append(board)

        while q:
            board_current, step = q.popleft()
            for board_next in neighbors(board_current):
                if board_next == target:
                    return step + 1
                if board_next not in seen:
                    seen.append(board_next)
                    q.append((board_next, step+1))
        return -1


board = [[1,2,3],[4,0,5]]
solution = Solution()
print(solution.slidingPuzzle(board))