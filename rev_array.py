# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array

def reverse_array_in_place(arr):
    """Reverses an array in place."""
    start_index = 0
    end_index = len(arr) - 1

    while end_index > start_index:
        # Swap the elements at the start and end indices
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]

        # Move the start and end indices towards the center
        start_index += 1
        end_index -= 1


        
        
my_array = [1, 2, 3, 4, 5]
reverse_array_in_place(my_array)
print(my_array)  # Output: [5, 4, 3, 2, 1]
     