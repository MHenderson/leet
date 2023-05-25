class Solution(object):
    def countOddCells(self, M):
        n_odd_cells = 0
        for row in M:
            for c in row:
                if(c % 2 == 1):
                    n_odd_cells = n_odd_cells + 1
        return(n_odd_cells)
    
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        M = [ [0]*n for i in range(m)]

        for p in indices:
            for j in range(n):
                M[p[0]][j] = M[p[0]][j] + 1
            for i in range(m):
                M[i][p[1]] = M[i][p[1]] + 1

        return(self.countOddCells(M))
