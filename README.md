# Daily Commits 📅

Daily coding practice - small commits to stay consistent.

## Project Structure

```
daily-commits/
├── utils/
│   ├── string_helpers.py    # String manipulation utilities
│   ├── math_helpers.py       # Mathematical functions
│   └── list_helpers.py       # List operations
└── README.md
```

## Utilities

### String Helpers
- `capitalize_words()` - Capitalize first letter of each word
- `remove_extra_spaces()` - Clean up whitespace
- `truncate()` - Truncate strings with suffix
- `reverse_words()` - Reverse word order in a string
- `is_palindrome()` - Check if a string is a palindrome (case-insensitive option)

### Math Helpers
- `fibonacci()` - Calculate Fibonacci numbers
- `is_prime()` - Prime number checker
- `gcd()` - Greatest common divisor
- `lcm()` - Least common multiple
- `mean()` - Calculate arithmetic mean of a list
- `median()` - Calculate median value of a list

## Usage

```python
from utils.string_helpers import capitalize_words, truncate, reverse_words, is_palindrome
from utils.math_helpers import fibonacci, is_prime, lcm, mean, median

# String operations
text = capitalize_words("hello world")
short = truncate("Long text here", 10)
reversed_text = reverse_words("hello world")  # "world hello"
is_palindrome("racecar")  # True

# Math operations
fib_10 = fibonacci(10)
is_17_prime = is_prime(17)
result = lcm(12, 18)  # 36

# Statistical functions
average = mean([1, 2, 3, 4, 5])  # 3.0
middle = median([1, 2, 3, 4, 5])  # 3.0
```

## Goal

Commit something every day to build consistency and improve coding skills! 🚀
