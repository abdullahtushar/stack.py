def pushStack(stack, value):
    # Find the index to insert the new value
    index = len(stack)
    while index > 0 and stack[index - 1] > value:
        index = index - 1

    # Insert the new value at the determined index
    stack.insert(index, value)

# Example usage
stack = [95, 90, 45, 25, 10]

pushStack(stack, 50)  # Inserting value 50

print(stack) 