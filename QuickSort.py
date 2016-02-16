''' Using the extra array makes the task easier. But cost is too much

The reason Quick-Sort is preferred over merge sort even though the worst case scenario for merge sort is
faster than worst case scenario for quick sort is space complexity. Plus less data movement even if no of comparisons of quick sort
is 39% percent more than Merge sort.

Quick sort cost very less w.r.t space as its an in-place sorting algorithm.

But its not a stable Algorithm w.r.t key pairs sorting. and not suitable for small array size

Time Complexity : O(n log n)

Best case : O(n log n)
Worst case : O(n**2)
Average Case : O(n log n)


Improve the performance by median finding - and choosing median as pivot is best option
Finding the median of median sample.
'''

import random
def qsort(L):
    if len(L)<2: return L
    pivot_element = random.choice(L)
    small = [i for i in L if i< pivot_element]
    medium = [i for i in L if i==pivot_element]
    large = [i for i in L if i> pivot_element]
    return qsort(small) + medium + qsort(large)


my_list = [3,2,6,9,4,1,8,7,14,10,5]
print "List before sort",my_list
print "List after Sort",qsort(my_list)