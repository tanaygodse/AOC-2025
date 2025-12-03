with open("input1.txt", "r") as f:
    ranges = f.read().replace("\n", "").split(",")

res = 0
print(ranges)
for r in ranges:
    split_ranges = r.split("-")
    start, end = split_ranges[0], split_ranges[-1]
    for id in range(int(start), int(end) + 1):
        id = str(id)
        if len(id) % 2 == 0 and id[: len(id) // 2] == id[len(id) // 2 :]:
            res += int(id)
print(res)
