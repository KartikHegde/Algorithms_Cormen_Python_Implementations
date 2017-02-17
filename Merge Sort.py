'''
Implementation of Merge_Sort

1. Divide the list into 2 halfs
2. Recursively sort each half.
3. Merge 2 halfs


Time Complexity : O(n log n)

Space Complexity: O(n)

However, it needs extra space to hold the merged array from subarray's. Thus it doesnt belong
to category of in-place memory algorithms like shell, insertion or selection.

And its complicated to use, if sub-array size is very small as there are too much overhead because of
recursive calls.

Lower bound = n log n
Upper bount = n log n

Hence Merge sort is an optimal Algorithm w.r.t comparisons but not w.r.t space

Also, Merge sort holds stability by preserving the sorting of key pairs along with Insertion sort.

Time Complexity :
worst case : O(n log n)
Best case : O(n log n)

'''


def merge_sort(lst):
    """Sorts the input list using the merge sort algorithm.
    #
    # >>> lst = [4, 5, 1, 6, 3]
    # >>> merge_sort(lst)
    [1, 3, 4, 5, 6]
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.
    #
    # >>> left = [1, 5, 6]
    # >>> right = [2, 3, 4]
    # >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])



my_list = [8,5,9,2,6,1,3,4]

# while True:
#     line = raw_input("Enter the numbers for sorting\n")
#     if line == 'done':
#         break
#     try:
#         my_input = int(line)
#         my_list.append(my_input)
#     except:
#         print "Error"

print "List before sort", my_list
print "List after sort", merge_sort(my_list)

# def merge(left, right):
#     result_list = []
#     n, m = 0, 0
#     while n < len(left) and m < len(right):
#         if left[n] <= right[m]:
#             result_list.append(left[n])
#             n += 1
#         else:
#             result_list.append(right[m])
#             m += 1
#     #
#     print left[n]
#     print right[m:]
#     result_list += left[n]
#     result_list += right[m]
#     return result_list
#
#
# def sort(my_list):
#     if len(my_list) <= 1:
#         return my_list
#
#     middle = int(len(my_list) / 2)
#     left = sort(my_list[:middle])
#     right = sort(my_list[middle:])
#     return merge(left, right)


