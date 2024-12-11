# Number of times the number occurs
from collections import Counter

# Step 1: Read the data from the file
with open('my_file.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Split the data into two separate lists
left_list = []
right_list = []

for line in lines:
    # Strip whitespace and check if the line is not empty
    line = line.strip()
    if line:  # Only process non-empty lines
        try:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
        except ValueError:
            print(f"Skipping line due to ValueError: {line}")

# Step 3: Count occurrences of each number in the right list
right_count = Counter(right_list)

# Step 4: Calculate the total similarity score
total_similarity_score = 0

for number in left_list:
    total_similarity_score += number * right_count[number]

# Step 5: Print the total similarity score
print("Total similarity score:", total_similarity_score)