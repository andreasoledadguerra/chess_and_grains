def square(n):
    """
    There once was a wise servant who saved the life of a prince.  
    The king, grateful for his service, promised to grant him any reward he desired.  
    The servant, knowing the king's passion for chess, made a humble request:  
    one grain of wheat on the first square of a chessboard, with the amount doubling on each subsequent square.  
    This function calculates the number of grains of wheat on a given square (1 to 64)  
    following this pattern: 1, 2, 4, 8, 16, ... (powers of 2).  
    Parameters:
        n (int): The square number (1-based index). Must be between 1 and 64.
    Returns:
        int: The number of grains on the nth square.
    Raises:
    ValueError: If n is not between 1 and 64.
    """
    if not(0 <= n <= 64):
        raise ValueError("square must be between 0 and 64")
    return pow(2,n)

def total():
    """
    After hearing the servant's request, the king gladly agreed—until he realized the true cost.  
    The total number of grains across all 64 squares is astonishing:  
    a sum so large that it surpasses the entire kingdom's wheat production.  

    This function calculates the total number of grains on the entire chessboard  
    by summing all the squares:  
    1 + 2 + 4 + 8 + 16 + ... + 2^63 = 2^64 - 1

    Returns:
        int: The total number of grains on all 64 squares.
    """
    return pow(2, 64) -1