"""
Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater than the average of all
previous elements. Skip the first element.
https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem
"""


def countResponseTimeRegressions(responseTimes):
    times = []
    count = 0
    for i, response in enumerate(responseTimes):
        if i == 0:
            times.append(response)
            continue
        avg = sum(times) / len(times)
        if response > avg:
            count += 1
        times.append(response)
    return count


if __name__ == '__main__':
    p6 = [100, 200, 150, 300]
    print(countResponseTimeRegressions(p6))
