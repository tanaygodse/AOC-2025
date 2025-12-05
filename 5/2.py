with open("input1.txt", "r") as f:
    x = f.read().split("\n")
    ranges = [r for r in x if "-" in r]
    ids = [id for id in x if id != "" and "-" not in id]

combined = []

processed = []

for r in ranges:
    start, end = r.split("-")
    start, end = int(start), int(end)
    processed.append([start, end])

processed.sort(key=lambda x: x[0])

prev_start, prev_end = processed[0][0], processed[0][1]

i = 1
while i < len(processed):
    while i < len(processed) and prev_end >= processed[i][0]:
        prev_end = max(prev_end, processed[i][1])
        i += 1
    if i >= len(processed):
        break
    combined.append([prev_start, prev_end])
    prev_start, prev_end = processed[i][0], processed[i][1]
    i += 1

if combined[-1] != [prev_start, prev_end]:
    combined.append([prev_start, prev_end])


res = 0
for s, e in combined:
    res += e - s + 1

print(res)
