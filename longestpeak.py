def longest_peak(array):
    longest_peak_length = 0
    i = 1  # Start from the second element because the first can't be a peak
    
    while i < len(array) - 1:
        # Check if array[i] is a peak
        is_peak = array[i - 1] < array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue
        
        # Explore left side of the peak
        left_idx = i - 1
        while left_idx > 0 and array[left_idx] > array[left_idx - 1]:
            left_idx -= 1
        
        # Explore right side of the peak
        right_idx = i + 1
        while right_idx < len(array) - 1 and array[right_idx] > array[right_idx + 1]:
            right_idx += 1
        
        # Calculate the peak's length
        current_peak_length = right_idx - left_idx + 1
        
        # Update the longest peak length found so far
        longest_peak_length = max(longest_peak_length, current_peak_length)
        
        # Move the index to the right of the current peak
        i = right_idx + 1
    
    return longest_peak_length

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longest_peak(array))  # Output should be 6
