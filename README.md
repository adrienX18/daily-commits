# Daily Commits 📅

Daily coding practice - small commits to stay consistent.

## Project Structure

```
daily-commits/
├── utils/
│   ├── string_helpers.py    # String manipulation utilities
│   └── math_helpers.py       # Mathematical functions
└── README.md
```

## Utilities

### String Helpers
- `capitalize_words()` - Capitalize first letter of each word
- `remove_extra_spaces()` - Clean up whitespace
- `truncate()` - Truncate strings with suffix
- `reverse_words()` - Reverse word order in a string

### Math Helpers
- `fibonacci()` - Calculate Fibonacci numbers
- `is_prime()` - Prime number checker
- `gcd()` - Greatest common divisor
- `lcm()` - Least common multiple

## Usage

```python
from utils.string_helpers import capitalize_words, truncate, reverse_words
from utils.math_helpers import fibonacci, is_prime, lcm

# String operations
text = capitalize_words("hello world")
short = truncate("Long text here", 10)
reversed_text = reverse_words("hello world")  # "world hello"

# Math operations
fib_10 = fibonacci(10)
is_17_prime = is_prime(17)
result = lcm(12, 18)  # 36
```

## Goal

Commit something every day to build consistency and improve coding skills! 🚀
