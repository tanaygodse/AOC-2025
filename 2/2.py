with open("input1.txt", "r") as f:
    ranges = f.read().replace("\n", "").split(",")

res = 0

for r in ranges:
    split_ranges = r.split("-")
    start, end = split_ranges[0], split_ranges[-1]
    for id in range(int(start), int(end) + 1):
        id = str(id)
        for i in range(len(id) // 2):
            pattern = id[: i + 1]
            pat_len = len(id[: i + 1])
            if pattern * (len(id) // pat_len) == id:
                res += int(id)
                break

print(res)
