# Daily Commits 🚀

Daily coding practice repository - small, meaningful commits to stay consistent and build coding habits.

## Overview

This repository contains a collection of utility functions and helpers for common programming tasks. The goal is to maintain daily coding practice through small, focused commits that add real value.

## Project Structure

```
daily-commits/
├── utils/                  # Utility functions library
│   ├── list_helpers.py    # List operations (flatten, chunk, unique, binary_search)
│   ├── string_helpers.py  # String manipulation (case conversion, truncate)
│   ├── math_helpers.py    # Mathematical functions (gcd, lcm, fibonacci, statistics)
│   ├── date_helpers.py    # Date/time utilities
│   ├── file_helpers.py    # File operations
│   ├── validators.py      # Input validation functions
│   └── array-helpers.ts   # TypeScript array utilities
├── tests/                 # Unit tests
│   └── test_list_helpers.py
├── examples/              # Usage examples
└── requirements.txt       # Python dependencies
```

## Installation

### Python Dependencies

```bash
pip install -r requirements.txt
```

### Node/TypeScript Setup

```bash
npm install
```

## Usage Examples

### List Helpers

```python
from utils.list_helpers import flatten, chunk, unique, binary_search

# Flatten nested lists
nested = [[1, 2], [3, 4], [5]]
flat = flatten(nested)  # [1, 2, 3, 4, 5]

# Split into chunks
data = [1, 2, 3, 4, 5, 6]
chunks = chunk(data, 2)  # [[1, 2], [3, 4], [5, 6]]

# Remove duplicates while preserving order
values = [1, 2, 2, 3, 1, 4]
unique_values = unique(values)  # [1, 2, 3, 4]

# Binary search in sorted list
sorted_list = [1, 3, 5, 7, 9, 11]
index = binary_search(sorted_list, 7)  # 3
```

### String Helpers

```python
from utils.string_helpers import snake_to_camel, kebab_to_snake, truncate

# Case conversions
camel = snake_to_camel('hello_world')  # 'helloWorld'
snake = kebab_to_snake('hello-world')  # 'hello_world'

# Truncate long strings
long_text = "This is a very long string that needs truncation"
short = truncate(long_text, 20)  # 'This is a very lo...'
```

### Math Helpers

```python
from utils.math_helpers import gcd, lcm, is_prime, fibonacci, mean, median

# Number theory
print(gcd(12, 8))      # 4
print(lcm(12, 8))      # 24
print(is_prime(17))    # True

# Sequences
print(fibonacci(10))   # 55

# Statistics
data = [1, 2, 3, 4, 5]
print(mean(data))      # 3.0
print(median(data))    # 3.0
```

## Running Tests

```bash
# Run all tests with coverage
pytest --cov=utils tests/

# Run specific test file
pytest tests/test_list_helpers.py

# Run with verbose output
pytest -v
```

## Code Quality

This project maintains high code quality standards:

```bash
# Format code
black utils/ tests/

# Sort imports
isort utils/ tests/

# Lint code
flake8 utils/ tests/
pylint utils/ tests/

# Type checking
mypy utils/
```

## Contributing

This is a personal daily practice repository, but feel free to:
- Open issues for bugs or suggestions
- Submit PRs for improvements
- Use the utilities in your own projects

## Philosophy

This repository follows the principle of **consistent, incremental progress**:
- Small, focused commits
- Real, usable code (not just placeholder commits)
- Proper documentation and testing
- Clean, maintainable code style

## License

MIT License - Feel free to use this code however you'd like!

---

*Last updated: March 4, 2026*
