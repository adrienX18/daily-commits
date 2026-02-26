# Daily Commits 📅

Daily coding practice - small commits to stay consistent.

## Project Structure

```
daily-commits/
├── utils/
│   ├── string_helpers.py    # String manipulation utilities
│   ├── math_helpers.py       # Mathematical functions
│   ├── list_helpers.py       # List operations
│   └── file_helpers.py       # File system utilities
├── tests/
│   ├── test_string_helpers.py
│   └── test_math_helpers.py
└── README.md
```

## Utilities

### String Helpers
- `capitalize_words()` - Capitalize first letter of each word
- `remove_extra_spaces()` - Clean up whitespace
- `truncate()` - Truncate strings with suffix
- `reverse_words()` - Reverse word order in a string
- `is_palindrome()` - Check if a string is a palindrome (case-insensitive option)
- `is_valid_email()` - Basic email format validation

### Math Helpers
- `fibonacci()` - Calculate Fibonacci numbers
- `is_prime()` - Prime number checker
- `gcd()` - Greatest common divisor
- `lcm()` - Least common multiple
- `mean()` - Calculate arithmetic mean of a list
- `median()` - Calculate median value of a list
- `standard_deviation()` - Calculate standard deviation (sample or population)

### File Helpers
- `get_file_extension()` - Extract file extension from filename
- `get_file_size_mb()` - Get file size in megabytes
- `list_files_by_extension()` - List files by extension in directory
- `create_directory_if_not_exists()` - Safely create directories

## Usage

```python
from utils.string_helpers import capitalize_words, truncate, reverse_words, is_palindrome, is_valid_email
from utils.math_helpers import fibonacci, is_prime, lcm, mean, median, standard_deviation
from utils.file_helpers import get_file_extension, get_file_size_mb

# String operations
text = capitalize_words("hello world")
short = truncate("Long text here", 10)
reversed_text = reverse_words("hello world")  # "world hello"
is_palindrome("racecar")  # True
is_valid_email("user@example.com")  # True

# Math operations
fib_10 = fibonacci(10)
is_17_prime = is_prime(17)
result = lcm(12, 18)  # 36

# Statistical functions
average = mean([1, 2, 3, 4, 5])  # 3.0
middle = median([1, 2, 3, 4, 5])  # 3.0
std_dev = standard_deviation([1, 2, 3, 4, 5])  # 1.58

# File operations
ext = get_file_extension("document.pdf")  # "pdf"
size = get_file_size_mb("/path/to/file")  # Size in MB
```

## Testing

Run tests using:
```bash
python -m pytest tests/
```

Or run individual test files:
```bash
python tests/test_string_helpers.py
python tests/test_math_helpers.py
```

## Goal

Commit something every day to build consistency and improve coding skills! 🚀

## Daily Progress

Track your commits and watch your consistency grow over time!
