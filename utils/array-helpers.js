/**
 * Remove duplicate values from an array
 * @param {Array} arr - Input array
 * @returns {Array} - Array with unique values
 * @note Returns empty array if input is null or undefined
 */
function deduplicate(arr) {
  if (!arr || !Array.isArray(arr)) {
    return [];
  }
  return [...new Set(arr)];
}

/**
 * Flatten nested arrays
 * @param {Array} arr - Input array
 * @returns {Array} - Flattened array
 */
function flatten(arr) {
  if (!arr || !Array.isArray(arr)) {
    return [];
  }
  return arr.flat(Infinity);
}

module.exports = { deduplicate, flatten };
