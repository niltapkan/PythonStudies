'''
The House
----------
This is week 5 homework. Please complete the necessary functions.
Make sure the game is working properly before you submit. Don't
hesitate to make creative changes to the code. Also do not forget
to add comments to your code!
-----------------------------------------------------------------
STORY:
-Name- wakes up with a unbearable pain in the back of his head.
He doesn't remember how he got there. He's not sure how long he
was laying there on the floor. It is pitch black and he can't see
anything. He tries to turn on the light, but it doesn't work...
-----------------------------------------------------------------
TASK:
The player is trying to find a way out of the house. Every room 
has different tools that player can interact with. The player will
solve how to get out of the house by using the tools. The given
tools are merely suggestions, you can modify them to your liking.
Every room must have at least 3 different tools. The player can
only use one tool at a time. The tools can be either grabbed or
dropped. There is no limit to how many tools the player can keep.
The tools can be just story related interactions. 
Let's review an example of a room and the tools in it;
Living Room:
- Fireplace: Can be used to light the room, if there is an item that
can initiate the fire. (Unless there is light you cannot see what else
is in the room.) 
- Window: Give a creative description of the window and explain that
there is no way to escape the window.
- Blood: A blood stain on the floor. It is sticky and seems to go 
under the carpet.
    - Carpet: (Comes in the options only if the blood is examined)
    Can be lifted which reveals a key.
        - Key: Can be used to open the door to the hallway.
There will be a comment starting with "TODO" in the code where you
need to add your code. There are also hints in the code. You can
use the hints to help you complete the code.
100 Points in total, partial points are possible.
-----------------------------------------------------------------
THE HOUSE STRUCTURE:
_____________________________________
|             |            |        |
|   Bedroom     Living R.           |
|__________  _|____  ______| Garage |
|             |                     |
|   Kitchen       Hallway  |________| 
|_____________|              Toilet |
              |____---_____|________|        
-----------------------------------------------------------------
'''


def start_menu():
    print('''
    --------------------------------------------------
     _____ _   _ _____   _   _  ___  _   _ ____  _____ 
    |_   _| | | | ____| | | | |/ _ \| | | / ___|| ____|
      | | | |_| |  _|   | |_| | | | | | | \___ \|  _|  
      | | |  _  | |___  |  _  | |_| | |_| |___) | |___ 
      |_| |_| |_|_____| |_| |_|\___/ \___/|____/|_____|
                                               
    --------------------------------------------------
    1. Start game
    2. Quit game
    --------------------------------------------------
    ''')

    option = int(input('Please choose one of the options: '))
    print('\n')
    while option != 1 and option != 2:
        option= int(input('Please choose again one of the options: '))
    if option == 1:
        return
    elif option == 2:
        exit
    
def house_init():
    '''
    This function initializes the house. Sets up all the rooms
    and the items - what they do.
    Returns to the dictionary of the house.
    '''
    # TODO: Complete the house dictionary. Every room must have
    # at least 3 tools and all the exits (check the map for the exits). 
    # The tools can be either pickable or not.
    # Every tool must have a description, a statement that
    # says if the tool is pickable or not, and action that
    # the player can do with the tool. You can edit the description
    # and the action as the story progresses. (20 points)
    house = {
        "Living Room": {
            "Description": "You are in the living room. You see a fireplace, a window, and a blood stain on the floor.",
            "Fireplace": {
                "description": "Fireplace seems to be off, if only there was something to light it up...",
                "pickable": False,
                "action": "Light the fire"
            },
            "Key": {
                "description": "A key which stays on the bloody floor",
                "pickable": True,
                "action": "Open the bedroom door"
            },
            "Door": {
                "description":"A door which opens the bedroom"
            },
            "Exits": ["Hallway"],
            },
        "Bedroom": {
            "Description":"The bed is completely tidied up. But there is little bit blood on the table. There is an axe also under the bed.",
            "Axe":{
                "description": "There is an axe also under the bed.",
                "picable": True,
                "action":"Break the kitchen door with axe"
            },
            "Exits": ["Living room"],
            },
                 
        "Kitchen": {
            "Description":""
            "":{
                "d":
                "p":
                "action":
            }
            "Exits":[]
        },
        "Hallway": {},
        "Garage": {},
        "Toilet": {}
        
    }

    return house


def display_story(house, current_room):
    '''
    This function displays the story of the game given player's
    and house's information.
    '''
    room = house[current_room]
    print("\n" + room["Description"])
    print("\nExits: " + str(room["Exits"]))

    # TODO: Display items in the room (9 points)
    
    print("\n")


def examine_item(house, current_room, item, player_inventory):
    '''
    Given the house and the current room, this function will
    examine the selected item.
    '''
    # TODO: Complete the function (40 points)
    # Hint: Use the house dictionary to get the item's description
    # Hint: Use the house dictionary to get the item's pickable status
    


def play_game(house):
    '''
    This function plays the game given the player and house
    information.
    '''
    print("Welcome to the game!")
    # clearing the screen
    print("\n" * 100)
    
    # Story starts here
    # -Name- wakes up with a unbearable pain in the back of his head.
    # He doesn't remember how he got there. He's not sure how long he
    # was laying there on the floor. It is pitch black and he can't see
    # anything. He tries to turn on the light, but it doesn't work...
    print("You wake up with a unbearable pain in the back of your head.")
    print("You don't remember how you got there.") 
    print("You're not sure how long you were laying there on the floor.")
    print("It is pitch black and you can't see anything.")
    print("You try to turn on the light, but it doesn't work...")
    print("\n")

    current_room = "Bedroom"
    player_inventory = {}
    choice = ''

    # Continue the story until the player reaches the end or exits the game
    while choice != 'quit':
        display_story(house, current_room)
        action = input("What do you want to do? ")
        choice = action.lower().strip()
    if choice == 'quit':
        exit
    elif choice == 'new room':
        current_room = "Living room"
    elif choice == 'examines an item':
        examine_item()
    
        # TODO: Check if the action is valid. If not, display an error 
        # message and ask the user to choose again. If user chooses to quit,
        # exit the game. (5 points)

        # TODO: The player can either move to a new room or examine an item.
        # If the player moves to a new room, update the current_room. If the
        # player examines an item, call the examine_item function. Update the
        # player's inventory if necessary. (5 points)
        # Hint: Use the if-elif-else statement

        # TODO: If the player is out of the house, display a message
        # and exit the game. (5 points)
        

def main():
    # main function
    # This is where the logic of the game will be.
    
    # Starting menu for the game displayed
    start_menu()

    # TODO: Greet the player. (1 point)

    # Initialize the house
    house = house_init()

    # play the game
    play_game(house)

    # Greetings and goodbye
    print("Thank you for playing!")
    print("Goodbye!")
main()