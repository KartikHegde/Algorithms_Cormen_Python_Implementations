__author__ = "Karthik"

'''Implementation of Binary Search

# Given : 1. A sorted array
#         2. A key to search

Logic : Compare the key againast middle term
Too small, Go left
Too large, Go right

Output : Search element's Index position

Running time :
Worst Case : O(log n to the base 2)
Average Case : O(log n to the base 2)
Best Case : O(1)

Worst case space complexity : O(1)

When used : 1. Switch cases 2. Best to access ordered data which doesnt change often 3. Debuggiing

Data Structure Used : Array  '''


def Binary_Search(list, search):
    low = 0
    high = len(list) - 1

    if len(list) == 0:
        print "Unable to search the element. List is empty."

    while low <= high:
        mid = (low + high) / 2
        if search > list[mid]:
            low = mid + 1
        elif search < list[mid]:
            high = mid - 1
        else:
            print "Element", search, "found at position", mid
            break

    if low > high:
        print "Not Found"

# List of prime numbers

list = [2, 3, 5, 7, 11,13]

try:
    my_input = raw_input("Enter the element you want to search\n")
    search = int(my_input)
    Binary_Search(list, search)
except:
    print "Wrong Input"

