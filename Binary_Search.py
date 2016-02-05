#Implementation of Binary Search

# Given : 1. A sorted array
#         2. A key to search

#Logic : Compare the key againast middle term
# Too small, Go left
# Too large, Go right

# Output : Search element's Index position


def Binary_Search(list, search):

    min = 0
    max = len(list) - 1

    if max <= min or search not in list:
        print "Unable to search the element. Either list is empty or element is not present in the list"

    while min <= max:
        mid = (min + max ) / 2
        if search > list[mid]:
            min = mid + 1
        elif search < list[mid]:
            max = mid -1
        else:
            print "Element",search,"found at position", mid
            break

# List of prime numbers

list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

my_input = raw_input("Enter the element you want to search\n")
search = int(my_input)

Binary_Search(list,search)