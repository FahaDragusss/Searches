def reccursive_binary_search_index(A,low,high,key):
    if low > high:
        return None
    mid = (low+high)//2
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return reccursive_binary_search_index(A,low,mid-1,key)
    else:
        return reccursive_binary_search_index(A,mid+1,high,key)
        