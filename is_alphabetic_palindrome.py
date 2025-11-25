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
    new_code = []
    for c in code:
        if c.isalpha():
            new_code.append(c.lower())
    return new_code == new_code[::-1]


if __name__ == '__main__':
    print(isAlphabeticPalindrome("A1b2B!a"))
