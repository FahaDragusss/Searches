def binary_search_index(A,key):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = (low+high)//2
        if key == A[mid]:
            return mid
        elif key > A[mid]:
            low = mid+1
        else:
            high = mid-1
    return None