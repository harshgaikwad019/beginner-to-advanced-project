import json


def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email,}
    return person


def display_contact(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_contact(people)
    
    while True:
        number = input("enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("invalid number out of range.")
            else:
                break
        except:
            print("invalid number")
        
    people.pop(number - 1)
    print("person deleted.")


def search(people):
    search_name = input("search for a name: ").lower()
    results =[]

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    
    display_contact(results)
    

print("hi, welcome to the contact managment system.")
print()

with open("contact.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print("contact size;", len(people))
    command  = input("you can 'add', 'delete', or 'search'and 'quit': ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("person added")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "quit":
        break
    else:
        print("invalid command.")

with open("contact.json", "w") as f:
    json.dump({"contacts": people}, f)