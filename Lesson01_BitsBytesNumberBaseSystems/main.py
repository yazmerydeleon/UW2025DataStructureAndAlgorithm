print('URL Shorteners Problem')
'''
In this assignment, you're being tasked to write a program to convert a base-62 number to base-10 and back again.
'''

base_62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# 1. For our first problem, write a function that converts a given base-62 string
#    into an integer. Only a single string will be provided, and it will be up to
#    11 characters in length.

# Function to convert a base-62 string to an integer.
def to_base_10(videoId):

    """
    Converts a base-62 string into a base-10 integer.

    Parameters:
        videoId (str): The base-62 string to convert.

    Returns:
        int: The corresponding base-10 integer.
    """

    #print('Base62 string: ', videoId)
    result = 0

    for char in videoId:
        index = base_62.index(char) # Find the index of the character in base_62      
        result = result * 62 + index  # Use iterative multiplication
        print(f'Adding "{char}" (index {index}) results in: {result}')

    #print('The Decimal number is: ', result)     
    return result

# 2. Write a function that does the opposite of the previous one. 
# That is, it encodes a base 10 number into base 62
# producing a string that represents the same number.

# Function to convert an integer to a base-62 string.
def to_base_62(number):
    """
    Converts a base-10 integer into a base-62 string.

    Parameters:
        number (int): The base-10 integer to convert.

    Returns:
        string: The corresponding base-62 string.
    """
    base62String = ''
    #print('Base10 integer: ', number)
    while (number > 0):
        remainder = number % 62
        number = number // 62
        #print(f'Quotient: {number}, Remainder: {remainder}')
        char= base_62[remainder]
        base62String = char + base62String
    #print('Base62 string:', base62String)
    return base62String

#if __name__ == "__main__":
    # Example usage
    #to_base_10('LpuPe81bc2w')
    #to_base_62(18327995462734721974)