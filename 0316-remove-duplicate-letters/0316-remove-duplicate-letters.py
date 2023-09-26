class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def removeDuplicateLetters(s):
            # Initialize a stack to keep track of characters in the result
            stack = []

            # Initialize a set to keep track of characters in the stack
            seen = set()

            # Initialize a dictionary to count the frequency of each character
            char_count = {}

            # Count the frequency of each character in the string
            for char in s:
                char_count[char] = char_count.get(char, 0) + 1

            # Iterate through the characters in the string
            for char in s:
                # Decrement the frequency of the character in the dictionary
                char_count[char] -= 1

                # If the character is already in the stack, skip it
                if char in seen:
                    continue

                # While there are characters remaining in the stack,
                # and the current character is smaller than the character
                # at the top of the stack, and the character at the top
                # of the stack will appear later in the string, pop it
                while stack and char < stack[-1] and char_count[stack[-1]] > 0:
                    seen.remove(stack.pop())

                # Add the current character to the stack and mark it as seen
                stack.append(char)
                seen.add(char)

            # Convert the stack to a string and return the result
            return ''.join(stack)

        result = removeDuplicateLetters(s)
        print(result)  # Output: "abc"
        return result
