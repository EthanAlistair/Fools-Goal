#########################
# Imports
#########################

# Location Dictionary
from loc_dict import locations


#########################
# Inventory
#########################

player_inventory = []
rusted_key = "Rusted Key"
blood_towel = "Blood Soaked Towel"
carmilla_knife = "Carmilla's Knife" # Utensil with carmilla name engraved
placeholder2 = "PLACEHOLDER2"
painting_fragment = "Painting Fragment"
necklace = "Tooth Necklace"
lock_pick = "Lock-Pick"


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
    with open("ascii/study.txt", "r", encoding="utf-8") as study:
        study_ascii = study.read()
        print(study_ascii)
    print()
    print("A large, ornate bookshelf looms against the far wall, its contents meticulously arranged. Some books seem newer than others, and as you step closer, you hear a faint whisper—not a voice, but the rustling of pages as if something inside is trying to escape.")
    print()
    print("To your left, the desk stands, its dark wood worn with age but polished enough to catch the faint light from a flickering candle.")
    print()
    print("This is the Matron's Study, it must hold something—information about your daughter, or perhaps a clue as to why the call led you here. Something in the disarray hints at a story left unfinished.")

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
    with open("ascii/clock.txt", "r", encoding="utf-8") as clock:
        clock_ascii = clock.read()
        print(clock_ascii)
    print()
    print("The grandfather clock stands against the far wall, its hands frozen in place, the pendulum motionless.")
    print()

    locations["floor1_dining"]["options"]["Look Clock"] = "puzzle_dining"

# Library
def look_library():
    print()
    with open("ascii/book.txt", "r", encoding="utf-8") as book:
        library_book = book.read()
        print(library_book)
    print()
    print("You pick up the book from the desk. Flipping through the pages, you see disturbing images. Human bodies twisted in unnatural ways, limbs rearranged in ways that defy nature.")
    print("Some diagrams depict organs removed or replaced. The most recent pages are smudged, as if written in a hurry.")
    print()
    print("A strange thought crosses your mind, something you try to push away. That phone call. The one where you heard your daughter's voice, faint and distant, before the line cut off.")
    print("This mansion, this place—it’s connected to her. Everything here feels like it’s leading you toward something you’ve been trying to avoid thinking about.")
    print()


#########################
# Floor 2
#########################

# Stairs Floor 2
def stairs_floor2():
    # Check if the player has the rusted key in their inventory
    print()
    with open("ascii/lock_gate.txt", "r", encoding="utf-8") as lock:
        locked_gate = lock.read()
        print(locked_gate)
    print()
    if "Rusted Key" in player_inventory:
        print("\nYou unlock the rusted gate with the key. The heavy metal creaks open, allowing you access to the staircase.")
        print()
        interface("floor2_landing")  # Move the player to the second floor
    else:
        print("\nThe iron gate is locked tight. You need a key to open it.")
        print()
        interface("floor1_hall")

#Landing
def look_landing():
    print()
    print("The portraits on the walls are strangely lifelike, eyes following you as you move. It’s hard to shake the feeling that you're being watched, even though you know you're alone. The doors leading from the landing are all slightly ajar, inviting you forward, but none of them feel safe. At the far end of the hall, a pair of heavy double doors stand shut, their dark wood marred with deep scratches, as if something had once tried to claw its way through. A thick iron lock holds them in place, the keyhole barely visible beneath layers of dust. Unlike the other rooms, this one doesn’t feel abandoned—it feels sealed. Whatever lies beyond wasn’t meant to be disturbed.")

    locations["floor2_landing"]["options"]["Go Laboratory"] = "stairs_floor3"

# Master Bedroom
def look2_bedroom():
    print()
    print("A large painting hangs on the wall. It looks like a portrait of the mansion’s owner, The Matron. same face, same cold expression, repeated over and over. No signs of age on the painting, no dust on the frame. The curtains are drawn tight, shutting out even the dimmest light from outside. You get the sense that they haven’t been opened in years. Maybe ever.")
    print("\nA full-length mirror stands in the corner, its surface catching just enough light to reflect the room… but something about it is off. The wardrobe door is cracked open just enough to show darkness inside. Hanging from the handle is a delicate silver locket, its chain swaying slightly, as if it had just been touched.")
    print()

    locations["floor2_bedroom"]["options"]["Look Mirror"] = "bedroom_mirror"

