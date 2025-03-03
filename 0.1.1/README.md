# Introduction

## Contents
[Introduction](#introduction)
[How To Play](#how-to-play)
[Mermaid](#mermaid)
[Links](#links)
[Walkthrough](#walkthrough)

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

    init[Start the game] --> intro[print intro]
    intro --> locationinfo[Description of location1]
    locationinfo --> explore1inst1{What do you do next?}

    subgraph explorationloc1[Exploration for location1 - Main House]
    explore1inst1 --> loc1action1[first action - Enter house]
    explore1inst1 --> loc1action2[second action - Walk to the side of house]
    explore1inst1 --> loc1action3[third action - Walk behind house]
    explore1inst1 --> openinv[Open your inventory]

    loc1action2 --Finds side door leading to the kitchen--> explore1inst2{What now?}
    explore1inst2 --> loc1action4[Enter kitchen]
    explore1inst2 --> loc1action5[Keep walking behind the house]
    explore1inst2 --> loc1action6[Go back to the front]
    explore1inst2 --> openinv[Open your inventory]

    loc1action3 --Finds cellar door--> explore1inst3{what now?}
    explore1inst3 --> loc1action7[Enter cellar]
    explore1inst3 --> loc1action8[Go back to the front]
    explore1inst3 --> openinv[Open your inventory]
    end
    loc1action6 --> locationinfo
    loc1action8 --> locationinfo

    subgraph explorationloc2
    loc1action1 --> loc2intro[introduces the next location - Inside the house]
    loc2intro --> explore2inst1{Where do you go now?}
    explore2inst1 --> loc2action1[Living Room]
    explore2inst1 --> loc2action2[Upstairs]
    explore2inst1 --> loc2action3[Kitchen]
    explore2inst1 --> loc2action4[Basement]
    end

    subgraph inventory
    openinv --> inv[opens the inventory]
    inv --> selectinv{select an item from your inventory}
    selectinv --> item1[first item] --> selectinv
    selectinv --> item2[second item] --> selectinv
    selectinv --> item3[third item] --> selectinv
    selectinv --> item4[fourth item] --> selectinv
    selectinv --> closeinv
    closeinv --> exploreinst
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