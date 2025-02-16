# Function to calculate the optimal cost of a binary search tree
def optimal_bst(keys, freq, n):
   
    cost = [[0 for x in range(n)] for y in range(n)]

   
    for i in range(n):
        cost[i][i] = freq[i]

   
    for length in range(2, n + 1):  
        for i in range(n - length + 1):
            j = i + length - 1 
            cost[i][j] = float('inf')  

            
            for r in range(i, j + 1):
                # Calculate the cost if r is the root
                left_cost = cost[i][r - 1] if r > i else 0  # Left subtree cost
                right_cost = cost[r + 1][j] if r < j else 0  # Right subtree cost
                # Total cost is the cost of left subtree + right subtree + sum of frequencies in the range keys[i..j]
                total_cost = left_cost + right_cost + sum(freq[i:j + 1])
                # Update the minimum cost for the range keys[i..j]
                cost[i][j] = min(cost[i][j], total_cost)

    # The final result is the minimum cost for the whole tree (i.e., for the range keys[0..n-1])
    return cost[0][n - 1]

# User input for number of keys
n = int(input("Enter the number of keys: "))

# User input for keys and frequencies
keys = []
freq = []

print("Enter the keys and their frequencies:")

for i in range(n):
    key = int(input(f"Enter key {i + 1}: "))
    frequency = int(input(f"Enter frequency for key {key}: "))
    keys.append(key)
    freq.append(frequency)


result = optimal_bst(keys, freq, n)

# Display the result
print(f"The minimum cost of the Optimal Binary Search Tree is: {result}")
