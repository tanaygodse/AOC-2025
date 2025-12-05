with open("input1.txt", "r") as f:
    x = f.read().split("\n")
    ranges = [r for r in x if "-" in r]
    ids = [id for id in x if id != "" and "-" not in id]

res = 0
for id in ids:
    for r in ranges:
        start, end = r.split("-")
        start, end = int(start), int(end)
        if start <= int(id) <= end:
            res += 1
            break

print(res)
