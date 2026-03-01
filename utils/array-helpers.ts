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

/**
 * Generate a range of numbers
 * @param start - Starting number (or stop if only one argument)
 * @param stop - Ending number (exclusive)
 * @param step - Step increment (default: 1)
 * @returns Array of numbers in the specified range
 * 
 * @example
 * range(5)              // [0, 1, 2, 3, 4]
 * range(2, 6)           // [2, 3, 4, 5]
 * range(0, 10, 2)       // [0, 2, 4, 6, 8]
 * range(5, 0, -1)       // [5, 4, 3, 2, 1]
 */
export function range(start: number, stop?: number, step: number = 1): number[] {
  if (step === 0) {
    return [];
  }
  
  // If only one argument, treat it as stop with start=0
  let actualStart = stop === undefined ? 0 : start;
  let actualStop = stop === undefined ? start : stop;
  
  const result: number[] = [];
  
  if (step > 0) {
    for (let i = actualStart; i < actualStop; i += step) {
      result.push(i);
    }
  } else {
    for (let i = actualStart; i > actualStop; i += step) {
      result.push(i);
    }
  }
  
  return result;
}
