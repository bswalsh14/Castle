init:

    # Set up the window title.
    $ config.window_title = "The Castle Game"

# Now, we declare the images that are used in the program.

    # Backgrounds.
    image entrance = Image("entrance.jpg")
    image hallway = Image("hallway.jpg")
    image door = Image("door.jpg")
    image main = Image("main.jpg")
    image black = Solid((0, 0, 0, 255))
    
    # Inventory 
    $ axe = 0
    $ key = 0
    $ unlock = 0

# The game starts here.

label start:

    scene black
    with fade
    
    "Welcome to Castle Neely. You're here because of a legend which states that there is hidden treasure within this castle,
     and those who find it are granted a lifetime of wealth. Will you be the lucky adventurer who finds the treasure?"
    
    $ name = renpy.input("What is your name?")
    $ name = name.strip()
    
    if name == "":
        $ name="Daring Dave"
    
    "Pleased to meet you, %(name)s!"
    
    jump mainroom

label mainroom:

    "You are in a large room with a cathedral ceiling. The door out is to the North. There is a stairway to your West. 
     There is a dark hallway to the South."
    
    menu:
        "I would like to..."
        
        "Try the front door":
            jump frontdoor

        "Go up the stairway":
            if unlock is 0:
                jump stairway
            if unlock >=1:
                jump stairwayNL
         
        "Explore the hallway":
            jump hallway
            
label frontdoor:
    
    if key is 0:
        "The door is locked shut." 
        jump mainroom
    if key >= 1:
        "You try the small key but it doesn't fit. Maybe it's for another door?"
        jump mainroom

label stairway:
    
    if key is 0 and axe is 0:
        "At the top of the stairs is a door with a rusty metal lock. You try the handle and it doesn't budge." 
        jump mainroom
        
    else:
        menu:
            "I would like to..."

            "Go back to the main room":
                jump mainroom

            "Use the key to unlock the door" if key >= 1:
                jump attic

            "Use the axe to break down the door" if axe >= 1:
                jump badending

label stairwayNL:
    
    "At the top of the stairs is the unlocked door."
    
    menu:
            "I would like to..."

            "Go back to the main room":
                jump mainroom

            "Go through the door":
                jump attic

label hallway:

    "The hallway is dimly lit. There are small candles along the walls. To the North is the main room. To the South is what looks like a brightly lit room."
    
    menu:
        "I would like to..."

        "Go back to the main room":
            jump mainroom

        "Enter the room to the South":
            jump lounge

label lounge:
    
    "You walk into a cozy little lounge. To the North is the hallway. To the West is a small library. To the East is a large cabinet. 
     There is a fireplace blasting heat to the South."
    
    menu:
        "I would like to..."

        "Go back to the hallway":
            jump hallway

        "Go into the library":
            jump library
            
        "Examine the lounge":
            jump examinelounge

label examinelounge:

    menu:
        "I would like to..."
        
        "Go back to the lounge":
            jump lounge

        "Examine the cabinet":
            jump cabinet   

        "Examine the fireplace":
            if axe is 0:
                jump fireplace
            if axe >= 1:
                jump fireplaceNA
            

label fireplace:
    
    "The fire is roaring, yet noone is there tending to it. There is a stack of wood next to the fireplace with an axe to the side."
    
    menu:
        "I would like to..."

        "Go back to the lounge":
            jump lounge

        "Pick up the axe":
            jump takeaxe
            
label fireplaceNA:

    "The fire is roaring, yet noone is there tending to it. There is a stack of wood next to the fireplace."
    jump lounge
                  
label takeaxe:
    
    "You pick up the axe."
    $ axe = axe + 1
    
    jump lounge
    
label cabinet:

    "You examine the cabinet. There are old pots and pans strewn about the bottom of the cabinet. There is an old coat crumpled up as well. 
     There doesn't seem to be anything of interest here."
    
    jump lounge

label library:
    
    "You walk through the door into the library. Books line the walls on all sides. In the middle of the room is a table. 
     On that table is a large red book with strange markings on it. The door back to the lounge is to the East."
    
    menu:

        "I would like to..."

        "Go back to the lounge":

            jump lounge
            
        "Pick up the large red book":
            if key is 0:
                jump examinebook
            if key >= 1:
                jump examinebookNK
           
label examinebook:

    "You pick up the big red book with strange markings on the cover. You open it and there are symbols on the pages that do not seem like any language you've seen.
     As you flip through it, you find a small key between the pages."
    
    menu:

        "I would like to..."

        "Go back to the library":
            jump library
            
        "Take the small key":
            jump takekey
            
label takekey:

    "You take the key"
    $ key = key + 1
    
    jump library

label examinebookNK:

    "You pick up the big red book with strange markings on the cover. You open it and there are symbols on the pages that do not seem like any language you've seen."
    
    jump library

label attic:
    
    "You find yourself in a massive attic. In the North-West corner there is a massive sleeping bear. Unaware of your presence, it's breathing is steady as it sleeps. 
     To the East is the doorway back out."
    
    menu:
        "I would like to..."

        "Attack the bear":
            jump bear
            
        "Go back to the stairway":
            jump stairwayNL

label bear:
    
    if axe is 0:
        "You attempt to kill the bear with your bare hands. The bear awakens angrily and throws you into the wall with its massive strength. 
         Dazed against the wall, the bear lunges at you and rips you apart. " 
        jump continue
    if axe >= 1:
        "With one sickening thud, you kill the bear with your axe. Moving its body, there is a trap door below. It opens easily."
        jump ending
        
label badending:
    
    "As you hack away at the door, you feel it start to give and you kick it open. You take a step inside what looks to be a massive attic. In the North-West 
     corner of the room, you see a massive creature moving incredibly quickly towards you. Without any time to react the giant creature tears you apart, roaring the entire time."
    jump continue
        
label ending:
    
    "You climb down the ladder and find yourself in a brightly lit room filled with gold. With the rusty key in hand, you carry as much gold as you can, 
    leaving the castle, intent on coming back for the rest of the gold."
    jump continue

label continue:

    scene black
    with fade
    
    "Thanks for playing [name]! Play again if you'd like to see all endings!"

    return
    
