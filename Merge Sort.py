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


def merge(left, right):
    result_list = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result_list.append(left[n])
            n += 1
        else:
            result_list.append(right[m])
            m += 1

    result_list += left[n:]
    result_list += right[m:]
    return result_list


def sort(my_list):
    if len(my_list) <= 1:
        return my_list

    middle = int(len(my_list) / 2)
    left = sort(my_list[:middle])
    right = sort(my_list[middle:])
    return merge(left, right)


my_list = []

while True:
    line = raw_input("Enter the numbers for sorting\n")
    if line == 'done':
        break
    try:
        my_input = int(line)
        my_list.append(my_input)
    except:
        print "Error"

print "List before sort", my_list
print "List after sort", sort(my_list)
