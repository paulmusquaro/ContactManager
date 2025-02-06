contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper

@input_error
def hello_command():
    return "How can I help you?"

@input_error
def add_contact_command(params):
    try:
        name, phone = params.split(" ", 1)
        contacts[name.lower()] = phone
        return f"Added contact: {name} - {phone}"
    except ValueError:
        return "Give me name and phone please"

@input_error
def change_contact_command(params):
    try:
        name, phone = params.split(" ", 1)
        if name.lower() in contacts:
            contacts[name.lower()] = phone
            return f"Changed contact: {name} - {phone}"
        else:
            return f"Contact {name} not found"
    except ValueError:
        return "Give me name and phone please"

@input_error
def phone_command(name):
    if name.lower() in contacts:
        return f"Phone number for {name}: {contacts[name.lower()]}"
    else:
        return f"Contact {name} not found"

@input_error
def show_all_command(params=None):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available"

def main():
    global contacts
    
    commands = {
        "hello": hello_command,
        "add": add_contact_command,
        "change": change_contact_command,
        "phone": phone_command,
        "show all": show_all_command,
        "good bye": "Good bye!",
        "close": "Good bye!",
        "exit": "Good bye!"
    }

    while True:
        user_input = input("Enter command: ").lower()
        if user_input in commands:
            if user_input in ["good bye", "close", "exit"]:
                print(commands[user_input])
                break
            else:
                command = commands[user_input]
                if callable(command):
                    if user_input == "hello" or user_input == "show all":
                        result = command()
                        print(result)
                    else:
                        params = input("Enter parameters: ")
                        result = command(params)
                        print(result)
                else:
                    print(command)
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()