# Bedroom Mirror
def bedroom_mirror():
    print()
    print("As you approach the mirror, your reflection warps slightly, as if it is not quite your own. The glass appears to ripple and shimmer, as though it is breathing, pulsing with something... ancient. The edges of the mirror are adorned with strange, faded symbols, the writing worn but still legible.")
    print()
    print("The moment you focus on the words, a chill runs through your body. The inscription seems to whisper to you, though the words appear faint and impossible to fully hear, as if they are both in the room and somewhere far away.")
    print()
    print("To pass through, speak her name.")

    locations["floor2_bedroom"]["options"]["Speak To Mirror"] = "puzzle_mirror"


# Guest bedroom
def look2_guestroom():
    print()
    print("The closet door stands ajar, a faint scraping sound echoing from inside as if the wood itself has been worn down by something trying to get out. A few items of clothing hang inside, all pressed and neat, except for one—a dark piece of fabric, out of place, its edges frayed like it had been pulled too hard.")
    print()
    print("A crumpled page from a journal lies abandoned on the nightstand, the ink smeared and blurred in places. The words repeat in jagged strokes, but one stands out.")
    print()
    print('"I thought I heard her... but I don’t know anymore."')
    print()

    locations["floor2_guestroom"]["options"]["Look Journal"] = "guestroom_journal"
    locations["floor2_guestroom"]["options"]["Look closet"] = "guestroom_clue"

# Guestroom Journal
def guestroom_journal():
    print()
    with open("ascii/blood_journal.txt", "r", encoding="utf-8") as journal:
        blood_journal = journal.read()
        print(blood_journal)
        print()
    print("On the bedside table, a worn, leather-bound journal sits. Its cover is faded and cracked, and it feels unnaturally heavy when touched. The journal is sealed with an intricate blood seal, a strange, runic symbol that seems almost alive when you approach. The seal pulsates faintly, as if reacting to your presence.")
    print()

    locations["floor2_guestroom"]["options"]["Open Journal"] = "puzzle_journal"


# Bathroom
def bathroom_sink():
    with open("narrative/bathroom_sink.txt", "r", encoding="utf-8") as sink:
        sink_narr = sink.read()
        print(sink_narr)

def bathroom_portrait():
    with open("narrative/bathroom_portrait.txt", "r", encoding="utf-8") as portrait:
        portrait_narr = portrait.read()
        print(portrait_narr)

# Recreation Room
def look2_recreation():
    print()
    with open("narrative/look_recreation.txt", "r", encoding="utf-8") as recreation:
        recreation_narr = recreation.read()
        print(recreation_narr)

    locations["floor2_recreation"]["options"]["Look Tapestry"] = "recreation_tapestry"
    locations["floor2_recreation"]["options"]["Look Piano"] = "recreation_piano"

def recreation_tapestry():
    print()
    with open("narrative/recreation_tapestry.txt", "r", encoding="utf-8") as tapestry:
        tapestry_narr = tapestry.read()
        print(tapestry_narr)
locations["floor2_recreation"]["options"]["Fix Tapestry"] = "puzzle_tapestry"

def recreation_piano():
    print()
    with open("narrative/recreation_piano.txt", "r", encoding="utf-8") as piano:
        piano_narr = piano.read()
        print(piano_narr)



# Laundry Room
def laundry_clothes():
    print()



#########################
# Floor 3
#########################

# Stairs Floor 3
def stairs_floor3():
    print()
    
    # Add check for item here

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

# Go upstairs to Landing
def floor2_landing():
    interface("floor2_landing")

# Enter the Bedroom
def enter2_bedroom():
    interface("floor2_bedroom")

# Enter the Guest Room
def enter2_guestroom():
    interface("floor2_guestroom")

# Enter the Laundry Room
def enter2_laundry():
    interface("floor2_laundry")

# Enter the Bathroom
def enter2_bathroom():
    interface("floor2_bathroom")

# Enter the Storage Room
def enter2_storage():
    interface("floor2_storage")

# Enter the Recreation Room
def enter2_recreation():
    interface("floor2_recreation")

