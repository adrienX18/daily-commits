"""Demonstration of string utility functions."""

from utils.string_helpers import capitalize_words, reverse_string, count_vowels


def main():
    """Run string utility demonstrations."""
    print("=== String Utilities Demo ===\n")
    
    # Capitalize words
    print("1. Capitalize Words")
    test_strings = [
        "hello world",
        "python programming is fun",
        "daily coding practice"
    ]
    for text in test_strings:
        result = capitalize_words(text)
        print(f"   '{text}' -> '{result}'")
    
    print("\n2. Reverse String")
    reverse_tests = ["hello", "python", "12345", "racecar"]
    for text in reverse_tests:
        result = reverse_string(text)
        is_palindrome = text == result
        status = "(palindrome!)" if is_palindrome else ""
        print(f"   '{text}' -> '{result}' {status}")
    
    print("\n3. Count Vowels")
    vowel_tests = [
        "hello world",
        "programming",
        "AEIOU",
        "xyz"
    ]
    for text in vowel_tests:
        count = count_vowels(text)
        print(f"   '{text}' has {count} vowels")


if __name__ == "__main__":
    main()
