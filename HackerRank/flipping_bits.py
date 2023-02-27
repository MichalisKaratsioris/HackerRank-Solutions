"""
Given a list of 32-bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1 )
and return the result as an unsigned integer.
"""
import math


def flipping_bits(n: int) -> int:
    """
    This function takes as an input a long-integer n as a string and returns a long-integer, as a string,
    which is the result of flipping the bits of n.
    * An int is a 32-bit integer; a long is a 64-bit integer.

    Example:
        (1) n = 9 = 1001 => 00000000000000000000000000001001 => 11111111111111111111111111110110 => 4294967286
            flipping_bits(n) => 4294967286

    Note:   Another way would be to just subtract from (2 * max_int). This would give O(1) time and space complexity.
            (2 * max_int) = 4,294,967,295, thus if we subtract for example 9, the result is 4,294,967,286.
    """

    b_n = []
    b_result = []
    for i in range(32-n.bit_length()):
        b_n.append(0)
    bits = bin(n)[-n.bit_length():]
    for i in range(len(bits)):
        b_n.append(int(bits[i]))
    for bit in b_n:
        if bit == 0:
            b_result.append(1)
        if bit == 1:
            b_result.append(0)
    number = 0
    for i in range(len(b_result)):
        number = number + b_result[i] * math.pow(2, 31 - i)
    return int(number)


# ----------------- TESTS -----------------

print(flipping_bits(9))
# Expected Output: 4294967286

print(flipping_bits(10))
# Expected Output: 4294967285

print(flipping_bits(11))
# Expected Output: 4294967284

print(flipping_bits(100))
# Expected Output: 4294967195
