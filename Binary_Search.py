def Binary_Search(list, search):


    min = 0
    max = len(list) - 1

    if max < min or search not in list:
        print "Unable to search the element. Either the list is empty or search item doesnt exist"
        return -1



list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
search = 60

print Binary_Search(list,search)