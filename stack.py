# Define the Stack class to implement stack operations
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Check if the word is a palindrome
def is_palindrome(word):
    stack = Stack()
    for char in word:
        stack.push(char)

    reversed_word = ""
    while not stack.is_empty():
        reversed_word += stack.pop()

    return word == reversed_word

# Main function to read input and print the result
def main():
    word = input().strip()  # Read the word from input and remove leading/trailing whitespaces
    if is_palindrome(word):  # Check if the word is a palindrome
        print("Yes")
    else:
        print("No")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
