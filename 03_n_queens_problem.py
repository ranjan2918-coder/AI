# 3. N-Queens Problem

def solve(q, n=4):
    if len(q) == n:
        print(q)
        return
    for r in range(n):
        if all(r != x and abs(r-x) != len(q)-i
               for i, x in enumerate(q)):
            solve(q + [r])

solve([])
