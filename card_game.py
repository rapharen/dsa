# Memoization cache
memo = {}


def maxCardCount(n, card):
    """
    Main function to start the recursive process with memoization.
    """
    memo.clear()
    return dp(0, n, card, 0)


def dp(i, n, card, current_power):
    """
    Recursive solver with memoization.
    i: current card index
    n: total number of cards
    card: the list of cards
    current_power: current power level
    """
    # Base case: If we have considered all cards, we can't pick any more.
    if i == n:
        return 0

    # If this state is already computed, return the stored result.
    if (i, current_power) in memo:
        return memo[(i, current_power)]

    # --- Decision 1: Don't pick the current card ---
    res_dont_pick = dp(i + 1, n, card, current_power)

    # --- Decision 2: Pick the current card (if possible) ---
    res_pick = -1  # Initialize with a value indicating this choice is not possible
    new_power = current_power + card[i]
    if new_power >= 0:
        res_pick = 1 + dp(i + 1, n, card, new_power)

    # The result for the current state is the maximum of the two decisions.
    result = max(res_pick, res_dont_pick)

    # Store the result in the cache before returning.
    memo[(i, current_power)] = result
    return result


# --- Test Cases ---
if __name__ == '__main__':
    # Test Case 1 (based on the explanation in the problem)
    n1 = 6
    card1 = [4, -41, 1, -3, 1, -3]
    assert maxCardCount(n1, card1) == 5, f"Test Case 1 Failed: Expected 5, got {maxCardCount(n1, card1)}"
    print("Test Case 1 Passed!")

    # Test Case 2
    n2 = 5
    card2 = [4, -4, -1, -2, 9]
    assert maxCardCount(n2, card2) == 4, f"Test Case 2 Failed: Expected 4, got {maxCardCount(n2, card2)}"
    print("Test Case 2 Passed!")

    print("\nAll tests passed successfully!")
