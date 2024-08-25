# 0x04-utf8_validation

Let's break down how this function works:

1. We iterate through each integer in the `data` list, considering only the 8 least significant bits (using `& 255`).

2. For each byte, we check if it's the start of a new UTF-8 character or a continuation byte:
   - If it's a new character (`n_bytes == 0`), we determine how many bytes it should have by counting the number of leading 1s.
   - If it's a continuation byte, we check if it starts with '10' in binary.

3. We keep track of how many bytes we expect in the current character with `n_bytes`.

4. We return `False` if we encounter any invalid scenarios:
   - A 1-byte character that starts with a 1 in the most significant bit.
   - A character that would require more than 4 bytes.
   - A continuation byte that doesn't start with '10' in binary.

5. If we've processed all bytes and all characters are complete (`n_bytes == 0`), we return `True`.

This implementation handles the requirements you specified:

- It works with a list of integers where each integer represents 1 byte.
- It only considers the 8 least significant bits of each integer.
- It correctly handles UTF-8 characters that can be 1 to 4 bytes long.
- It can process multiple characters in the data set.

The function will return `True` for valid UTF-8 encodings and `False` otherwise, matching the behavior in your example output.

Another implementation for comparsion:
 `https://medium.com/@simbarashemutombe1/determining-if-a-given-data-set-represents-a-valid-utf-8-encoding-b65c792a56f4`
