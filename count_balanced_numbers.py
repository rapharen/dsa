def countBalancedNumbers(p):
    n = len(p)
    pos = [0] * (n + 1)

    for i in range(n):
        pos[p[i]] = i

    result = []
    min_pos = pos[1]
    max_pos = pos[1]

    for k in range(1, n + 1):
        if k > 1:
            # Actualizar min y max incrementalmente
            min_pos = min(min_pos, pos[k])
            max_pos = max(max_pos, pos[k])

        if max_pos - min_pos + 1 == k:
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)


# Example usage:
if __name__ == '__main__':
    p6 = [5, 3, 1, 2, 4]
    assert countBalancedNumbers(p6) == "11111", f"Expected 11111, got {countBalancedNumbers(p6)}"
    print(f"✓ p = {p6}, balanced: {countBalancedNumbers(p6)}")

    p7 = [1, 4, 2, 3]
    assert countBalancedNumbers(p7) == "1001", f"Expected 1001, got {countBalancedNumbers(p7)}"
    print(f"✓ p = {p7}, balanced: {countBalancedNumbers(p7)}")

    p8 = [7, 3, 2, 4, 5, 1, 6]
    assert countBalancedNumbers(p8) == "1000111", f"Expected 1000111, got {countBalancedNumbers(p8)}"
    print(f"✓ p = {p8}, balanced: {countBalancedNumbers(p8)}")

    print("\n✅ All tests passed!")