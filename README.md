# Daily Commits

Daily coding practice and experiments by Adrien Lemercier.

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
