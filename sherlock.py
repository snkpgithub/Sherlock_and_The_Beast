def decentNumber(n):
    # Try different combinations of 3's and 5's
    # Starting with maximum possible 5's (must be divisible by 3)
    for num_fives in range((n // 3) * 3, -1, -3):
        remaining = n - num_fives
        # Check if remaining digits can be filled with 3's (must be divisible by 5)
        if remaining >= 0 and remaining % 5 == 0:
            return "5" * num_fives + "3" * remaining
    return "-1"
