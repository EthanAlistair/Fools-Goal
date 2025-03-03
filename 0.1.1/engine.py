# Main story
#########################
# Inventory
#########################

player_inventory = []
rusted_key = "Rusted key"
placeholder = "PLACEHOLDER"

#########################
# Dictionary
#########################
locations = {

    # Location base-line to copy paste
    "roomname": {
        "description": """Room Desc""",
        "options": {
            "Look around" : "look_m1",
        }
    },
    # End base-line

    # Mansion Entrance
    "mansion_entrance": {
        "description": """\nYou stand before the massive wooden doors of the mansion. The iron-wrought gate behind you creaks as the wind howls through the trees. Rain pounds against the stone steps, mixing with the distant sound of thunder. The mansion’s towering frame looms above, its windows dark and watchful. The door is locked, but something about the air here feels... wrong, as if you’re being expected.""",
        "options": {
            "Look around" : "look_entrance", #done
        }
    },

    # Floor 1 - Main Hall
    "floor1_hall": {
        "description": """\nThe grand hall is unsettling in its eerie elegance. A massive chandelier hangs above, its dim, flickering lights casting long, crawling shadows across the polished floors. The air carries a faint metallic scent, and portraits of unfamiliar faces line the walls, their hollow eyes seeming to follow your every step. The silence is heavy, broken only by the occasional creak of the mansion settling. Several doors lead to different rooms, each hiding something within.""",
        "options": {
            "Look around" : "look_hall", # done - ASCII
            "Enter Study" : "enter_study", #done
            "Enter Dining" : "enter_dining", #done
            "Enter Library" : "enter_library", #done
            "Back Entrance" : "enter_entrance" #done
        }
    },

    #Floor 1 - Study
    "floor1_study": {
        "description": """\nThe study is lined with bookshelves, but many of the tomes are strangely untouched, as if placed here for decoration rather than knowledge. The fireplace is cold, but a single candle flickers on the desk, illuminating a stack of aged, handwritten notes. A leather chair sits in the corner, its surface unnervingly pristine despite the dust coating everything else.""",
        "options": {
            "Look Around" : "look_study", # done - ASCII
            "Main Hall" : "enter_hall" #done
        }
    },

    # Floor 1 - Dining Room
    "floor1_dining": {
        "description": """\nA long dining table stretches across the room, its surface set with ornate but unused silverware. A faint scent of decayed roses clings to the air, mixed with something else, almost medicinal, like the scent of antiseptics. Plates rest in front of empty chairs, but one seat at the head of the table is pulled back, as if someone had only just left.""",
        "options": {
            "Look Around" : "look_dining",
            "Look Table" : "dining_clue",
            "Main Hall" : "enter_hall" #done
        }
    },

    # Floor 1 - Library
    "floor1_library": {
        "description": """\nTowering bookshelves stretch toward the high ceiling, filled with tomes bound in cracked leather. The room is oddly warm compared to the rest of the mansion, but the heat feels unnatural, almost suffocating. A single book lies open on the reading desk, its pages filled with medical diagrams—distorted images of the human body, altered in ways that defy nature. A ladder leans against one of the bookshelves, its rungs stained with something dark. A strange gap in the books on one shelf catches your eye.""",
        "options": {
            "Look Around" : "look_library", # done - ASCII
            "Look Gap" : "library_clue", # done
            "Main Hall" : "enter_hall" #done
        }
    },
}

#########################
# Action Functions
#########################

#Entrance 
def look_entrance():
    print()
    print("You look around the entrance. The fog swirls in the air, and the mansion looms over you. As you examine the door more closely, you notice it's old and worn, with several cracks visible. ")
    print()
    print("It looks weak, possibly splintered. You feel like you could probably kick it down if you wanted to.")
    print()
    
    # Shows another option after looking around
    locations["mansion_entrance"]["options"]["Kick the door"] = "kick_door"

    return

# Kick door to enter the mansion
def kick_door():
    print()
    print("You take a few steps back and kick the door with all your strength. The old wood splinters with a loud crack and the door gives way, swinging open. You’re in!")
    print()

    # Adds the option to enter the main hall after kicking down the door if you go back to the entrance for some reason
    locations["mansion_entrance"]["options"]["Enter mansion"] = "enter_hall"

    interface("floor1_hall")

