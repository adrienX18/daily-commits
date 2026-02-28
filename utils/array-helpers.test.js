const { deduplicate, flatten } = require('./array-helpers');

describe('Array Helpers', () => {
  describe('deduplicate', () => {
    test('removes duplicate numbers', () => {
      expect(deduplicate([1, 2, 2, 3, 4, 4, 5])).toEqual([1, 2, 3, 4, 5]);
    });

    test('removes duplicate strings', () => {
      expect(deduplicate(['a', 'b', 'b', 'c'])).toEqual(['a', 'b', 'c']);
    });

    test('handles null input', () => {
      expect(deduplicate(null)).toEqual([]);
    });

    test('handles undefined input', () => {
      expect(deduplicate(undefined)).toEqual([]);
    });

    test('returns empty array for non-array input', () => {
      expect(deduplicate('not an array')).toEqual([]);
    });
  });

  describe('flatten', () => {
    test('flattens nested arrays', () => {
      expect(flatten([1, [2, [3, [4, 5]]]])).toEqual([1, 2, 3, 4, 5]);
    });

    test('handles already flat arrays', () => {
      expect(flatten([1, 2, 3, 4, 5])).toEqual([1, 2, 3, 4, 5]);
    });

    test('handles null input', () => {
      expect(flatten(null)).toEqual([]);
    });
  });
});
