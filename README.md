# Fool's Goal

## Contents
- [Introduction](#introduction)
- [How To Play](#how-to-play)
- [Mermaid](#mermaid)
- [Links](#links)
- [Walkthrough](#walkthrough)

## Me
Hi, I’m Ethan, a computer science student. This project started as part of a course assignment but also serves as a stepping stone in my journey to making my own games. My friend and I share an interest in game development. We both aspire to create a big game and have even collaborated on projects together.

## My game
This is a text-based horror RPG set in a mysterious mansion filled with disturbing secrets. As the protagonist, you’re searching for your missing daughter, only to uncover gruesome experiments and unsettling truths. Explore, solve puzzles, and survive as you uncover the fate of your daughter.

---

# How To Play

## Commands

The game is entirely text-based, requiring typed commands to progress.

You’ll always have a set of core commands to navigate and interact with, but new options can appear as you interact with certain commands.

## Exploration

You can explore at your own pace as I implemented a, sort-of, free roam system allowing you to enter and exit rooms at your leisure. There is a set path to progress but I didn't enforce a set order you need to do them in. 

## Inventory

TBA

## Combat 

TBA

---

# Walkthrough

TBA

---

# Mermaid

## Full Flow Chart
```mermaid

  flowchart TD

subgraph main_menu
    title[Fool's Goal] --> m_menu[Main Menu]
    m_menu --> start[Start Game]
    m_menu --> m_settings[Main Settings]
    m_menu --> exit[Exit Game]
end

%% Various settings 

m_settings --> settings
i_settings --> settings
subgraph config
    settings --> s_menu[Settings Menu]
    s_menu --> res[Resolution?]
        res --> test_res[Text/ASCII Test]
    s_menu --> b_main[Back to Main Menu]
        b_main --> m_menu
    s_menu --> b_int[Back to interface]
end
b_int --> int_input


%% Game Mechanics

subgraph interface
narr_text[Dynamic Narrative text preceeding every command]
narr_text --> int_input{Interface Input}
int_input --> int_mov[Movement]
int_input --> int_act[Action]
int_input --> int_inv[Open inventory]
int_input --> i_settings[Interface Settings]
end

%% Interface Connections
int_input --> inv_comm
int_input --> mov_comm
int_input --> act_comm

subgraph inventory
int_inv --> inv_menu[Inventory]
inv_menu --> list_inv[List Gear + Inventory including stats]
inv_menu --> inv_comm{Inventory Input}
inv_comm --> select[Command Item_Name]
    select --> use[Use Item]
    select --> drop[Drop Item]
    select --> equip[Equip Item]
    select --> unequip[Unequip Item]
    drop --> trash[Trashes Item]
    drop --> destroy[Destroys Item]
end

subgraph movement
int_mov --> mov_comm{Move Input}
    mov_comm --> north[Move North]
    mov_comm --> south[Move South]
    mov_comm --> west[Move West]
    mov_comm --> east[Move East]
    north --> forward[Move Forward] --> update_pos --> narr_text
    south --> back[Move Backward] --> update_pos --> narr_text
    west --> left[Move left] --> update_pos --> narr_text
    east --> right[Move Right] --> update_pos --> narr_text
    mov_comm --> up[Move Up] --> update_pos --> narr_text
    mov_comm --> down[Move Down] --> update_pos --> narr_text
end

subgraph action
int_act --> act_comm[Action Input]
    act_comm --> take[Take]
end

%% Interface Loop
subgraph int_loop
int_input --> check_val[Check if input is valid]
check_val --yes--> check_mov[Check if command is movement]
check_val --no--> inval_input[Input is invalid, try again] --> narr_text

check_mov --yes--> mov_comm
check_mov --no--> check_act[Check if command is action]

check_act --yes--> update_act[Update Action] --> narr_text
check_act --no--> check_inv[Check if command is inventory]

check_inv --yes--> inv_menu[Open Inventory]
check_inv --no--> check_sett[Check if command is settings]

check_sett --yes--> l_settings[Open settings]
check_sett --no--> inval_input
end

subgraph combat
    encounter --> init_combat[Initiates combat]
    init_combat --> enemy_dialogue[Introduce Enemy]

    subgraph enemy_loop
    init_enem[Introduce Enemy] 
    init_enem --> check_enemy[Checks the enemy]

    check_enemy --alive--> enemy_hp[Checks enemy health]
        enemy_hp --damaged--> dec_enem_hp[Decreases enemy health] --> check_enemy
        enemy_hp --no damage--> e_dlog[Enemy Dialogue]
    check_enemy --dead--> dead_dlog[Enemy Died Dialogue]

    e_dlog --> d_atk[Dialogue for attack]
    e_dlog --> d_h_atk[Dialogue for heavy attack]
    e_dlog --> d_pry[Dialogue for parry]
    e_dlog --> d_dodge[Dialogue for dodge]
    end

    enemy_dialogue--> combat_menu[Combat menu]

    subgraph combat_menu
    c_menu[Combat Menu] --> c_input{Combat Input}
    c_input --> c_comm[Combat Commands]
    c_comm --> atk[Attack]
    c_comm --> h_atk[Heavy Attack]
    c_comm --> pry[Parry]
    c_comm --> dodge[Dodge]
    c_comm --> inv[Open Inventory]
    c_comm --> c_quit[Exit Fight]
    end

%% Combat Loop
subgraph c_loop
c_input --> c_check[Check if Command is valid]
c_check --yes--> check_atk[Check if it is attack]
c_check --no--> inval_combat[Invalid Combat Command] --> c_menu

check_atk --yes--> atk_succ[Check success]
    atk_succ --yes--> update_atk[Attack success] --> check_enemy
    atk_succ --no--> fail_atk[Attack Failed - Enemy Parried] --> check_enemy
check_atk --no--> check_heavy[Check if it is heavy attack]

check_heavy --yes--> heavy_succ[Check success]
    heavy_succ --yes--> update_heavy[Heavy Attack success] --> check_enemy
    heavy_succ --no--> fail_heavy[Heavy Attack Failed - Enemy Dodged] --> check_enemy
check_heavy --no--> check_pry[Check if it is parry]

check_pry --yes--> pry_succ[check success]
    pry_succ --yes--> update_pry[Parry success] --> check_enemy
    pry_succ --no--> fail_pry[Parry failed - You got Heavy Attacked] --> check_enemy
check_pry --no--> check_dodge[Check if it is dodge]

check_dodge --yes--> dodge_succ[check success]
    dodge_succ --yes--> update_dodge[dodge success] --> check_enemy
    dodge_succ --no--> fail_dodge[Dodge Failed - You got attacked] --> check_enemy
check_dodge --no--> inval_combat
end

end

%% Location Starts here

subgraph location_1
end

subgraph location_2
end

subgraph location_3
end

subgraph location_4
end

subgraph location_5
end

subgraph location_6
end

subgraph location_7
end

%% Location Map
location_1 --> location_2
location_1 --> location_3

%% Plot / Story starts here

subgraph chap_1
end

subgraph chap_2
end

subgraph chap_3
end

subgraph chap_4
end

subgraph chap_5
end

subgraph chap_6
end
```

## Main Menu Flow Chart
```
```

## Combat Flow Chart

## Inventory Flow Chart

---

# Changelog

## Version [0.1.0]

- Created the README for the game, outlining the purpose and plan.
- Started designing the structure and flow of the game using a Mermaid flowchart.
- Added a table of contents to the README with links to sections.
- Began organizing the game's core systems and components for future development.

## Version (0.1.1)

- Completed Title Menu
- Started coding the main game loop
- Started and finished coding the puzzles for the first floor.
- Established a basic inventory system for the game.
- Added ASCII art for various interactions in the first floor.


---

# Links

[Github](https://github.com/EthanAlistair)