# Main Hall
def look_hall():
    print()
    print("You look around the grand hall. Dust coats the furniture, and the faded tapestries on the walls seem to sag with age.")
    print("At the far end, a grand staircase winds its way up, disappearing into the darkness. But it's blocked by a heavy iron gate, its lock rusted but still sturdy")
    print()

    # Shows go upstairs option
    locations["floor1_hall"]["options"]["Go Upstairs"] = "stairs_floor2"

# Study
def look_study():
    print()
    with open("ascii/study.txt", "r") as study:
        study_ascii = study.read()
        print(study_ascii)
    print()
    print("A large, ornate bookshelf looms against the far wall, its contents meticulously arranged. Some books seem newer than others, and as you step closer, you hear a faint whisper—not a voice, but the rustling of pages as if something inside is trying to escape.")
    print()
    print("To your left, the desk stands, its dark wood worn with age but polished enough to catch the faint light from a flickering candle.")
    print()
    print("This is the study, and surely, it must hold something—information about your daughter, or perhaps a clue as to why the call led you here. Something in the disarray hints at a story left unfinished.")

    # Shows the option to examine the desk
    locations["floor1_study"]["options"]["Look Desk"] = "study_clue"

    # Check if the player has the books from library for the puzzle
    if not all(book in player_inventory for book in [
        "Clinical Report: Final Analysis",
        "Experiment Log: Subject #04",
        "Research Notes: Phase II"
    ]):
        print("\nYou don't have all the books needed to solve the puzzle. You must first visit the library to collect them.")
        return  
    else:

        # If the player has the books, show the option to start the puzzle
        print()
        print("You notice the bookshelf is slightly ajar. It looks like you could rearrange the books to unlock a compartment.")
        print()
        locations["floor1_study"]["options"]["Look Bookshelf"] = "puzzle_study"

# Dining Room
def look_dining():
    print()
    with open("ascii/clock.txt", "r") as clock:
        clock_ascii = clock.read()
        print(clock_ascii)
    print()
    print("The grandfather clock stands against the far wall, its hands frozen in place, the pendulum motionless.")
    print()

    locations["floor1_dining"]["options"]["Look Clock"] = "puzzle_dining"

# Library
def look_library():
    print()
    with open("ascii/book.txt", "r") as book:
        library_book = book.read()
        print(library_book)
    print()
    print("You pick up the book from the desk. Flipping through the pages, you see disturbing images. Human bodies twisted in unnatural ways, limbs rearranged in ways that defy nature.")
    print("Some diagrams depict organs removed or replaced. The most recent pages are smudged, as if written in a hurry.")
    print()
    print("A strange thought crosses your mind, something you try to push away. That phone call. The one where you heard your daughter's voice, faint and distant, before the line cut off.")
    print("This mansion, this place—it’s connected to her. Everything here feels like it’s leading you toward something you’ve been trying to avoid thinking about.")
    print()

# Stairs
def stairs_floor2():
    # Check if the player has the rusted key in their inventory
    print()
    with open("ascii/lock_gate.txt", "r") as lock:
        locked_gate = lock.read()
        print(locked_gate)
    print()
    if "Rusted key" in player_inventory:
        print("\nYou unlock the rusted gate with the key. The heavy metal creaks open, allowing you access to the staircase.")
        print()
        interface("floor2")  # Move the player to the second floor
    else:
        print("\nThe iron gate is locked tight. You need a key to open it.")
        print()

#########################
# Location Functions
#########################

# Go back to entrance
def back_entrance():
    interface("mansion_entrance")

# Enter the Main Hall
def enter_hall():
    interface("floor1_hall")

# Enter the Study
def enter_study():
    interface("floor1_study")

# Enter the Dining Room
def enter_dining():
    interface("floor1_dining")

# Enter the Library
def enter_library():
    interface("floor1_library")


#########################
# Puzzle Dictionary
#########################

book_tags = {
    "Clinical Report: Final Analysis" : "Report",
    "Experiment Log: Subject #04" : "04",
    "Research Notes: Phase II" : "II"
}

#########################
# Puzzle Functions
#########################

# Study Room Puzzle
study_puzzle_completed = False

