# Imports
import math
from collections import Counter
#______________________________________________________________________

# Exercise 1: Implement the Euclidean Distance Function
def euclidean_distance(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Points must have the same dimensions")
    
    squared_diff = [(a - b) ** 2 for a, b in zip(p1, p2)]
    distance = math.sqrt(sum(squared_diff))
    return distance

p1 = [5, 3]
p2 = [3, 7]
print("Euclidean Distance:", euclidean_distance(p1, p2))
#______________________________________________________________________

# Exercise 2: Find the k Nearest Neighbors
def get_neighbors(training_data, test_point, k):
    distances = []
    for data_point in training_data:
        point = data_point[:-1]
        label = data_point[-1]
        dist = euclidean_distance(point, test_point)
        distances.append((point, label, dist))
    
    distances.sort(key=lambda x: x[2])  # sort by distance
    neighbors = distances[:k]
    return neighbors

# example values
training_data = [
    [2, 3, 'A'],
    [3, 5, 'A'],
    [1, 8, 'B'],
    [6, 2, 'B'],
    [7, 3, 'A'],
    [8, 6, 'B']
]

test_point = (5, 10)  # 'A' or 'B' assuming k = 3
k = 3

print(get_neighbors(training_data, test_point, k))
#______________________________________________________________________

# Exercise 3: Classify a New Data Point
def classify(neighbors):
    # Extract labels from neighbors and count occurrences
    labels = [label for _, label, _ in neighbors]
    most_common = Counter(labels).most_common(1)
    return most_common[0][0]

# Example usage
neighbors = [
    ([2, 3], 'A', 7.0),
    ([3, 5], 'A', 5.0),
    ([1, 8], 'B', 3.0)
]

print("Classified label:", classify(neighbors))
#______________________________________________________________________

# Exercise 4: Full Test of KNN Implementation
# Define dataset
dataset = [
    [2, 3, 'A'],
    [3, 5, 'A'],
    [1, 8, 'B'],
    [6, 2, 'B'],
    [7, 3, 'A'],
    [8, 6, 'B']
]

# New data point to classify
test_point = [5, 3]
k = 3

# Find neighbors and classify
neighbors = get_neighbors(dataset, test_point, k)
prediction = classify(neighbors)

print(f"The predicted class for point {test_point} is '{prediction}'")  # Example output: 'A'
#______________________________________________________________________