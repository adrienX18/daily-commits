/**
 * Array Helper Utilities
 * 
 * Collection of common array manipulation functions for JavaScript/Node.js
 * All functions include input validation and edge case handling
 */

/**
 * Remove duplicate values from an array
 * 
 * Uses Set data structure for efficient deduplication
 * Time Complexity: O(n) where n is the length of the input array
 * Space Complexity: O(n) for the Set storage
 * 
 * @param {Array} arr - Input array with potential duplicates
 * @returns {Array} - New array with unique values only
 * @note Returns empty array if input is null or undefined
 * 
 * @example
 * deduplicate([1, 2, 2, 3, 4, 4, 5])
 * // Returns: [1, 2, 3, 4, 5]
 * 
 * @example
 * deduplicate(['a', 'b', 'a', 'c'])
 * // Returns: ['a', 'b', 'c']
 */
function deduplicate(arr) {
  if (!arr || !Array.isArray(arr)) {
    return [];
  }
  return [...new Set(arr)];
}

/**
 * Flatten nested arrays to any depth
 * 
 * Recursively flattens arrays using Array.flat with Infinity depth
 * Time Complexity: O(n) where n is total number of elements including nested
 * Space Complexity: O(d) where d is the maximum nesting depth (call stack)
 * 
 * @param {Array} arr - Input array with potential nested arrays
 * @returns {Array} - Single-level flattened array
 * @note Returns empty array if input is null or undefined
 * 
 * @example
 * flatten([1, [2, [3, [4, 5]]]])
 * // Returns: [1, 2, 3, 4, 5]
 * 
 * @example
 * flatten([1, 2, [3, 4], [[5]], [[[6]]]])
 * // Returns: [1, 2, 3, 4, 5, 6]
 */
function flatten(arr) {
  if (!arr || !Array.isArray(arr)) {
    return [];
  }
  return arr.flat(Infinity);
}

module.exports = { deduplicate, flatten };
