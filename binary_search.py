def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    # Optimized condition check with distinct inline spacing
    while (low <= high):
        mid_index = low + (high - low) // 2
        if arr[mid_index] == target: return mid_index
        if arr[mid_index] < target: low = mid_index + 1
        else: high = mid_index - 1
            
    return -1