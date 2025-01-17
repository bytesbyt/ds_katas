"""
A complete text game, the program will let users move through rooms based on user input and get descriptions
of each room. To create this, you'll need to establish the direction in which the user can move, a
way to track how far the user has moved (and therefore which room he/she is in), and to print
out a description. You'll also need to set limits for how far the user can move. In other words,
create “walls” around the rooms that tell the user, “You can't move further in this direction.”
"""

def adventure_game():

    print(

        """
        Welcome to my house! You can stop any time by typing 'stop'.

        Here is the floor plan of the house: 

         -------------------------------------------
        |   Kitchen   |   Bedroom    |   Office     |
         -------------------------------------------
        |   Toilet    |   Storage    |  Guest Room  |
         -------------------------------------------
        """
    )

    kitchen = "kitchen, where the spice of life comes alive"
    bedroom = "bedroom, where the magic happens"
    office = "office, the source of wealth"
    toilet = "toilet you know what happens here"
    storage = "storage, where there are all sorts of stuff"
    guest_room = "guest room, where you have friends"

    # list of rooms
    room = [[kitchen, bedroom, office],[toilet, storage, guest_room]]
    # start in the first row
    current_row_index = 0
    # start in the first column (kitchen)
    current_column_index = 0
    # walk counter
    walk_count = 0
    # current room list indexing stored in current_room variable 
    current_room = room[current_row_index][current_column_index]

    while True:
        # current room list indexing stored in current_room variable 
        current_room = room[current_row_index][current_column_index]
        # let users move through rooms based on user input and get descriptions of each room
        direction = input(f"You are in {current_room}.\nWhich direction would you like to move to?\nPlease enter left/right/up/down/stop: ").lower()

        if direction == "left":
            # set limits for how far the user can move
            if current_column_index == 0:
                print("\nYou can't move further left, try the other direction.")
            # track which room user has moved to
            else:
                current_column_index -= 1
                walk_count += 1
                print(f"\nYou moved left to the {room[current_row_index][current_column_index]}.")

        elif direction == "right":
            # set limits for how far the user can move
            if current_column_index == len(room[current_row_index]) -1:
                print("\nYou can't move further right, try the other direction.")
            # track which room user has moved to
            else:
                current_column_index += 1
                walk_count += 1
                print(f"\nYou moved right to the {room[current_row_index][current_column_index]}.")

        elif direction == "up":
            # set limits for how far the user can move
            if current_row_index == 0:
                print("\nYou can't move further up, try the other direction.")
            # track which room user has moved to
            else:
                current_row_index -= 1
                walk_count += 1
                print(f"\nYou moved up to the {room[current_row_index][current_column_index]}.")

        elif direction == "down":
            # set limits for how far the user can move
            if current_row_index == len(room) -1:
                print("\nYou can't move further down, try the other direction.")
            # track which room user has moved to
            else:
                current_row_index += 1
                walk_count += 1
                print(f"\nYou moved down to the {room[current_row_index][current_column_index]}.")
        
        elif direction == "stop":
            # exits the program
            print(f"\nYou are in the {current_room}. Thank you for your visit!")
            break

        else:
            print("\nInvalid Input. Please try again.")
            continue
        # establish a way to track how far the user has moved
        print(f"\nTotal walks taken: {walk_count}\n")

adventure_game()