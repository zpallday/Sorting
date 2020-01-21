# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
     min_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
     for j in range (i+1, len(arr)): 
        if arr[min_index] > arr[j]: 
            min_index = j
     arr[i], arr[min_index] = arr[min_index], arr[i]


        # TO-DO: swap
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
   swap = True
   while swap == True:
     swap = False
     for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
           arr[i], arr[i + 1]  = arr[i+1], arr[i]
           swap = True
   return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr