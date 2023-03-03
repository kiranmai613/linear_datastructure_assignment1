def find_smallest(stack):
    if not stack:
        return None

    # Initialize the smallest number as the first element of the stack
    smallest = stack[-1]

    # Iterate over the stack to find the smallest number
    for item in stack:
        if item < smallest:
            smallest = item

    return smallest
stack = [5, 2, 8, 1, 6]
smallest = find_smallest(stack)
print("Smallest number in the stack:", smallest)
