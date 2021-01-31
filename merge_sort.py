def merge_sort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    mid = len(list_to_sort)//2
    left = list_to_sort[:mid]
    right = list_to_sort[mid:]

    # sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # merge the sorted halves
    sorted_list = []
    current_index_left = 0
    current_index_right = 0

    # sortedLeft's first element comes next
    # if it's less than sortedRight's first
    # element or if sortedRight is exhausted

    while len(sorted_list) < len(left) + len(right):
        if current_index_left < len(left) and (current_index_right == len(right) or \
           sorted_left[current_index_left] < sorted_right[current_index_right]):
            sorted_list.append(sorted_left[current_index_left])
            current_index_left += 1
        else:
            sorted_list.append(sorted_right[current_index_right])
            current_index_right += 1

    return sorted_list

print(merge_sort([1,3,2,6,4,5,7]))

# Time Complexity: O(nlogn)
