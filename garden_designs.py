def solve(N):
    """
    Calculates the number of unique garden layouts (structurally unique Binary Search Trees)
    for N species, which corresponds to the N-th Catalan number.

    Args:
        N: An integer representing the number of distinct tree species (1 <= N <= 15).

    Returns:
        The number of unique garden layouts possible.
    """
    # The number of unique BSTs with N nodes is the N-th Catalan number.
    # We can compute this using dynamic programming.

    if N < 0:
        return 0
    if N == 0:
        return 1

    # Create a DP array to store Catalan numbers
    catalan = [0] * (N + 1)

    # Base cases
    catalan[0] = 1
    catalan[1] = 1

    # Fill the array iteratively
    for i in range(2, N + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]

    return catalan[N]


# Example usage:
if __name__ == '__main__':
    # Example 1 from the problem description
    N1 = 2
    print(f"For N = {N1}, Unique Layouts: {solve(N1)}")  # Expected: 2

    # Example 2 from the problem description
    N2 = 3
    print(f"For N = {N2}, Unique Layouts: {solve(N2)}")  # Expected: 5

    # Another test case
    N3 = 4
    print(f"For N = {N3}, Unique Layouts: {solve(N3)}")  # Expected: 14

    # Test with the maximum constraint
    N4 = 15
    print(f"For N = {N4}, Unique Layouts: {solve(N4)}")  # Expected: 9694845
