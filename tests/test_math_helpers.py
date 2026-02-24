"""
Unit tests for math helper functions
"""
import sys
sys.path.insert(0, '..')

from utils.math_helpers import fibonacci, is_prime, gcd, lcm


def test_fibonacci():
    """Test Fibonacci function."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    print("✓ Fibonacci tests passed")


def test_is_prime():
    """Test prime number checker."""
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
    print("✓ Prime checker tests passed")


def test_gcd():
    """Test greatest common divisor."""
    assert gcd(48, 18) == 6
    assert gcd(7, 5) == 1
    assert gcd(100, 50) == 50
    print("✓ GCD tests passed")


def test_lcm():
    """Test least common multiple."""
    assert lcm(12, 18) == 36
    assert lcm(7, 5) == 35
    assert lcm(0, 5) == 0
    print("✓ LCM tests passed")


if __name__ == '__main__':
    test_fibonacci()
    test_is_prime()
    test_gcd()
    test_lcm()
    print("\n✅ All tests passed!")
