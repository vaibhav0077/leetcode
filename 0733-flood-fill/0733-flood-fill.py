class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[-1 for i in range(n)] for j in range(m)]
        startColor = image[sr][sc]
        def sol(i, j):
            if i < 0 or j < 0 or i >= m or j >= n :
                return 0
            if visited[i][j] != -1 : return 0
            visited[i][j] = 0
            
            if image[i][j] == startColor:
                image[i][j] = color
            else:
                return
            up = sol(i-1, j)
            down = sol(i+1, j)
            right = sol(i, j+1)
            left = sol(i, j-1)
            
            return image
        
        return sol(sr, sc)
            