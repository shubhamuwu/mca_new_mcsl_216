# Recursive binary search function
def binary_search_recursive(arr, low, high, target, steps=[]):
    # Base case: If the array has no more elements to search
    if high < low:
        steps.append(f"Element {target} not found")
        return -1, steps
    
    # Calculate the middle index
    mid = (low + high) // 2
    steps.append(f"Checking middle index {mid}, value {arr[mid]}")

    # If the middle element is the target
    if arr[mid] == target:
        steps.append(f"Element {target} found at index {mid}")
        return mid, steps
    
    # If target is greater than the middle element, search the right half
    elif arr[mid] < target:
        steps.append(f"Element {target} is greater than {arr[mid]}, searching right half")
        return binary_search_recursive(arr, mid + 1, high, target, steps)
    
    # If target is smaller, search the left half
    else:
        steps.append(f"Element {target} is less than {arr[mid]}, searching left half")
        return binary_search_recursive(arr, low, mid - 1, target, steps)

# Array and target
arr = [10, 35, 40, 45, 50, 55, 60, 65, 70, 100]
target = 100

# Initial recursive call
index_found, steps_trace = binary_search_recursive(arr, 0, len(arr) - 1, target)

index_found, steps_trace