from collections import deque
class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def id2rc(idx):
            r, c = (idx-1)//n, (idx-1)%n
            if r%2 ==1:
                c= n-1-c
            return int(n-1-r),int(c)
        vis = set()
        q = deque([(1,0)])
        while q:
            idx, step = q.popleft()
            for i in range(1, 6+1):
                idx_next = idx+i
                if idx_next >n * n:
                    break

                x_next,y_next = id2rc(idx_next)
                if board[x_next][y_next] >0:
                    idx_next = board[x_next][y_next]
                if idx_next == n*n:
                    return step+1
                if idx_next not in vis:
                    vis.add(idx_next)
                    q.append((idx_next,step+1))
        return -1

board =[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
solution = Solution()
print(solution.snakesAndLadders(board))