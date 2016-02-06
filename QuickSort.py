''' Using the extra array makes the task easier. But cost is too much

The reason Quick-Sort is preferred over merge sort even though the worst case scenario for merge sort is
faster than worst case scenario for quick sort is space complexity. Plus less data movement even if no of comparisons of quick sort
is 39% percent more than Merge sort.

Quick sort cost very less w.r.t space as its an in-place sorting algorithm.

But its not a stable Algorithm w.r.t key pairs sorting. and not suitable for small array size

Running time is : N log N

Best case : N log N
Worst case : N^2
Average Case : N log N


Improve the performance by median finding - and choosing median as pivot is best option
Finding the median of median sample.
'''

def merge(list):
    if len(list) < 2:
        return list
    n=len(list)
    pivot=list[n-1]
    left=[]
    right=[]
    mid=[]
    for item in list:
        if item<pivot:
            left.append(item)
        elif item>pivot:
            right.append(item)

    sort(left,right)
    mid.append(pivot)
    result=left+mid+right
    return result

def sort(left,right):

    new_left=left.sort()
    new_right=right.sort()
    return new_left,new_right


list=[9,7,5,11,12,2,14,3,10,6]
print "List before sorting", list
print "List after sorting",merge(list)