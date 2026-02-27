# Daily Commits 📅

Daily coding practice - small commits to stay consistent.

## Project Structure

```
daily-commits/
├── utils/
│   ├── string_helpers.py    # String manipulation utilities
│   ├── math_helpers.py       # Mathematical functions
│   ├── list_helpers.py       # List operations
│   ├── date_helpers.py       # Date and time utilities
│   └── file_helpers.py       # File system utilities
├── tests/
│   ├── test_string_helpers.py
│   ├── test_math_helpers.py
│   └── test_list_helpers.py
└── README.md
```

## Utilities

### String Helpers
- `capitalize_words()` - Capitalize first letter of each word
- `remove_extra_spaces()` - Clean up whitespace
- `truncate()` - Truncate strings with suffix
- `reverse_words()` - Reverse word order in a string
- `is_palindrome()` - Check if a string is a palindrome (case-insensitive option)
- `is_valid_email()` - Email format validation using regex

### Math Helpers
- `fibonacci()` - Calculate Fibonacci numbers
- `is_prime()` - Prime number checker
- `gcd()` - Greatest common divisor
- `lcm()` - Least common multiple
- `factorial()` - Calculate factorial of a number
- `mean()` - Calculate arithmetic mean of a list
- `median()` - Calculate median value of a list
- `standard_deviation()` - Calculate standard deviation (sample or population)

### List Helpers
- `chunk_list()` - Split list into chunks of specified size
- `flatten()` - Flatten nested list structures
- `remove_duplicates()` - Remove duplicates while preserving order
- `find_common_elements()` - Find common elements between two lists
- `rotate_list()` - Rotate list elements left or right
- `filter_by_condition()` - Filter list by custom condition function
- `group_by()` - Group list elements by key function

### File Helpers
- `get_file_extension()` - Extract file extension from filename
- `get_file_size_mb()` - Get file size in megabytes
- `list_files_by_extension()` - List files by extension in directory
- `create_directory_if_not_exists()` - Safely create directories

## Usage

```python
from utils.string_helpers import capitalize_words, truncate, reverse_words, is_palindrome, is_valid_email
from utils.math_helpers import fibonacci, is_prime, lcm, factorial, mean, median, standard_deviation
from utils.list_helpers import chunk_list, flatten, remove_duplicates, find_common_elements
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
fact_5 = factorial(5)  # 120

# Statistical functions
average = mean([1, 2, 3, 4, 5])  # 3.0
middle = median([1, 2, 3, 4, 5])  # 3.0
std_dev = standard_deviation([1, 2, 3, 4, 5])  # 1.58

# List operations
chunks = chunk_list([1, 2, 3, 4, 5, 6], 2)  # [[1, 2], [3, 4], [5, 6]]
flat = flatten([[1, 2], [3, 4]])  # [1, 2, 3, 4]
unique = remove_duplicates([1, 2, 2, 3, 1])  # [1, 2, 3]
common = find_common_elements([1, 2, 3], [2, 3, 4])  # [2, 3]

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
python tests/test_list_helpers.py
```

## Goal

Commit something every day to build consistency and improve coding skills! 🚀

## Development Tips

- Write clean, readable code
- Add docstrings to all functions
- Include type hints for better IDE support
- Write tests for new features
- Keep commits small and focused
- Use meaningful commit messages

## Daily Progress

Track your commits and watch your consistency grow over time!
