def longest_subarray(arr):
    left, mid, right = [], [], []
    for i in range(len(arr)):
        temp_left, temp_mid, temp_right = [], [], []
        for j in range(i+1, len(arr)):
            if arr[i] - arr[j] == -1:
                temp_left.append(j)
            elif arr[i] - arr[j] == 1:
                temp_right.append(j)
            elif arr[i] - arr[j] == 0:
                temp_mid.append(j)
            else:
                continue
        left.append(temp_left)
        right.append(temp_right)
        mid.append(temp_mid)

    print_list = lambda x: [arr[x[i]] for i in range(len(x))]
    # Find Max
    max_length = 0
    result_subarray = []

    for i in range(len(arr)):
        current_subarray = print_solution(i, left, mid, right, arr, [])
        if len(current_subarray) > max_length:
            max_length = len(current_subarray)
            result_subarray = current_subarray

    print("Longest Subarray:", result_subarray)

def print_solution(i, left, mid, right, arr, out):
    res1, res2, res3 = [], [], []
    l, m, o = 0, 0, 0

    if len(left[i]) == 0 and len(mid[i]) == 0 and len(right[i]) == 0:
        return out

    while l < len(left[i]) and m < len(mid[i]) and o < len(right[i]):
        min_value = min(left[i][l], mid[i][m], right[i][o])
        if left[i][l] == min_value:
            res1.append(left[i][l])
            l += 1
        elif mid[i][m] == min_value:
            res2.append(mid[i][m])
            m += 1
        elif right[i][o] == min_value:
            res3.append(right[i][o])
            o += 1

    while l < len(left[i]):
        res1.append(left[i][l])
        l += 1

    while m < len(mid[i]):
        res2.append(mid[i][m])
        m += 1

    while o < len(right[i]):
        res3.append(right[i][o])
        o += 1

    return out + [arr[i]] + res1 + res2 + res3


if __name__ == "__main__":
    arr = [1, 1, 4, 5, 4, 3, 1, 1, 0, 1, 2]
    longest_subarray(arr)
