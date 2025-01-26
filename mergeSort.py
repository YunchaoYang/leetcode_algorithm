# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def merge(arr, Left, Right):   
    i = j = k = 0
    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1

    while i < len(Left):
        arr[k] = Left[i]
        i += 1
        k += 1
    while j < len(Right):
        arr[k] = Right[j]
        j += 1
        k += 1
        
def mergeSort(arr):
    if len(arr) <= 1: return # The final sub problem solution.

    # divide into 2 subproblem
    mid = len(arr) // 2
    Left = arr[:mid]
    Right = arr[mid:]

    mergeSort(Left)
    mergeSort(Right)
    
    # sub problem are solved.
    merge(arr, Left, Right)

# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printList(arr)
    mergeSort(arr)
    print("\nSorted array is ")
    printList(arr)