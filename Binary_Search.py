def Binary_Search(list, search):

    min = 0
    max = len(list) - 1

    if max <= min or search not in list:
        print "Unable to search the element. List is empty or Element is not present in list"

    while min <= max:
        mid = (min + max ) / 2
        if search > list[mid]:
            min = mid + 1
        elif search < list[mid]:
            max = mid -1
        else:
            print "Element",search,"found at position", mid
            break


list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
search = 67

Binary_Search(list,search)