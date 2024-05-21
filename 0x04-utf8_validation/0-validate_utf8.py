#!/usr/bin/python3
"""
UTF-8 Validation module
"""

def validUTF8(data):
    """
    Validate if a given list of integers represents valid UTF-8 encoding.
    
    Args:
    data: List of integers where each integer represents a byte of data
    
    Returns:
    True if the data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6
    
    for num in data:
        # Get the binary representation of the byte
        bin_rep = bin(num).replace('0b', '').rjust(8, '0')[-8:]
        
        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            for bit in bin_rep:
                if bit == '0':
                    break
                num_bytes += 1
            
            if num_bytes == 0:
                continue
                
            if num_bytes == 1 or num_bytes > 4:
                return False
            
        else:
            # For the remaining bytes, they must start with '10'
            if not (num & mask1 and not (num & mask2)):
                return False
        
        num_bytes -= 1
    
    return num_bytes == 0

