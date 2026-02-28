/**
 * Remove duplicate values from an array
 * @param arr - Input array
 * @returns Array with unique values
 * @note Returns empty array if input is null or undefined
 * @note Uses Map for O(n) performance on large arrays
 */
export function deduplicate<T>(arr: T[] | null | undefined): T[] {
  if (!arr || !Array.isArray(arr)) {
    return [];
  }
  
  // For primitive types, Set is optimal
  if (arr.length === 0 || typeof arr[0] !== 'object') {
    return [...new Set(arr)];
  }
  
  // For objects, use Map with JSON serialization for deep comparison
  const seen = new Map<string, T>();
  const result: T[] = [];
  
  for (const item of arr) {
    const key = JSON.stringify(item);
    if (!seen.has(key)) {
      seen.set(key, item);
      result.push(item);
    }
  }
  
  return result;
}

/**
 * Flatten nested arrays to any depth
 * @param arr - Input array (potentially nested)
 * @returns Flattened array
 */
export function flatten<T>(arr: any[] | null | undefined): T[] {
  if (!arr || !Array.isArray(arr)) {
    return [];
  }
  return arr.flat(Infinity) as T[];
}

/**
 * Chunk an array into smaller arrays of specified size
 * @param arr - Input array
 * @param size - Size of each chunk
 * @returns Array of chunks
 */
export function chunk<T>(arr: T[], size: number): T[][] {
  if (!arr || !Array.isArray(arr) || size <= 0) {
    return [];
  }
  const result: T[][] = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}
