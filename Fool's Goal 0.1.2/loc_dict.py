# Location Dictionary

locations = {

    # Location base-line to copy paste
    "roomname": {
        "description": """Room-Desc""",
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
            "Look Around" : "look_dining", #done
            "Look Table" : "dining_clue", #done
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

    #########################
    # Floor 2
    #########################

    # Floor 2 - Landing
    "floor2_landing": {
        "description": """You head up the staircase, the old wood groaning underfoot with every step. The air up here feels thicker, heavier, as if the house itself is holding its breath. The landing is dim, the weak light barely cutting through the shadows that seem to cling to the corners. The walls are cracked, peeling, like they've been forgotten over time. A faint musty smell lingers, and the silence is unsettling—broken only by the occasional creak of the house settling.""",
        "options": {
            "look around" : "look_landing", # DONE
            "Enter Bedroom" : "enter2_bedroom", # puzzle done
            "Enter Guestroom" : "enter2_guestroom", # Done
           #  "Enter Laundry" : "enter2_laundry", # NOT READY
            "Enter Bathroom" : "enter2_bathroom", # done
            "Enter Storage" : "enter2_storage", # done
            "Enter Recreation" : "enter2_recreation", # done
            "Go Downstairs" : "enter_hall", #done
        }
    },

    # Floor 2 - Bedroom
    "floor2_bedroom": {
        "description": """You step inside, and the first thing that hits you is the smell—dried roses, aged perfume, and something sharper, metallic, lingering beneath it. The air is unnaturally still, thick like it hasn’t been disturbed in years, yet there’s not a speck of dust.
        \nThe massive four-poster bed is made too perfectly, the crimson sheets smooth, untouched. But the longer you stare, the more it feels like someone was just there. The high-backed chair near the fireplace is turned slightly away, as if someone had been sitting in it, watching the door… waiting. The fire has long since burned out, but the embers glow faintly, refusing to die.""",
        "options": {
            "Look around" : "look2_bedroom", #done
            "Landing" : "floor2_landing" #done
        }
    },

    # Floor 2 - Guest Room
    "floor2_guestroom": {
        "description": """The door pushes open, the bed is a mess, sheets tangled and torn, dark stains seeping into the fabric. The furniture is scratched, deep grooves in the wood, as if something, or someone, had spent nights pacing, restless.""",
        "options": {
            "Look around" : "look2_guestroom", # done
            "Landing" : "floor2_landing" # done
        }
    },

    # Floor 2 - Laundry
    "floor2_laundry": {
        "description": """The door creaks open, and the room smells of mildew, damp clothes, and a faint, chemical tang that makes your skin crawl. The washer and dryer stand silently in the corner, their doors slightly ajar, like they’ve been abandoned mid-cycle. Dirty laundry is heaped on the floor, some items stained dark, others ripped as if someone had been searching for something—or hiding it.
        \nThe shelves along the walls are cluttered with cleaning supplies, but some jars are broken or open, their contents spilled across the floor, sticky and congealing in dark puddles. A faded, stained rag lies in the corner, soaked in something that smells strangely metallic.""",
        "options": {
            "Look Clothes" : "laundry_clothes",
            "Look Shelves" : "laundry_shelves",
            "Look Washer" : "laundry_washer",
            "Landing" : "floor2_landing"
        }
    },

    "floor2_bathroom": {
        "description": """The bathroom feels constricted, as though the walls are closing in around you. The tiles on the floor are cracked and stained, remnants of water damage long forgotten. The sink is old, its porcelain chipped, and something dark clings to the corners. A small stream of water drips from the faucet, the rhythmic sound too loud in the silence.
        \nThe shower curtain is half-drawn, concealing the tub, but you can see dark stains near its edges, like they’ve been left there for an eternity. A single framed picture hangs crookedly on the wall—a landscape that doesn’t seem to belong here, but it’s the way the edges curl that unsettles you most.""",
        "options": {
            "Look Picture" : "bathroom_portrait", # done
            "Look Sink" : "bathroom_sink", # done
            "Look Bath" : "bathroom_clue", #done
            "Landing" : "floor2_landing" #done
        }
    },

    # Floor 2 - Storage
    "floor2_storage": {
        "description": """You step into the cramped, dimly lit space. Boxes are stacked haphazardly against the walls, some collapsed under the weight of forgotten memories. Dust coats every surface, and the air feels dense, heavy. Every movement stirs up a fine, choking powder that hangs in the air, settling on the back of your throat.
        \nA few broken crates lie scattered on the floor, the remnants of their contents spilled—old papers, glass bottles, and scraps of cloth. One crate is overturned, its contents twisted and scattered, but something wrapped in tattered fabric lies beneath the debris.
        \nA rusted metal chest sits motionless in the corner, its lock hanging loosely. The faintest gleam of something metallic shines through the darkness, drawing your gaze.""",
        "options": {
            "Look Crate" : "storage_crate", # done
            "Look Chest" : "storage_chest", # done
            "Look Darkness" : "storage_dark", # done
            "Landing" : "floor2_landing"
        }
    },

    # Floor 2 - Recreation
    "floor2_recreation": {
        "description": """As you enter, you get hit with a waft of heavy, sweet perfume that clings to the air, almost choking in its intensity. The velvet curtains hang low, casting the room in a dim, private glow. The furniture, rich and dark, feels far too inviting. Each piece designed for more than comfort. A chaise lounge rests in the center, its plush red fabric worn soft with use, as if it’s been molded to fit the body of someone who’s spent far too long lost in its embrace.""",
        "options": {
            "Look around" : "look2_recreation", #done
            "Landing" : "floor2_landing" # done
        }
    },

    #########################
    # Floor 3
    #########################

    "floor3_labhall": {
        "description": """Room-Desc""",
        "options": {
            "Look around" : "look_m1",
        }
    },
}

