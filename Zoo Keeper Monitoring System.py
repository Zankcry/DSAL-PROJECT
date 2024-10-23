import os

class Animal:
    def __init__(self, species, animal_type, name):
        self.species = species
        self.animal_type = animal_type
        self.name = name
        self.next = None

class ZooKeeper:
    def __init__(self):
        self.head = None
        self.filename = "zoo_data.txt"
        self.load_data()
        
    def get_animal_types(self, species):
        animal_types = {
            1: ["Lion", "Tiger", "Bear", "Elephant", "Giraffe", "Monkey"],
            2: ["Eagle", "Penguin", "Parrot", "Owl", "Flamingo", "Peacock"],
            3: ["Snake", "Lizard", "Crocodile", "Turtle", "Iguana", "Gecko"],
            4: ["Frog", "Salamander", "Toad", "Newt"],
            5: ["Shark", "Goldfish", "Clownfish", "Angelfish"],
            6: ["Butterfly", "Ant", "Beetle", "Grasshopper"],
            7: ["Spider", "Scorpion", "Tarantula", "Mite"],
            8: ["Octopus", "Snail", "Squid", "Clam"],
            9: ["Crab", "Lobster", "Shrimp", "Crayfish"],
            10: ["Jellyfish", "Coral", "Sea Anemone", "Hydra"]
        }
        return animal_types.get(species, [])

    def display_categories(self):
        print("\n--- Animal Species Categories ---")
        species_dict = {
            1: "Mammals",
            2: "Birds",
            3: "Reptiles",
            4: "Amphibians",
            5: "Fish",
            6: "Insects",
            7: "Arachnids",
            8: "Mollusks",
            9: "Crustaceans",
            10: "Cnidarians"
        }
        
        for num, species in species_dict.items():
            print(f"{num}. {species}:")
            animal_types = self.get_animal_types(num)
            print("   Available animals:", ", ".join(animal_types))
            print()

    def add_animal(self, species, animal_type, name):
        new_animal = Animal(species, animal_type, name)
        if not self.head:
            self.head = new_animal
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_animal
        self.save_data()
        species_name = self.get_species_name(species)
        print(f"Added animal: Species: {species_name}, Type: {animal_type}, Name: {name}")

    def get_species_name(self, species_num):
        species_dict = {
            1: "Mammals",
            2: "Birds",
            3: "Reptiles",
            4: "Amphibians",
            5: "Fish",
            6: "Insects",
            7: "Arachnids",
            8: "Mollusks",
            9: "Crustaceans",
            10: "Cnidarians"
        }
        return species_dict.get(species_num, "Unknown")

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

    def record_birth(self, parent_name, new_species, new_animal_type, new_name):
        current = self.head
        while current:
            if current.name.lower() == parent_name.lower():
                self.add_animal(new_species, new_animal_type, new_name)
                species_name = self.get_species_name(new_species)
                print(f"Recorded birth: Parent: {parent_name}, New animal - Species: {species_name}, Type: {new_animal_type}, Name: {new_name}")
                return
            current = current.next
        print(f"Parent animal named '{parent_name}' not found.")

    def display_animals(self):
        if not self.head:
            print("Zoo is empty.")
            return
        print("\n--- Current Zoo Animals ---")
        current = self.head
        while current:
            species_name = self.get_species_name(current.species)
            print(f"Species: {species_name}, Type: {current.animal_type}, Name: {current.name}")
            current = current.next

    def save_data(self):
        with open(self.filename, 'w') as file:
            current = self.head
            while current:
                file.write(f"{current.species},{current.animal_type},{current.name}\n")
                current = current.next

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    species, animal_type, name = line.strip().split(',')
                    self.add_animal(int(species), animal_type, name)

zoo = ZooKeeper()
while True:
    print("\n--- Zoo Keeper Animal Monitoring System ---")
    print(" 1. Add animal")
    print(" 2. Remove animal")
    print(" 3. Record birth")
    print(" 4. Display all animals")
    print(" 5. View Categories")
    print(" 6. Exit")
    choice = input("Enter your choice (1-6): ")

    try:
        if choice == '1':
            zoo.display_categories()
            species = int(input("Enter species number (1-10): "))
            if 1 <= species <= 10:
                animal_types = zoo.get_animal_types(species)
                print("\nAvailable animal types:")
                for i, animal_type in enumerate(animal_types, 1):
                    print(f"{i}. {animal_type}")
                type_choice = int(input(f"Enter animal type number (1-{len(animal_types)}): "))
                if 1 <= type_choice <= len(animal_types):
                    name = input("Enter animal name: ")
                    zoo.add_animal(species, animal_types[type_choice-1], name)
                else:
                    print("Invalid animal type number.")
            else:
                print("Invalid species number. Please enter 1-10.")
        elif choice == '2':
            name = input("Enter animal name to remove: ")
            zoo.remove_animal(name)
        elif choice == '3':
            parent_name = input("Enter parent animal name: ")
            zoo.display_categories()
            new_species = int(input("Enter new animal species (1-10): "))
            if 1 <= new_species <= 10:
                animal_types = zoo.get_animal_types(new_species)
                print("\nAvailable animal types:")
                for i, animal_type in enumerate(animal_types, 1):
                    print(f"{i}. {animal_type}")
                type_choice = int(input(f"Enter animal type number (1-{len(animal_types)}): "))
                if 1 <= type_choice <= len(animal_types):
                    new_name = input("Enter new animal name: ")
                    zoo.record_birth(parent_name, new_species, animal_types[type_choice-1], new_name)
                else:
                    print("Invalid animal type number.")
            else:
                print("Invalid species number. Please enter 1-10.")
        elif choice == '4':
            zoo.display_animals()
        elif choice == '5':
            zoo.display_categories()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number for species and animal type.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")