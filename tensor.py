import random

# Example tuple
example_tuple = (10, 20, 30, 40, 50)

# Get two random and distinct indices
random_indices = random.sample(range(len(example_tuple)), 2)

# Access the elements at those indices
random_elements = [example_tuple[index] for index in random_indices]

print("Random Indices:", random_indices)
print("Elements at Random Indices:", random_elements)

for i in range(1, 6):
    tuple_value = tuple(random.choice([0, 1]) for _ in range(i))
    print(tuple_value)