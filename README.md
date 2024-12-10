# Decent Number Generator

## Overview
This project implements a solution to the "Decent Number" problem, where Sherlock Holmes must find special numbers to save MI6's supercomputer from Professor Moriarty's virus. The challenge involves generating the largest possible number of a given length that satisfies specific properties.

## Problem Description

A Decent Number must have the following properties:
1. It can only contain digits 3 and/or 5
2. The number of 3's must be divisible by 5
3. The number of 5's must be divisible by 3
4. It must be the largest such number possible for its given length

For example:
- For length 11: 55555533333 is a decent number
- For length 3: 555 is a decent number
- For length 5: 33333 is a decent number
- For length 1: No decent number exists (-1)

## Solution Implementation

```python
def decentNumber(n):
    # Try different combinations of 3's and 5's
    # Starting with maximum possible 5's (must be divisible by 3)
    for num_fives in range((n // 3) * 3, -1, -3):
        remaining = n - num_fives
        # Check if remaining digits can be filled with 3's (must be divisible by 5)
        if remaining >= 0 and remaining % 5 == 0:
            return "5" * num_fives + "3" * remaining
    return "-1"
```

### Algorithm Explanation
1. Start with the maximum possible number of 5's (must be divisible by 3)
2. Gradually reduce the number of 5's until a valid solution is found
3. The remaining digits must be fillable with 3's (must be divisible by 5)
4. Return -1 if no valid solution exists

### Time & Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

## Usage

1. Clone the repository:
```bash
git clone https://github.com/yourusername/decent-number-generator.git
cd decent-number-generator
```

2. Run the script with your test cases:
```python
# Example usage
print(decentNumber(11))  # Outputs: 55555533333
print(decentNumber(3))   # Outputs: 555
print(decentNumber(5))   # Outputs: 33333
print(decentNumber(1))   # Outputs: -1
```

## Test Cases

```python
def test_decent_number():
    assert decentNumber(1) == "-1"
    assert decentNumber(3) == "555"
    assert decentNumber(5) == "33333"
    assert decentNumber(11) == "55555533333"
    print("All test cases passed!")
```

## Input Constraints
- 1 ≤ n ≤ 100000
- Input will be an integer representing the desired length of the decent number

## Project Structure
```
decent-number-generator/
├── README.md
├── decent_number.py
├── test_decent_number.py
└── requirements.txt
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Original problem from HackerRank
- Inspired by the Sherlock Holmes series