def puzzle_study():
    global study_puzzle_completed 

    # Check if the puzzle has already been completed
    if study_puzzle_completed:
        print("\nThe bookshelf is already unlocked. You have already solved the puzzle.")
        return

    # Check if the player has collected the books
    if not all(book in player_inventory for book in [
        "Clinical Report: Final Analysis",
        "Experiment Log: Subject #04",
        "Research Notes: Phase II"
    ]):
        print("\nYou haven't collected all the books from the library yet. Go back to the library to retrieve them before solving the puzzle.")
        return

    print("\nYou approach the bookshelf in the study. The books appear to be out of order, leaving gaps between them and there's a strange energy in the air.")
    print("The books you collected from the library seem to whisper as you place them in order. You need to arrange the books using their shortcuts:")
    print()

    display_books()

    # Correct order
    correct_order = ["04", "ii", "report"]
    
    # Player's order
    player_order = []

    # Loop through the 3 tags for the correct order
    for i in range(3):  
        # Ask the player for each tag input one by one
        tag = input(f"Enter the tag for book #{i + 1}: ").strip().lower()  # Normalize input to lowercase
        
        # Check if the tag is correct
        if tag == correct_order[i]:
            player_order.append(tag)
        else:
            print(f"The tag '{tag}' is incorrect. Try again.")
            return  

    # After all 3 tags are correctly entered, check the order
    if player_order == correct_order:
        print("\nYou place the books in the correct order on the shelf. Suddenly, the bookshelf creaks open, revealing a hidden compartment.")
        print("Inside the compartment, you find a rusted key.")
        print()
        print("Puzzle complete! You have obtained the rusted key.")

        # Add rusted key to inventory
        player_inventory.append(rusted_key)
        study_puzzle_completed = True 
    else:
        print("\nThe books are in the wrong order. The bookshelf remains locked.")
        print("Try again.")


 

# Dining Room Puzzle
dining_room_puzzle_completed = False
def puzzle_dining():
    global dining_room_puzzle_completed

    # Check if the puzzle has already been completed
    if dining_room_puzzle_completed:
        print("\nThe clock is already working. You have already solved the puzzle.")
        return

    print()
    print("You approach, drawn to the silent timepiece. Its brass hands are frozen at a 00:00, stuck as if cursed by some force.")
    print("You wonder if the clock might be able to start working if you can place the hands in the right position... but what could that be?")

    while True:

        # Gets input from the player
        hour = input("Enter the hour(0-12): ")
        minute = input("Enter the minute(0-59): ")

        # Checks if the time is correct
        if hour == "5" and minute == "18":
            print("\nThe hands of the clock shift into place with a deep, unsettling click.")
            print("The clock begins to tick again, the sound echoing through the room with an eerie rhythm.")
            print("Suddenly, it chimes, its notes reverberating in the stillness, before a hidden compartment beneath the clock creaks open.")
            print("Inside the compartment, you find a PLACEHOLDER.")
            print()
            print("Puzzle complete! You have obtained the PLACEHOLDER.")

            # Add placeholder to inventory
            player_inventory.append(placeholder)
            dining_room_puzzle_completed = True
            break
        else:
            print("\nThe hands refuse to move, as though the clock resists your touch.")
            print("Try again.")


#########################
# Puzzle Clues
#########################

def dining_clue():
    print()
    print("You walk toward the end of the dining table, approach the chair at the head of the table")
    print()
    print("As you approach, your eyes are drawn to the shattered plate on the floor, its porcelain pieces scattered among the remains of a half-eaten meal.")
    print("The rest of the table seems almost too perfect. Five plates are still neatly set, untouched, as though still waiting for people to arrive.")
    print()
    print("As you stare at the plates, a small, nagging thought crosses your mind.")
    print()
    print("FIVE")
    print()
    print("The number sticks with you, lingering. Could it be a coincidence?")
    print("Your gaze flicks toward the broken plate, scattered on the floor. Why was it destroyed?")
    print("You brush the idea aside, dismissing it as nothing more than a coincidence. It can’t be related, can it?")
def study_clue():
    print()
    print("You begin to rummage through the scattered pages on the desk. ")
    print("You come across a journal entry, written hastily and with a sense of despair")
    print()
    print("Subject 18 was our greatest hope. The serum showed unprecedented results—better than all the others before her. But in the end, she too succumbed. The final phase was too much. It always is. They never survive.")
    print()
    print("You continue flipping through more pages, where the other subjects are listed")
    print("Subject 1 — terminated after rapid deterioration")
    print("Subject 7 - metabolic collapse, subject unresponsive")
    print("Subject 21 — excessive hemorrhaging, no recovery.")
    print("The same grim fates are repeated for all the others.")
    print()
    print("But 18... That number lingers in your mind, gnawing at you. For some reason, it feels like it means something. You glance back at the journal.")
    print()
    print("It reminds you, for some reason, of your daughter. May 18th. Your mind races for a moment, and a tight knot forms in your stomach. But no—there's no way. The number's just a coincidence. It has to be.")
    print("You shake your head, refusing to entertain the thought. It's ridiculous. The connection can't be real.")
    print()
    print("Still, your gaze lingers for a moment longer than you'd like, before you push the thought aside. It’s just another failed experiment. Just a number.")
    print()
