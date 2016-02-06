'''

Implementation of Merge_Sort

1. Divide the list into 2 halfs
2. Recursively sort each half.
3. Merge 2 halfs

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
print "List after sort", sort (my_list)