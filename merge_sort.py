def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive call on each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add remaining elements from both halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print(sorted_list)































def merge_main(nums):
    mid  = len(nums)//2
    left_part = nums[:mid]
    right_part = nums[mid:]
    return mergesort(left_part, right_part)
def mergesort(left_half, right_half):
    merger_list = []
    left, right = 0, 0
    while(left<len(left_half) and right < len(right_half)):
        if left_half[left]< right_half[right]:
            merger_list.append()
