import os

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.next = None

class ZooKeeper:
    def __init__(self):
        self.head = None
        self.filename = "zoo_data.txt"
        self.load_data()

    def add_animal(self, species, name):
        new_animal = Animal(species, name)
        if not self.head:
            self.head = new_animal
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_animal
        self.save_data()
        print(f"Added animal: Species {species}, Name: {name}")

    def remove_animal(self, name):
        if not self.head:
            print("Zoo is empty.")
            return

        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            self.save_data()
            print(f"Removed animal: {name}")
            return

        current = self.head
        while current.next:
            if current.next.name.lower() == name.lower():
                current.next = current.next.next
                self.save_data()
                print(f"Removed animal: {name}")
                return
            current = current.next
        print(f"Animal named '{name}' not found.")

    def record_birth(self, parent_name, new_species, new_name):
        current = self.head
        while current:
            if current.name.lower() == parent_name.lower():
                self.add_animal(new_species, new_name)
                print(f"Recorded birth: Parent: {parent_name}, New animal - Species: {new_species}, Name: {new_name}")
                return
            current = current.next
        print(f"Parent animal named '{parent_name}' not found.")

    def display_animals(self):
        if not self.head:
            print("Zoo is empty.")
            return
        current = self.head
        while current:
            print(f"Species: {current.species}, Name: {current.name}")
            current = current.next

    def save_data(self):
        with open(self.filename, 'w') as file:
            current = self.head
            while current:
                file.write(f"{current.species},{current.name}\n")
                current = current.next

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    species, name = line.strip().split(',')
                    self.add_animal(int(species), name)


zoo = ZooKeeper()
while True:
    print("\n--- Zoo Keeper Animal Monitoring System ---")
    print(" 1. Add animal")
    print(" 2. Remove animal")
    print(" 3. Record birth")
    print(" 4. Display all animals")
    print(" 5. Exit")
    choice = input("Enter your choice (1-5): ")

    try:
        if choice == '1':
            species = int(input("Enter species (as integer): "))
            name = input("Enter animal name: ")
            zoo.add_animal(species, name)
        elif choice == '2':
            name = input("Enter animal name to remove: ")
            zoo.remove_animal(name)
        elif choice == '3':
            parent_name = input("Enter parent animal name: ")
            new_species = int(input("Enter new animal species (as integer): "))
            new_name = input("Enter new animal name: ")
            zoo.record_birth(parent_name, new_species, new_name)
        elif choice == '4':
            zoo.display_animals()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter an integer for species.")
    except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")