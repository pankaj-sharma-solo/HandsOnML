from DSA import StopWatch

def isValid(arr, curr, next):
    if abs(arr[curr] - arr[next]) > 1:
        return False
    return True

def solve(arr, curr, next, out):
    if next == len(arr):
        out.append(arr[curr])
        return out

    temp = out.copy()
    res1 = []
    if isValid(arr, curr, next):
        # print(arr[curr], end=" ")
        out.append(arr[curr])
        res1 = solve(arr, next, next + 1, out)
        # print(f"inner: {res1}")
    res2 = solve(arr, curr, next + 1, temp)
    # print(f"outer: {res2}")

    return res1 if len(res1) > len(res2) else res2

def print_solution(out):
    if len(out) < 2:
        return
    print(out)

if __name__ == "__main__":
    # StopWatch.start()
    arr = [9, 10, 12, 4, 3, 2, 4, 1, 3, 2]
    res = []
    for i in range(len(arr)):
        out  = solve(arr, i, i+1, [])
        if len(res) < len(out):
            res = out
    print(res)
    StopWatch.stop()
    StopWatch.elapsed()