# Go upstairs to Laboratory
def floor3_laboratory():
    interface("floor3_laboratory")


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
            print("Puzzle complete! You have obtained the Carmilla's Knife.")
            
            # Knife is a clue item
            print()
            with open("ascii/carmilla_knife.txt", "r", encoding="utf-8") as knife:
                knife_ascii = knife.read()
                print(knife_ascii)
                print()
            print("The knife is elegant, its blade straight and gleaming with a faint sheen. The hilt is adorned with intricate carvings, the silver handle smooth and cold to the touch. Along the middle of the blade, faint etchings seem to shimmer, catching the light.")
            print()
            print("As you examine it closely, you make out the name 'Carmilla' engraved in flowing script, the letters aged but unmistakable.")
            print("You can't help but wonder who its for. Carmilla?")
            print()


            # Add placeholder to inventory
            player_inventory.append(carmilla_knife)
            dining_room_puzzle_completed = True
            interface("floor1_dining")
        else:
            print("\nThe hands refuse to move, as though the clock resists your touch.")
            print("Try again.")
            interface("floor1_dining")

# Floor 2 Bedroom Mirror Puzzle
floor2_mirror_puzzle_completed = False

def puzzle_mirror():
    global floor2_mirror_puzzle_completed

    # Check if the puzzle has already been completed
    if floor2_mirror_puzzle_completed:
        print("\nThe mirror is already open. You have already solved the puzzle.")
        return

    print()
    print("The inscription on the mirror is clear now. Speak her name. The words etched along the borders of the mirror seem to glow, faintly, as if urging you to say the right words")
    print()
    print("To pass through, speak her name. To leave, type Landing")

    mirror_choice = input("> ").strip().lower()

    if mirror_choice == "carmilla":
        print()
        print("The moment her name leaves your lips, the mirror shimmers, its surface pulsing with a strange, ethereal light. Cracks spiderweb across the glass, yet instead of breaking, the surface ripples, distorting your reflection until it vanishes entirely. A dark, endless void replaces it.")
        print()
        print("Stepping through, you find yourself in a narrow hidden space, a compartment sealed away long ago.  In front of you, resting atop a small stone pedestal, sits the PLACEHOLDER2.")
        print()
        print("Puzzle complete! You have obtained the PLACEHOLDER2.")

        # complete puzzle events
        floor2_mirror_puzzle_completed = True
        # add item to inventory
        player_inventory.append(placeholder2)
    
        interface("floor2_bedroom")

    elif mirror_choice == "landing":
        print()
        print("You leave the room")
        interface("floor2_landing")
    else:
        print("\nYou cannot pass through the mirror. Try again.")

# Floor 2 Guest Bedroom Journal Puzzle
floor2_journal_puzzle_completed = False

def puzzle_journal():
    global floor2_journal_puzzle_completed

    # Check if the puzzle has already been completed
    if floor2_journal_puzzle_completed:
        print("\nThe journal is already open. You have already solved the puzzle.")
        return

    if "Blood-Soaked Towel" in player_inventory:
        print()
        with open("narrative/blood_journal.txt", "r", encoding="utf-8") as blood_journal:
            blood_journal_narrative = blood_journal.read()
            print(blood_journal_narrative)
        print()
        print("Puzzle complete! You have obtained the Painting Fragment.")

        # complete puzzle events
        floor2_journal_puzzle_completed = True

        locations["floor2_guestroom"]["options"]["Read Journal"] = "floor2_journal2"
        # add item to inventory
        player_inventory.append(painting_fragment)

        interface("floor2_guestroom")
    
    else:
        print("\nYou run your fingers along the seal, but nothing happens.")
        print("The journal remains locked, its cover cold and unyielding.")
        interface("floor2_guestroom")

# Floor 2 Recreation Room Tapestry Puzzle
floor2_tapestry_puzzle_completed = False

