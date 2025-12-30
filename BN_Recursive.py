def binary_search(arr,left,right,target): #O(logn) is the time complexity
    if left>right: #base condition
        return -1
    mid = left + (right-left)//2 #mid is the middle element of the array
    if arr[mid]== target: #if the middle element is the target element
        return mid
    elif arr[mid]>target:#if the middle element is greater than the target element
        return binary_search(arr,left,mid-1,target) #recursive call to the left half of the array
    else:
        return binary_search(arr,mid+1,right,target) #recursive call to the right half of the array
    
arr = [2,3,4,6,10,10,20,30]
target = 10
print(binary_search(arr,0,len(arr)-1,target)) #0 is the index of the target element within the array print(binary_search(arr,0,len(arr)-1,target)) #0 is the index of the target element within the array 