# Exercise 1: Implement the Euclidean Distance Function
def euclidean_distance(p1, p2):
    pass


p1 = [5, 3]
p2 = [3, 7]


# Exercise 2: Find the k Nearest Neighbors
def get_neighbors(training_data, test_point, k):
    pass


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


# Exercise 3: Classify a New Data Point
def classify(neighbors):
    # Extract labels from neighbors and count occurrences
    pass


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