def puzzle_tapestry():
    global floor2_tapestry_puzzle_completed

    # Check if the puzzle has already been completed
    if floor2_tapestry_puzzle_completed:
        print("\nThe tapestry is already open. You have already solved the puzzle.")
        return

    if "Painting Fragment" in player_inventory and "Adhesive Paste" in player_inventory:
        print()
        with open("narrative/tapestry.txt", "r", encoding="utf-8") as tapestry:
            tapestry_narrative = tapestry.read()
            print(tapestry_narrative)
        print()
        print("Puzzle complete!")

        # complete puzzle events
        floor2_tapestry_puzzle_completed = True
        # add item to inventory
        player_inventory.append(necklace)

        

        interface("floor2_recreation")
    
    else:
        print("The damage is too great for you to repair with your hands alone. You need the right materials to fix it.")
        interface("floor2_recreation")

# Floor 3 Doors
floor2_lockpick_puzzle_completed = False

def stairs_floor3():
    print()
    with open("ascii/floor3_doors.txt", "r", encoding="utf-8") as doors:
        doors_ascii = doors.read()
        print(doors_ascii)
        print()
        print("The double doors leading to the third floor stand tall and unyielding, their dark wood polished to a near mirror sheen. Intricate carvings swirl along the surface, depicting scenes of figures bowing before a towering, crowned silhouette. The handles are wrought iron, cold to the touch, and shaped like twisting serpents locked in an eternal coil.")
        print()
    
    if "Lock-Pick" in player_inventory:
        lockpick_puzzle()

        # complete puzzle events
        interface("floor3_labhall")
    
    else:
        print("You give the door a firm push, but it doesn’t so much as budge. The lock is solid, heavy, and far too intricate to be forced open. No amount of brute strength will break through, and there are no visible hinges or weak points to exploit.")
        interface("floor2_landing")

def lockpick_puzzle():
    print()
    print("\nYou kneel in front of the double doors, running your fingers along the cold metal lock. The mechanism is finely crafted—deliberate, intricate.")
    print()
    print("You steady your breath and insert the first pick. The tension wrench trembles in your grip as you feel for the pins inside. Three of them. If you move too fast, the mechanism will reset. You need to be careful.")


    # check if puzzle has already been completed

    if floor2_lockpick_puzzle_completed:
        interface("floor3_labhall")
    
    # pins
    correct_pins = [3, 1, 3] # change this to change the "code" (correct pins) for the lock
    attempts = 3

    print("\nThe lock has three pins, each needing to be lifted to the right position.")
    print("Choose numbers between 1 and 5 for each pin. If they align correctly, the lock will open.")

    while attempts > 0:
        print("\nEnter three numbers (1-5) separated by spaces.")
        print("(Example: 1 2 3)")
        guess = input("> ").strip().split()

        #check if input is valid
        if len(guess) != 3 or not all(num.isdigit() for num in guess):
            print("Your fingers slip slightly. That wasn't right. Focus.")
            print("\nInvalid input. Please enter three numbers.")
            continue

        guess = [int(num) for num in guess]

        #check if input is correct
        correct_count = sum(1 for i in range(3) if guess[i] == correct_pins[i])
        close_count = sum(1 for i in range(3) if guess[i] in correct_pins and guess[i] != correct_pins[i])

        if guess == correct_pins:
            print("\nA sharp click echoes through the hall as the final pin slides into place. The tension in the wrench eases, and the lock gives way.")
            print("\nThe double doors shudder, then slowly drift open, revealing the darkness beyond. Whatever waits on the third floor is no longer sealed away.")

            interface("floor3_labhall")

            # complete puzzle events
            floor2_lockpick_puzzle_completed = True
        
            

        if correct_count > 0:
            print(f"{correct_count} pin{' clicks' if correct_count > 1 else ' clicked'} perfectly into place.")
        if close_count > 0:
            print(f"{close_count} pin{' is' if close_count == 1 else 's are'} close but not correct.")
        if correct_count == 0 and close_count == 0:
            print("The lock resists. No pins hold. You grit your teeth and adjust your tools.")

        attempts -= 1
        print(f"{attempts} attempts remaining.")

    print("\nYour pick slips, and you feel the mechanism inside snap back into place. The lock resets, refusing to give way.")
    interface("floor2_landing")  # Puzzle failed


#########################
# Puzzle Clues
#########################

def dining_clue():
    print()
    with open("narrative/dining_clue.txt", "r", encoding="utf-8") as dining_clue:
        dining_clue_narr = dining_clue.read()
        print(dining_clue_narr)
        
