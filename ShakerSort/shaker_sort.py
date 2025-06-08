def shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        # Reset the swapped flag for the forward pass
        swapped = False
        
        # Forward pass (left to right)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
            
        # Move the end point back as the last element is now in place
        end = end - 1
        
        # Reset the swapped flag for the backward pass
        swapped = False
        
        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        # Move the start point forward as the first element is now in place
        start = start + 1
    
    return arr
