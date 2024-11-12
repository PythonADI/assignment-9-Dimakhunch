import random

NAME_CHOICES = [
    "John",
    "Jane",
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Jack",
]


def generate_random_users(n, output_file):
    """
    Generate n random users and write them to a file.
    Each user should be on a new line and have the format "Name,Age".
    Name should be randomly selected from the NAME_CHOICES list.

    Do not return anything, just write to the file.
    """
    with open(output_file, 'a') as f:
        for _ in range(n):
            name = random.choice(NAME_CHOICES)
            age = random.randint(18, 65)
            f.write(f"{name}, {age}\n")
