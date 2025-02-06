def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility from 2 to sqrt(n)
        if n % i == 0:  # If divisible, it's not a prime number
            return False
    return True  # If no divisors found, it's a prime number

def generate_spiral_matrix(n):
    """Generate an n x n spiral matrix."""
    # Create an n x n matrix filled with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Initialize boundaries for filling the matrix (left, right, top, bottom)
    left, right, top, bottom = 0, n - 1, 0, n - 1
    num = 1  # Start filling the matrix with number 1
    
    # Loop until the entire matrix is filled
    while left <= right and top <= bottom:
        # Fill top row (left to right)
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1  # Move the top boundary down
        
        # Fill right column (top to bottom)
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1  # Move the right boundary left
        
        # Fill bottom row (right to left)
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1  # Move the bottom boundary up
        
        # Fill left column (bottom to top)
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1  # Move the left boundary right
    
    return matrix  # Return the filled spiral matrix

def get_diagonal_numbers(matrix, n):
    """Get the numbers from both diagonals of the matrix."""
    diagonal_numbers = set()  # Use a set to store diagonal numbers (to avoid duplicates)
    
    # Add numbers from the primary diagonal: (i, i) positions
    for i in range(n):
        diagonal_numbers.add(matrix[i][i])
    
    # Add numbers from the secondary diagonal: (i, n-i-1) positions
    for i in range(n):
        diagonal_numbers.add(matrix[i][n-i-1])
    
    return diagonal_numbers  # Return the set of diagonal numbers

def calculate_prime_percentage(n):
    """Calculate the percentage of prime numbers on both diagonals of an n x n matrix."""
    # Generate the spiral matrix of size n
    matrix = generate_spiral_matrix(n)
    
    # Get the set of diagonal numbers from the matrix
    diagonal_numbers = get_diagonal_numbers(matrix, n)
    
    # Count how many of the diagonal numbers are prime
    prime_count = sum(1 for num in diagonal_numbers if is_prime(num))
    
    # Total count of diagonal numbers
    total_count = len(diagonal_numbers)
    
    # Calculate the percentage of prime numbers on the diagonals
    prime_percentage = (prime_count / total_count) * 100
    
    return prime_percentage  # Return the calculated prime percentage

# Input and output handling
t = int(input())  # Read the number of test cases
for _ in range(t):
    n = int(input())  # Read the size of the spiral matrix (always odd)
    
    # Calculate the percentage of prime numbers on the diagonals for this matrix size
    result = calculate_prime_percentage(n)
    
    # Print the result rounded to 6 decimal places
    print(f"{result:.6f}")

