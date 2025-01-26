
def heapify(arr, N, i):
    largest = i # initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2
    
    # find the largest child node
    # There are many ways to do this. 
    # Method 1
    # # See if left child of root exists and is
    # # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l
 
    # # See if right child of root exists and is
    # # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, N, largest) # recursively move largest to next level 
     
    # two propertties
    # 1. number of leaf nodes = N//2, thenfore only heapify the leaf node, from N//2-1
    # 2.which leads to time complexity O(n) in this for-loop + heapify process.

def heapSort(arr):
    N = len(arr)
    
    #build a maxheap    
    for i in range(N//2-1, -1, -1):
        heapify(arr, N, i)

    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        # move the max heap first to the end (largest)
        heapify(arr, i, 0)

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
    heapSort(arr)
    print("\nSorted array is ")
    printList(arr)
    
# https://www.geeksforgeeks.org/python-program-for-heap-sort/   
# https://www.geeksforgeeks.org/heap-sort/