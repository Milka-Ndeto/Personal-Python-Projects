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

# Step 3: Sort both lists
left_list.sort()
right_list.sort()

# Step 4: Pair the numbers and calculate the total distance
total_distance = 0

for left, right in zip(left_list, right_list):
    distance = abs(left - right)
    total_distance += distance

# Step 5: Print the total distance
print("Total distance:", total_distance)