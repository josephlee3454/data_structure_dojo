def selection_sort(arr):
    for i in range(0,len(arr)-1): ## loops through every index of array in python list 
        min_idx = i ## set min index at i 
        for j in range(i+1, len(arr)):## nested loop that that adds 1 to every starting index during every iteration4
            if arr[j] < arr[min_idx]: # checks if arr[j] is less than the arr[min_idx] basically its cheking if the value next to it is less than the current value that i sits at 
                min_idx = j # if it meets that condition it will reassign min_idx to j 
        if min_idx != i: # put this outside to keep it going through the whole list but this will reassign as long as min_idx is reassigned and does not eqaul i
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(arr) # moves the min values over to left through every iteration 
    return arr
arr = [5,3,7,8,2]
print(selection_sort(arr))