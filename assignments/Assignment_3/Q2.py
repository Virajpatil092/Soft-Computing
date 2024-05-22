# Define input features and weights
x1 = [0, 0, 1, 1]  # Roundness (0 for not round, 1 for round)
x2 = [0, 1, 0, 1]  # Color (0 for not purple, 1 for purple)
w1 = 1
w2 = 1
t = 2  # Threshold

# Output
print("Object | Round | Color | O (Eats)")
print("----------------------------------")
for i in range(len(x1)):
    # Calculate weighted sum
    weighted_sum = x1[i]*w1 + x2[i]*w2
    
    # Determine if the bird eats or not based on the threshold
    if weighted_sum >= t:
        eats = 1  # Bird eats
    else:
        eats = 0  # Bird does not eat
    
    # Print the details
    print(f"  {i+1}    |   {x1[i]}   |   {x2[i]}   |     {eats}")
