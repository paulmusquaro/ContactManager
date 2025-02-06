# ContactManager

ContactManager is a simple command-line contact management application. It allows users to add, update, retrieve, and display contacts using an intuitive CLI interface.

## Features
- Add new contacts with a name and phone number
- Update existing contact details
- Retrieve a contact's phone number
- Display all saved contacts
- Simple and user-friendly command-line interface

## Installation
No installation is required. Simply clone the repository and run the script using Python.

```sh
# Clone the repository
git clone https://github.com/paulmusquaro/ContactManager.git
cd ContactManager

# Run the script
python main.py
```

## Usage
The application supports the following commands:

| Command      | Description |
|-------------|-------------|
| `hello`     | Greets the user |
| `add`       | Adds a new contact (requires name and phone number) |
| `change`    | Updates an existing contact's phone number |
| `phone`     | Retrieves a contact's phone number |
| `show all`  | Displays all saved contacts |
| `good bye` / `close` / `exit` | Exits the application |

### Example Usage
```
Enter command: add
Enter parameters: John 123456789
Added contact: John - 123456789

Enter command: phone
Enter parameters: John
Phone number for John: 123456789

Enter command: show all
John: 123456789

Enter command: exit
Good bye!
```

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
