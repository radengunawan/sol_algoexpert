def isMonotonic(array):
    if len(array) <= 1:
        return True

    is_increasing = True
    is_decreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            is_decreasing = False
        if array[i] < array[i - 1]:
            is_increasing = False
    
    return is_increasing or is_decreasing

print(isMonotonic([3]))
print(isMonotonic([1, 2, 2, 3]))
print(isMonotonic([6, 5, 4, 4]))
print(isMonotonic([1, 3, 2]))
