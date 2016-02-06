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
print merge(list)