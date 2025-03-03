import menu
import engine

# Main Menu Loop
def main():
    while True:
        choice = menu.main_menu()

        if choice == "start":
            print()
            print("Starting game...")
            print()
            return engine.start_engine()

        elif choice == "settings":
            menu.settings_menu()

        elif choice == "exit":
            print("Exiting game...")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    main()