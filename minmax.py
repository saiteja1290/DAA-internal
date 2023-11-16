def find_min_max(arr, start, end):
    if start ==  end:
        return arr[start], arr[end]
    
    if end - start == 1:
        return min(arr[start], arr[end]), max(arr[start], arr[end])
    
    mid = (start + end)// 2
    min1, max1 = find_min_max(arr, start, mid)
    min2, max2 = find_min_max(arr, mid+1, end)

    return min(min1, min2), max(max1, max2)
l = "abcdefg"
print(find_min_max(l, 0, len(l) - 1))