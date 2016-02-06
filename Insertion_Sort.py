''' Insertion_Sort Implementation

Analysis : Approx 1/4th of N^2 compares and 1/4th of N^2 exchanges which is worse than selection sort

However it des depend on initial data set of the given array. If the array is sorted then
it requires N-1 comparisons but 0 exchanges which is the best case.

It also on linear time for partially sorted arrays '''

def InsertionSort(my_array):
   for i in range(0,len(my_array)):
        for j in range(i,0,-1):
            if my_array[j]<my_array[j-1]:
                swap (my_array, j , j-1)
            else:
                break


def swap(list,x,y):
    temp = list[x]
    list[x] = list[y]
    list[y] = temp


my_list = [54,26,93,17,77,31,44,55,20]
print "Array before the sorting:", my_list
InsertionSort(my_list)
print "Array after the sorting:", my_list





