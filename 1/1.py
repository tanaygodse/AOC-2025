with open("input1.txt", "r") as f:
    moves = f.read().split("\n")
    moves = [move for move in moves if move != ""]

start = 50
dials = 100

res = 0

for move in moves:
    if "L" in move:
        start = (start - int(move[1:])) % dials
    else:
        start = (start + int(move[1:])) % dials

    if start == 0:
        res += 1

print(res)
