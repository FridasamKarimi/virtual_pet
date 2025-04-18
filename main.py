from pet import Pet

def main():
    print("🐾 Digital Pet Simulator 🐾")
    my_pet = Pet(input("Name your pet: "))
    
    actions = {
        '1': ('Feed', my_pet.eat),
        '2': ('Sleep', my_pet.sleep),
        '3': ('Play', my_pet.play),
        '4': ('Status', my_pet.get_status),
        '5': ('Train', lambda: my_pet.train(input("Trick to teach: "))),
        '6': ('Tricks', my_pet.show_tricks),
        '7': ('Quit', None)
    }
    
    while True:
        print("\nMain Menu:")
        for key, (desc, _) in actions.items():
            print(f"{key}. {desc}")
        
        choice = input("Choose action: ")
        
        if choice == '7':
            print(f"Goodbye! {my_pet.name} will miss you!")
            break
        
        if choice in actions:
            actions[choice][1]()
        else:
            print("Invalid choice (1-7)")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
