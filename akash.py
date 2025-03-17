def calcRedundantBits(m):
    """Calculate the number of redundant bits needed."""
    for i in range(m):
        if (2**i >= m + i + 1):
            return i

def posRedundantBits(data, r):
    """Position the redundant bits in the data."""
    j = 0
    k = 1
    m = len(data)
    res = ''
    
    for i in range(1, m + r + 1):
        if (i == 2**j):  # Place '0' at redundant bit positions
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]  # Place data bits
            k += 1
    return res[::-1]

def calcParityBits(arr, r):
    """Calculate parity bits and update the Hamming Code."""
    n = len(arr)
    
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if (j & (2**i) == (2**i)):  # Check bit positions for parity calculation
                val = val ^ int(arr[-1 * j])
        arr = arr[:n - (2**i)] + str(val) + arr[n - (2**i) + 1:]
    
    return arr

def detectError(arr, nr):
    """Detect if there is an error and return the error position."""
    n = len(arr)
    res = 0
    
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if (j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val * (10**i)
    
    return int(str(res), 2)  # Convert binary to decimal

# Given data
data = '1011001'
m = len(data)

# Step 1: Calculate redundant bits
r = calcRedundantBits(m)

# Step 2: Position redundant bits
arr = posRedundantBits(data, r)

# Step 3: Calculate parity bits
arr = calcParityBits(arr, r)

print("Data transferred is:", arr)

# Introduce an error in the transmitted data
arr = '11101001110'  # Example of received data with error
print("Error Data is:", arr)

# Step 4: Detect error
correction = detectError(arr, r)

if correction == 0:
    print("There is no error in the received message.")
else:
    print("The position of error is at bit:", len(arr) - correction + 1, "from the left")