# Library Books
def display_books():
    print("\nArrange the books in the correct order by using the following shortcuts:")
    print("Type 'Report' for 'Clinical Report: Final Analysis'")
    print("Type '04' for 'Experiment Log: Subject #04'")
    print("Type 'II' for 'Research Notes: Phase II'")

def library_clue():
    global player_inventory  # Ensure we modify the global player_inventory list
    print()
    print("As you pull the books from the shelf, you notice that each one has a strange, cryptic title written on the spine. Each is part of the mansion's dark history.")

    print("'Clinical Report: Final Analysis'")
    print("'Experiment Log: Subject #04'")
    print("'Research Notes: Phase II'")

    print("\nThese books might be important... You take them.")

    player_inventory.append("Clinical Report: Final Analysis")
    player_inventory.append("Experiment Log: Subject #04")
    player_inventory.append("Research Notes: Phase II")


    print("\n[Books added to your inventory]")

    # Remove the option after picking up the books
    locations["floor1_library"]["options"].pop("Look Gap", None)


#########################
# Interface
#########################
# Had to get help to handle this part since my original code kept giving me error after error and it got to a point where I didn't know how to fix it

# Interface function to handle user input
def interface(location):

    # Check if the player has visited the room before, then prints room description
    # This way, the description doesnt get printed every time you finish an action
    if not locations[location].get("visited", False):
        print(locations[location]["description"])
        locations[location]["visited"] = True

    # Prints the options
    options = locations[location]["options"]
    print("\nWhat would you like to do?")
    print()
    for option in options:
        print(f"- {option}")

    # additional option to print inventory
    print("- Inventory")
    
    # Handles user input
    choice = input("\n> ").strip().lower()

    # Checks if input is to call inventory
    if choice == "inventory":
        show_inventory()
        print()
        interface(location)

    valid_option = None
    for option in options:
        if choice == option.lower():
            valid_option = option
            break

    if valid_option:
        action = options[valid_option]
        globals()[action]()

        # Keep the player in the same room after an action unless moving
        if valid_option not in ["Enter hall", "Enter study", "Enter dining", "Enter library", "Back entrance", "Go Upstairs"]:  #Keep adding movement commands here
            interface(location)  
    else:
        # Handle invalid input
        print("Invalid command. Try again.")
        print()
        interface(location)

# Function to display the inventory
def show_inventory():
    if player_inventory:
        print("\nYour inventory:")
        for item in player_inventory:
            print(f"- {item}")
    else:
        print("\nYour inventory is empty.")


#########################
# Puzzle Tracking
#########################


#########################
# Game Start
#########################

def start_engine():

    # Introductory Narrative
    print()
    with open("ascii/intro.txt", "r") as intro:
        intro_ascii = intro.read()
        print(intro_ascii)
    print()
    print("The rain pelts against the windshield, the rhythmic thuds almost hypnotic as you drive through the dense, desolate woods.")
    print()
    print("The road is narrow, barely visible through the heavy downpour. It twists and turns like a living thing, dragging you deeper into the heart of the forest.")
    print()
    print("Your knuckles are pale as your grip tightens on the steering wheel. Beside you, the empty seat feels heavier than it should.")
    print()
    print("Your name is PLACEHOLDER")
    print()
    print("You never thought you'd be here. But that phone call—you can still hear it in your head, the voice, the faintest whisper of your daughter’s name, Rose.")
    print()
    print("You thought she was gone. You thought you were done with all of this. But now you're driving through the dark, your heart pounding in your chest. You thought it was over, but the past doesn’t let go so easily.")
    print()
    print("The lights of the mansion finally break through the trees, a towering silhouette that seems to watch your every move. The gate groans as it opens in front of you, the rusted metal protesting your arrival.")
    print()
    print("You can barely make out the outline of the house, but even from here, you feel something strange, something wrong. The mansion isn't just old—it's alive with a presence you can't ignore.")
    print()
    print("This isn’t a place for answers.")
    print()
    print("This is a place that takes.")
    print()
    print()

# End Narrative

    current_location = "mansion_entrance"

    while True:
        interface(current_location)