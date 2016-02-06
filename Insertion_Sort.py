# Insertion_Sort Implementation


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





