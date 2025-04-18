from pet import Pet

def main():
    """Main game loop for interacting with the virtual pet."""
    print("🐾 Digital Pet Simulator 🐾")
    
    # Create pet with user-provided name
    my_pet = Pet(input("Name your pet: "))
    
    # Define available actions 
    # Format: 'choice': ('Description', action_function)
    actions = {
        '1': ('Feed', my_pet.eat),
        '2': ('Sleep', my_pet.sleep),
        '3': ('Play', my_pet.play),
        '4': ('Status', my_pet.get_status),
        '5': ('Train', lambda: my_pet.train(input("Trick to teach: "))),
        '6': ('Tricks', my_pet.show_tricks),
        '7': ('Quit', None)
    }
    
    # Main game loop
    while True:
        print("\nMain Menu:")
        # Display menu options from the actions dictionary
        for key, (desc, _) in actions.items():
            print(f"{key}. {desc}")
        
        # Get user input
        choice = input("Choose action: ")
        
        # Handle quit option
        if choice == '7':
            print(f"Goodbye! {my_pet.name} will miss you, come back soon!")
            break
        
        # Execute chosen action if valid
        if choice in actions:
            actions[choice][1]()  # Call the associated function
        else:
            print("Invalid choice (1-7)")
        
        # Pause to let user see results before clearing screen
        input("Press Enter to continue...")

if __name__ == "__main__":
    # Only run if executed directly (not when imported)
    main()
