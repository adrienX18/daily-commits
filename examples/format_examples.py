"""
Format Helpers Examples
Demonstrates usage of format_helpers utility functions
"""

import sys
import os
# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.format_helpers import format_currency, format_percentage, truncate_text


def demo_currency_formatting():
    """Demonstrate currency formatting with various inputs"""
    print("=== Currency Formatting Examples ===")
    
    # Basic usage
    print(f"Basic: {format_currency(1234.56)}")  # $1,234.56
    
    # Large numbers
    print(f"Large: {format_currency(1234567.89)}")  # $1,234,567.89
    
    # Different currencies
    print(f"Euro: {format_currency(999.99, currency_symbol='€')}")  # €999.99
    print(f"Pound: {format_currency(500.50, currency_symbol='£')}")  # £500.50
    
    # Different decimal places
    print(f"No decimals: {format_currency(1234, decimal_places=0)}")  # $1,234
    print(f"Three decimals: {format_currency(1234.5678, decimal_places=3)}")  # $1,234.568
    
    print()


def demo_percentage_formatting():
    """Demonstrate percentage formatting"""
    print("=== Percentage Formatting Examples ===")
    
    # Basic usage
    print(f"Basic: {format_percentage(0.75)}")  # 75.0%
    
    # High precision
    print(f"Precise: {format_percentage(0.7523, decimal_places=2)}")  # 75.23%
    
    # Low percentages
    print(f"Small: {format_percentage(0.025)}")  # 2.5%
    
    # Over 100%
    print(f"Over 100: {format_percentage(1.5)}")  # 150.0%
    
    print()


def demo_text_truncation():
    """Demonstrate text truncation"""
    print("=== Text Truncation Examples ===")
    
    long_text = "This is a very long text that definitely needs to be truncated for display"
    
    # Basic truncation
    print(f"Default: {truncate_text(long_text)}")
    
    # Custom length
    print(f"Short (20): {truncate_text(long_text, max_length=20)}")
    
    # Custom suffix
    print(f"Custom suffix: {truncate_text(long_text, max_length=30, suffix=' [more]')}")
    
    # Text shorter than max_length (no truncation)
    short_text = "Short text"
    print(f"No truncation needed: {truncate_text(short_text)}")
    
    print()


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Format Helpers - Usage Examples")
    print("="*50 + "\n")
    
    demo_currency_formatting()
    demo_percentage_formatting()
    demo_text_truncation()
    
    print("="*50)
    print("All examples completed successfully!")
    print("="*50)
