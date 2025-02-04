def recursive_bubble_sort(A,n=None):
    if n is None:
        n = len(A)
    
    elif n == 1:
        return
    
    for j in range(n-1):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]        
    
    recursive_bubble_sort(A, n-1)
    

