def Binary_Search(list, search):
    if (len(list) == 0):
        return "Not Found"
    else:
        mid = len(list) // 2
        if (list[mid]== search):
            return "Found"
        else:
            if search > list[mid]:
                return Binary_Search(list[mid+1:],search)
            else:
                return Binary_Search(list[:mid],search)
# List of prime numbers

list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

my_input = raw_input("Enter the element you want to search\n")
search = int(my_input)

print Binary_Search(list,search)