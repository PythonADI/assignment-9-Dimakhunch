def save_users(users, file_path):
    """
    function to save users to a file with folowing format:
    "name,age\n"

    do not return anything
    """
    with open(file_path, 'w') as file:
        for user in users:
            file.write(f"{user['name']},{user['age']}\n")
