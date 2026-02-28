/**
 * Remove duplicate values from an array
 * @param {Array} arr - Input array
 * @returns {Array} - Array with unique values
 */
function deduplicate(arr) {
  return [...new Set(arr)];
}

/**
 * Flatten nested arrays
 * @param {Array} arr - Input array
 * @returns {Array} - Flattened array
 */
function flatten(arr) {
  return arr.flat(Infinity);
}

module.exports = { deduplicate, flatten };