def study_clue():
    print()
    with open("narrative/study_clue.txt", "r", encoding="utf-8") as study_clue:
        study_clue_narr = study_clue.read()
        print(study_clue_narr)

# Library Books
def display_books():
    print("\nArrange the books in the correct order by using the following shortcuts:")
    print("Type 'Report' for 'Clinical Report: Final Analysis'")
    print("Type '04' for 'Experiment Log: Subject #04'")
    print("Type 'II' for 'Research Notes: Phase II'")

def library_clue():
    global player_inventory  # Ensure we modify the global player_inventory list

    print()
    with open("narrative/library_clue.txt", "r", encoding="utf-8") as library_clue:
        library_clue_narr = library_clue.read()
        print(library_clue_narr)
    print()

    player_inventory.append("Clinical Report: Final Analysis")
    player_inventory.append("Experiment Log: Subject #04")
    player_inventory.append("Research Notes: Phase II")


    print("\n[Books added to your inventory]")

    # Remove the option after picking up the books
    locations["floor1_library"]["options"].pop("Look Gap", None)

# Floor 2 Guest Bedroom Journal Clue
def guestroom_clue():
    print()
    with open("narrative/guest_clue.txt", "r", encoding="utf-8") as guest_clue:
        guest_clue_narr = guest_clue.read()
        print(guest_clue_narr)

# Floor 2 Bathroom Clue - Bloody Towel
def bathroom_clue():
    print()
    with open("ascii/blood_soaked_towel.txt", "r", encoding="utf-8") as blood_soaked_towel:
        blood_soaked_towel_ascii = blood_soaked_towel.read()
        print(blood_soaked_towel_ascii)
    print()
    with open("narrative/bloody_towel_clue.txt", "r", encoding="utf-8") as bloody_towel_clue:
        bloody_towel_clue_narr = bloody_towel_clue.read()
        print(bloody_towel_clue_narr)
        print()

    #add bloody towel to inventory
    print("Blood-Soaked Towel added to your inventory")
    player_inventory.append("Blood-Soaked Towel")

# Floor 2 Storage Crate
def storage_crate():
    print()
    with open("narrative/storage_crate.txt", "r", encoding="utf-8") as storage_crate:
        storage_crate_narr = storage_crate.read()
        print(storage_crate_narr)

    print()
    print("Adhesive Paste added to your inventory")
    player_inventory.append("Adhesive Paste")
    interface("floor2_storage")

# Floor 2 Storage Darkness
def storage_dark():
    print()
    with open("narrative/storage_dark.txt", "r", encoding="utf-8") as storage_dark:
        storage_dark_narr = storage_dark.read()
        print(storage_dark_narr)
    print()

    print()
    print("Lock-Pick added to your inventory")
    player_inventory.append("Lock-Pick")

    interface("floor2_storage")

# Floor 2 Storage Chest
def storage_chest():
    print()
    with open("narrative/storage_chest.txt", "r", encoding="utf-8") as storage_chest:
        storage_chest_narr = storage_chest.read()
        print(storage_chest_narr)
    print()


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
    print("\n- Inventory")
    
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

        # Keep the player in the same room after an action unless moving and re-prints the interface options for that room
        if valid_option not in ["Enter hall", 
                                "Enter study", 
                                "Enter dining", 
                                "Enter library", 
                                "Back entrance", 
                                "Go Upstairs",
                                "Go Downstairs",
                                "Landing",
                                "Enter Bedroom",
                                "Enter Guestroom",
                                "Enter Laundry",
                                "Enter Bathroom",
                                "Enter Storage",
                                "Enter Recreation"]:  #Keep adding movement commands here
            interface(location)  
    else:
        # Handle invalid input
        print("\nInvalid command. Try again.")
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
# Game Start
#########################

def start_engine():

    # Introductory Narrative
    print()
    # Ascii art for intro
    with open("ascii/intro.txt", "r", encoding="utf-8") as intro:
        intro_ascii = intro.read()
        print(intro_ascii)
    print()
    print()
    with open("narrative/intro_narr.txt", "r", encoding="utf-8") as intro_narr:
        intro_narrative = intro_narr.read()
        print(intro_narrative)
    print()


# End Narrative

    current_location = "mansion_entrance"

    while True:
        interface(current_location)