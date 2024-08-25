#!/usr/bin/python3
""" UTF-8 Validation module"""


def validUTF8(data):
    """
    This function checks whether a given list of integers
    represents a valid UTF-8 encoding.

    Parameters:
    data (list): A list of integers representing
    the bytes of a UTF-8 encoded string.

    Returns:
    bool: True if the input data represents
    a valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit
    # (8th bit from the left) is set or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits
        byte = num & 255

        if n_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            mask = mask1
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1

            # 1-byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    # All characters must be complete
    return n_bytes == 0
