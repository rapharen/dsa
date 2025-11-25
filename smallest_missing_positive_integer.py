"""
Find the Smallest Missing Positive Integer
Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.
https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/find-smallest-missing-positive-integer/problem
"""


def findSmallestMissingPositive(orderNumbers):
    # O(n), O(1)
    n = len(orderNumbers)
    i = 0
    # cyclic sort
    while i < n:
        val = orderNumbers[i]
        correct_idx = val - 1
        if 0 < val <= n and orderNumbers[i] != orderNumbers[correct_idx]:
            orderNumbers[i], orderNumbers[correct_idx] = orderNumbers[correct_idx], orderNumbers[i]
        else:
            i += 1
    # scan
    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1
    return n + 1


if __name__ == '__main__':
    print(findSmallestMissingPositive([3, 4, -1, 1]))
