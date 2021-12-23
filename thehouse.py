
def start_menu():
    print("""
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
""")
#start_menu()

options = ["Start game", "Quit game"]  
'''def choice():
    op = input('Your choice: ')
    if op == "Start game":
        print('Welcome to The House!')
    elif op == '1':
        print('Welcome to The House!')
        house_init()
    elif op == 'Start':
        print('Welcome to The House!')    
    elif op == "Quit game":
        print('Good bye!')
    elif op == '2':
        print('Good bye!')
    else:
        op = input('Please choose again: ')
        
    # def exit():
    #     return 'Come again!'
    # op == '2' or 'Quit game'    
    # while op == False:
    #     print(exit())

choice()'''
house = {
        "Living Room": {
            "Description": "You are in the living room. You see a fireplace, a window, and a blood stain on the floor.",
            "Fireplace": {
                "description": "Fireplace seems to be off, if only there was something to light it up...",
                "pickable": False,
                "action": "Light the fire"
            },
            "Tool2": {
                "description": "The window is open and it's really cold inside. You should close the window immediately.",
                "pickable": True,
                "action": "Close the window"
            },
            "Tool3": {"There is blood on the floor. Someone here was horribly injured. So where is the injured? Is the person who hurt her still at home?"},
            "Exits": ["Hallway", "Garage", "Bedroom"],
        },
        "Kitchen": {},
        "Hallway": {},
        "Garage": {},
        "Toilet": {}
    }
for key, value in house.get():
    print(f'{key}: {value}')


