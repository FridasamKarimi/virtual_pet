from pet import Pet  # Assuming your Pet class is in a file named pet.py

def main():
    print("🐾 Welcome to the Virtual Pet Game! 🐾")
    pet_name = input("What do you want to name your pet? ")
    my_pet = Pet(pet_name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Check pet status")
        print("5. Train a new trick")
        print("6. Show learned tricks")
        print("7. Exit game")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            my_pet.eat()
            print(f"{my_pet.name} enjoyed the meal!")
        elif choice == '2':
            my_pet.sleep()
            print(f"{my_pet.name} feels rested.")
        elif choice == '3':
            my_pet.play()
            print(f"{my_pet.name} had fun playing!")
        elif choice == '4':
            my_pet.get_status()
        elif choice == '5':
            trick = input("What trick do you want to teach your pet? ")
            my_pet.train(trick)
        elif choice == '6':
            my_pet.show_tricks()
        elif choice == '7':
            print(f"Goodbye! {my_pet.name} will miss you. 🐾")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
