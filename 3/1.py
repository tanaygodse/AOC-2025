with open("input1.txt", "r") as f:
    banks = f.read().split("\n")
    banks = [b for b in banks if b != ""]

res = 0

for b in banks:
    max_jolt = 0
    for i in range(0, len(b)):
        for j in range(i + 1, len(b)):
            if max_jolt < int(b[i] + b[j]):
                max_jolt = int(b[i] + b[j])
    res += max_jolt

print(res)
