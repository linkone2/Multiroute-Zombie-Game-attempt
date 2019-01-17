# The script of the game goes in this file.

# Character Naming?
python:
    playername = renpy.input("Enter Character Name:")
    playername = playername.strip()

# Characters
# Player
define p = Character("[playername]")
# Office Path Characters
# Erin White (Secritary)
define ew = Character("Erin White")
default ew_wave = False
default ew_out = 0


# The game starts here.
label start:

label Path_Office:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Ext_Office:
        "Another day working for Accounting Associates of York County..."
    #

    scene Int_Office:

        #Erin White is In or Out?
    $ ew_out = renpy.random.randint (1,2)      
    if $ ew_out = 1:
        $ ew_is_out = True         
    else:
        pass
    #
            



    if ew_is_out = True:
        #Internal thoughts about Erin White

        "It seems that Erin White is out today..."
        "Erin was always the nice secritary"
        "Always greeting people into the building"
        "Or Helping others"
        "I wonder if she's sick today, or if something happened"
        "Either way, I hope that its nothing serious"

    else:
        ew "{i} Waves at you {/i}"
        
        "Should I go over to her?"
        menu:
            "Yes":
                $ ew_wave = True
                jump ew_wave_yes

            "No":
                "Should I tell her anything?"
            
                menu: 
                    "Good Morning":
                        "Good Morning Erin"
                        #Add jump
                        return 
            
                    "No":
                        #Add jump
                        return

    #            

    label ew_wave_yes:
        ew "Good Morning [playername]!"
        

    



                        

        
        
            
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

   

    # These display lines of dialogue.



    # This ends the game.

    return
