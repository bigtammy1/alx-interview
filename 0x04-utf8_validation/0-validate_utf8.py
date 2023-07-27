#!/usr/bin/python3

def validUTF8(data):
    num_bytes_to_follow = 0

    for byte in data:
        # Check if the most significant bit (MSB) is set
        if byte & 0x80:
            if num_bytes_to_follow == 0:
                # Determine the number of bytes to follow based on the MSB
                mask = 0x80
                while byte & mask:
                    num_bytes_to_follow += 1
                    mask >>= 1

                # The first byte of a character must have a valid number of bytes to follow (1 to 4)
                if num_bytes_to_follow < 1 or num_bytes_to_follow > 4:
                    return False
            else:
                # If it's not the first byte of a character, it should have the pattern '10xxxxxx'
                if not (byte & 0xC0 == 0x80):
                    return False

            num_bytes_to_follow -= 1
        else:
            # If the MSB is not set, it must be a single-byte character (ASCII), so num_bytes_to_follow should be 0
            if num_bytes_to_follow != 0:
                return False

    # After processing all bytes, if num_bytes_to_follow is not zero, it means an incomplete character was found
    return num_bytes_to_follow == 0

# Test the function
data_set1 = [197, 130, 1]  # Represents a valid UTF-8 encoding of a character
data_set2 = [235, 140, 4]  # Represents an invalid UTF-8 encoding

print(validUTF8(data_set1))  # Output: True
print(validUTF8(data_set2))  # Output: False

