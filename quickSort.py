def partition(arr, low, high):
    pivot = high
    
    idx_sorted_low = low - 1
    
    for j in range(low, high):
        if arr[j] < arr[pivot]:
            idx_sorted_low += 1
            arr[idx_sorted_low], arr[j] = arr[j], arr[idx_sorted_low]

    idx_sorted_low += 1
    
    arr[idx_sorted_low], arr[pivot] = arr[pivot], arr[idx_sorted_low]

    return idx_sorted_low
    
 
def quickSort(arr, low, high):
    if low >= high: return # the final subproblem 
    
    pivot_position = partition(arr, low, high) 
    quickSort(arr, low, pivot_position-1)
    quickSort(arr, pivot_position + 1, high)

 
# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printList(arr)
    quickSort(arr, 0, len(arr)-1)
    print("\nSorted array is ")
    printList(arr)