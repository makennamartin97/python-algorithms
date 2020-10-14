# bubble sort
# It is a comparison-based algorithm in which each pair of adjacent elements 
# is compared and the elements are swapped if they are not in order.



def bubblesort(list):
    # Swap the elements to arrange in order
    for i in range(len(list)-1,0,-1): # start stop step
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(bubblesort(list))


