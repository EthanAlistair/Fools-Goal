import menu
import engine

# Main Menu Loop
def main():

    menu.title()

    # Menu loop
    while True:
        choice = menu.main_menu()

        if choice in ["start", "start game"]:
            print()
            print("Starting game...")
            print()
            return engine.start_engine()

        elif choice == "settings":
            menu.settings_menu()

        elif choice in ["exit", "quit", "exit game"]:
            print("Exiting game...")
            break

        else:
            print("\nInvalid choice. Please try again.")
            return

if __name__ == "__main__":
    main()