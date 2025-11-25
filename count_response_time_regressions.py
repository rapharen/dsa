"""
Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater than the average of all
previous elements. Skip the first element.
https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem
"""


def countResponseTimeRegressions(responseTimes):
    # v1: O(n^2)
    # v2: O(n)
    if not responseTimes:
        return 0
    count = 0
    current_sum = responseTimes[0] # first element
    for i in range(1, len(responseTimes)):
        avg = current_sum / i
        if responseTimes[i] > avg:
            count += 1
        current_sum += responseTimes[i]
    return count


if __name__ == '__main__':
    p6 = [100, 200, 150, 300]
    print(countResponseTimeRegressions(p6))
