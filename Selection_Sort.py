'''

Selection_Sort Implementation

Let the first element in the array be the least. Scan through rest of the array and if
a value less than least is found, make it the new least And swap with old least

Selection_Sort running time needs N-1 + N-2 + ..... Comparisons and N exchanges which is a quadratic time.
Thus the running time is N^2 in all conditions no matter if array is sorted or partially sorted.

'''

def Selectionsort( array ):
  for i in range( len( array ) ):
    least_value = i
    for k in range( i + 1 , len( array ) ):
      if array[k] < array[least_value]:
        least_value = k

    swap( array, least_value, i )


def swap( array, least_value, i ):
  temp = array[least_value]
  array[least_value] = array[i]
  array[i] = temp


list = [54,26,93,17,77,31,44,55,20]
print "Array before sorting", list
Selectionsort(list)
print "Array after sorting", list