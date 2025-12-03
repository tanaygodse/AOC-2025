with open("input1.txt", "r") as f:
    banks = f.read().split("\n")
    banks = [b for b in banks if b != ""]

res = 0
k = 12

for b in banks:
    n = len(b)
    dp = [[None] * (k + 1) for _ in range(n + 1)]
    dp[n][0] = ""

    for i in range(n - 1, -1, -1):
        curr = b[i]

        dp[i][0] = ""

        for j in range(1, k + 1):
            pick = None
            not_pick = None

            if dp[i + 1][j - 1] is not None:
                pick = curr + dp[i + 1][j - 1]

            not_pick = dp[i + 1][j]

            if pick is not None and not_pick is not None:
                dp[i][j] = max(pick, not_pick)
            elif pick:
                dp[i][j] = pick
            else:
                dp[i][j] = not_pick

    res += int(dp[0][k] if dp[0][k] else 0)

print(res)
