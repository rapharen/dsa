"""
Check Palindrome by Filtering Non-Letters
Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

Example

Input

code = A1b2B!a
Output

1
Explanation

- Step 1: Extract only letters → ['A','b','B','a']
- Step 2: Convert to lowercase → ['a','b','b','a']
- Step 3: Compare sequences forward and backward: 'abba' == 'abba' → true
"""


def isAlphabeticPalindrome(code):
    # v1: O(n), O(n)
    # v2:
    # new_code = []
    # for c in code:
    #     if c.isalpha():
    #         new_code.append(c.lower())
    # return new_code == new_code[::-1]

    left, right = 0, len(code) - 1
    while left < right:
        if not code[left].isalpha():
            left += 1
            continue
        if not code[right].isalpha():
            right -= 1
            continue
        if code[left].lower() != code[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    print(isAlphabeticPalindrome("A1b2B!a"))
