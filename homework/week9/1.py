# maze_dfs.py

def dfs_maze(maze, start, end):
    """使用深度優先搜尋 (DFS) 尋找迷宮路徑"""
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set([start])
    
    # 上、下、左、右 移動方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        current, path = stack.pop()
        
        if current == end:
            return path
        
        for dr, dc in directions:
            next_r, next_c = current[0] + dr, current[1] + dc
            next_pos = (next_r, next_c)
            
            # 檢查是否在邊界內、是否為通道(0)、且未造訪過
            if (0 <= next_r < rows and 0 <= next_c < cols and 
                maze[next_r][next_c] == 0 and next_pos not in visited):
                visited.add(next_pos)
                stack.append((next_pos, path + [next_pos]))
                
    return None

if __name__ == "__main__":
    # 0 代表通道，1 代表牆壁
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    
    path = dfs_maze(maze, start, end)
    print("=== 1. 老鼠走迷宮 (DFS) ===")
    print("尋找到的路徑座標:", path)