from main import generate_food

snake = [(3, 3), (3, 2), (3, 1)]

# Test food generation
food = generate_food()

assert food not in snake

print("All tests passed!")