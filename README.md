# Daily Commits

Daily coding practice and experiments by Adrien Lemercier.

## Last Updated
**March 3, 2026** - Added new utility functions and test coverage

## Python Utilities

### String Helpers

Utility functions for string manipulation.

- `capitalize_words(text)` - Capitalize first letter of each word
- `reverse_string(text)` - Reverse a string

### Math Utils

Mathematical utility functions.

- `fibonacci(n)` - Calculate nth Fibonacci number
- `is_prime(n)` - Check if a number is prime

## Array Helpers

Utility functions for common array operations.

### Installation

```javascript
const { deduplicate, flatten } = require('./utils/array-helpers');
```

### Usage

#### deduplicate(arr)

Removes duplicate values from an array.

```javascript
const numbers = [1, 2, 2, 3, 4, 4, 5];
const unique = deduplicate(numbers);
console.log(unique); // [1, 2, 3, 4, 5]
```

#### flatten(arr)

Flattens nested arrays to any depth.

```javascript
const nested = [1, [2, [3, [4, 5]]]];
const flat = flatten(nested);
console.log(flat); // [1, 2, 3, 4, 5]
```

## License

MIT
