from collections import deque

def solution(heights, startRow, startCol):
    #I'd need the entire time just to do this one question.
    # Dimensions of the grid
    rows = len(heights)
    cols = len(heights[0])
    
    # Initialize the wet_time grid with -1 (dry cells)
    wet_time = [[-1 for _ in range(cols)] for _ in range(rows)]
    
    # BFS queue, starting with the initial water source at time 0
    queue = deque([(startRow, startCol, 0)])
    wet_time[startRow][startCol] = 0  # Starting point gets wet at time 0
    
    # Directions for moving in the grid (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Process the queue
    while queue:
        row, col, time = queue.popleft()
        
        # Check all 4 possible directions
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            
            # Check if the new cell is within bounds
            if 0 <= newRow < rows and 0 <= newCol < cols:
                # Water flows to the new cell if it's lower or equal height and hasn't been visited
                if heights[newRow][newCol] <= heights[row][col] and wet_time[newRow][newCol] == -1:
                    wet_time[newRow][newCol] = time + 1  # Mark it wet at the next time step
                    queue.append((newRow, newCol, time + 1))  # Add to queue for further exploration

    return wet_time


