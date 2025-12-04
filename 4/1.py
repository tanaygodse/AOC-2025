with open("input1.txt", "r") as f:
    grid = f.read().split("\n")
    grid = [g for g in grid if g != ""]

rows = len(grid)
cols = len(grid[0])

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

res = 0

for r in range(rows):
    for c in range(cols):
        if not grid[r][c] == "@":
            continue
        count = 0
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                count += 1
        if count < 4:
            res += 1

print(res)
