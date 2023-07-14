def pushStack(stack, value):
    index = 0

    # Find the correct index to insert the new value
    while index < len(stack) and stack[index] < value:
        index += 1

    # Insert the new value at the determined index
    stack.insert(index, value)


def main():
    stack = [95, 90, 45, 25, 10]

    pushStack(stack, 50)  # Inserting value 50

    print(stack)  # Output: [95, 90, 50, 45, 25, 10]


if __name__ == "__main__":
    main()
