""" Insertion_Sort Implementation

Analysis : Approx 1/4th of N^2 compares and 1/4th of N^2 exchanges which is worse than selection sort

However it des depend on initial data set of the given array. If the array is sorted then
it requires N-1 comparisons but 0 exchanges which is the best case.

It also runs on linear time for partially sorted arrays

Good to use if array size is small

It holds stability by preserving the sorting of key pairs

Time Complexity:
Worst Case : O(n**2)
Best case : O (N)      --- Already sorted array or partially sorted array

Space Complexity: O(n) total
"""


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentvalue


alist = [7,10,5,3]
insertionSort(alist)
print(alist)
