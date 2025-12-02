with open("input1.txt", "r") as f:
    moves = f.read().split("\n")
    moves = [move for move in moves if move != ""]

start = 50
dials = 100

res = 0

for move in moves:
    old = start
    count = int(move[1:])

    if "L" in move:
        start -= count
        res += abs(start // dials)
        start = start % dials
        if start == 0:
            res += 1
        elif old == 0:
            res -= 1
    else:
        start += count
        res += start // dials
        start = start % dials

print(res)
